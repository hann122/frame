# python3 split_flareon13.py flareon13.doc  -> ./split/
import sys,os,struct,hashlib,re
d=open(sys.argv[1],'rb').read(); O='split'; os.makedirs(O+'/cd_udf',exist_ok=True)
def w(p,b): open(f'{O}/{p}','wb').write(b); print(p,len(b))
Z=d.find(b'%%EOF\nPK\x03\x04')+6
w('01_pdf.pdf',d[0x84:Z]); w('03_zip_raw.bin',d[Z:]); w('04_vhd_footer.bin',d[-512:])
# CD raw 2352 -> ISO 2048
n=782; iso=b''.join(d[i*2352+16:i*2352+2064] for i in range(n)); w('02_cd.iso',iso)
# UDF (flat root)
S=2048; sec=lambda k:iso[k*S:]; tag=lambda b:struct.unpack_from('<H',b)[0]
ln,loc=struct.unpack_from('<II',sec(256),16)
for i in range(ln//S):
    b=sec(loc+i)
    if tag(b)==5: P=struct.unpack_from('<I',b,188)[0]
    if tag(b)==6: F=struct.unpack_from('<I',b,252)[0]
lb=lambda k:iso[(P+k)*S:]
def fe(k):
    b=lb(k); ext=tag(b)==266; sz=struct.unpack_from('<Q',b,56)[0]
    lea,lad=struct.unpack_from('<II',b,208 if ext else 168); o=(216 if ext else 176)+lea
    at=struct.unpack_from('<H',b,34)[0]&7
    if at==3: return b[o:o+lad][:sz]
    st=8 if at==0 else 16; out=b''
    for p in range(o,o+lad,st):
        l,pos=struct.unpack_from('<II',b,p); l&=0x3fffffff
        if l: out+=lb(pos)[:l]
    return out[:sz]
root=fe(struct.unpack_from('<I',lb(F),404)[0]); p=0
while p<len(root) and tag(root[p:])==257:
    fc,lfi=root[p+18],root[p+19]; icb=struct.unpack_from('<I',root,p+24)[0]; liu=struct.unpack_from('<H',root,p+36)[0]
    nm=root[p+38+liu+1:p+38+liu+lfi].decode('latin1'); p+=(38+liu+lfi+3)&~3
    if not fc&8: w('cd_udf/'+nm,fe(icb))
# fat Mach-O
f=open(O+'/cd_udf/click_me','rb').read()
for i in range(struct.unpack_from('>I',f,4)[0]):
    ct,cs,off,sz,_=struct.unpack_from('>5I',f,8+i*20); w(f'cd_udf/click_me.arm64_cpusub{cs}',f[off:off+sz])
# PDF RC4 (empty password)
PAD=bytes.fromhex('28BF4E5E4E758A4164004E56FFFA01082E2E00B6D0683E802F0CA9FE6453697A')
Ov=bytes.fromhex(re.search(rb'/O <([0-9a-f]+)>',d).group(1).decode()); ID=bytes.fromhex(re.search(rb'/ID \[<([0-9a-f]+)>',d).group(1).decode())
key=hashlib.md5(PAD+Ov+struct.pack('<i',int(re.search(rb'/P (-?\d+)',d).group(1)))+ID).digest()[:5]
def rc4(k,x):
    s=list(range(256));j=0
    for i in range(256): j=(j+s[i]+k[i%len(k)])&255; s[i],s[j]=s[j],s[i]
    i=j=0;o=bytearray()
    for c in x: i=(i+1)&255;j=(j+s[i])&255;s[i],s[j]=s[j],s[i];o.append(c^s[(s[i]+s[j])&255])
    return bytes(o)
for num,name in ((5,'obj5_content.txt'),(8,'obj8_image.jb2')):
    m=re.search(rb'\n%d 0 obj\n<<.*?/Length (\d+) >>\nstream\n'%num,d,re.S)
    w('pdf_'+name,rc4(hashlib.md5(key+struct.pack('<I',num)[:3]+b'\0\0').digest()[:10],d[m.end():m.end()+int(m.group(1))]))
# ZIP with fixed offsets
b=bytearray(d[Z:]); c=b.find(b'PK\x01\x02'); e=b.find(b'PK\x05\x06')
for q in (c+42,e+16): struct.pack_into('<I',b,q,struct.unpack_from('<I',b,q)[0]-Z)
w('03_flag_encrypted.zip',bytes(b))
