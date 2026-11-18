# Rà soát so sánh 2026-11-11 → 2026-11-18 (ELAPSED 7 ngày)

> Tự động sinh bởi `vr_compare.py`. Chưa có gì được ghi vào DB.

## 1. Kiểm dữ liệu đầu vào
- Dòng đọc được D2: **199** · số UI game: **199** · khớp: **True**
- D1 = snapshot 2026-11-11, 197 dòng **đã lưu** (không phải số trong game).
- Power giảm đơn điệu theo thứ tự đọc: **True** · bộ ba trùng: **0**
- Phủ cặp dòng liền kề: **196/198** — thiếu tại cặp [75, 80]
- `aliases.json` as_of = 2026-11-11 (phải bằng ngày D1: **True**)
- Tên mơ hồ / chưa đọc được ở D2: ['llllllllll', 'llllllllllll', '[?]', 'llllllllllll']
- Phương trình cân đối: {'D2 == matched + D2-only': True, 'D1 == matched + D1-only': True, 'D2 == D1 - left + new (+excluded)': True}

## 2. Loại ngày
- pass1_rate 0.925 (thường > 0.95) · turnover 0.041 (thường < 0.05) · pool_size 195 (thường < 100)
- Chế độ ngày đặc biệt: **False**
- Nhóm đối chứng Pass 1: n=184, median 1.9866%, p90 5.0499%, max 9.5738% → **KP_CEIL 10.5312%** (max of 184-pair control group x 1.1)
- Tỷ lệ Act tụt < 500k trong nhóm đối chứng: 3.8% → tín hiệu rejoin Act≈0 dùng được
- Pass 1/2/3: {1: 184, 2: 10, 3: 0} · RANK_WIN 49

## 3. Cần Ha xác nhận
### 3.1 Đổi tên (người cũ, giữ ID)
- **R350-0011** `Anew27` → `WithLove` (dòng D2 23): renamed (Pass 2): dPower +0.07%, dKP +1.7599%, name similarity 0.14, competitors 0, neighbourhood_size 31
- **R350-0251** `Морффей` → `Морфей` (dòng D2 29): renamed (Pass 2): dPower +1.22%, dKP +3.0955%, name similarity 0.92, competitors 7, neighbourhood_size 151
- **R350-0034** `Be3yhunk` → `Be3vhunk` (dòng D2 42): renamed (Pass 2): dPower +0.76%, dKP +2.1965%, name similarity 0.88, competitors 6, neighbourhood_size 151
- **R350-0098** `lllllllll` → `brayan` (dòng D2 73): renamed (Pass 2): dPower +0.17%, dKP +2.7581%, name similarity 0.83, competitors 7, neighbourhood_size 151
- **R350-0106** `彡MiaMoR彡` → `MiaMoR` (dòng D2 75): renamed (Pass 2): dPower +1.93%, dKP +0.6484%, name similarity 0.86, competitors 0, neighbourhood_size 151
- **R350-0261** `llllllllllll` → `llllllllllll` (dòng D2 119): ambiguous (Pass 2): dPower +3.42%, dKP +4.6556%, name similarity 1.00, competitors 9, neighbourhood_size 151
- **R350-0164** `[?]` → `[?]` (dòng D2 125): ambiguous (Pass 2): dPower +2.05%, dKP +1.4454%, name similarity 1.00, competitors 5, neighbourhood_size 151
- **R350-0195** `llllllllllll` → `llllllllllll` (dòng D2 182): ambiguous (Pass 2): dPower +3.88%, dKP +7.5264%, name similarity 1.00, competitors 0, neighbourhood_size 15

### 3.2 Rejoin (dùng lại ID gốc) và 3.3 người mới
- Dòng D2 6 `FinistBrFalcon` P 300,701,112 KP 43,795,151,620 Act 991,509: ứng viên rejoin: R350-0012 `VeloX` (vắng từ 2026-09-06, 73 ngày, dKP 59.714% = 0.818%/ngày, dPower 15.54%, CÙNG ID này cũng khớp dòng [7] → chưa giải quyết); R350-0250 `FinistBrFalcon` (vắng từ 2026-11-09, 9 ngày, dKP 11.527% = 1.281%/ngày, dPower 0.72%, CÙNG ID này cũng khớp dòng [7] → chưa giải quyết); R350-0019 `Kral38` (vắng từ 2026-09-01, 78 ngày, dKP 395.851% = 5.075%/ngày, dPower 37.14%, CÙNG ID này cũng khớp dòng [7] → chưa giải quyết) · ⚠ tên này xuất hiện trong `note` của snapshot gần đây — kiểm xem Ha có từng loại dòng này khỏi DB không
- Dòng D2 7 `Shebeastinem` P 279,539,984 KP 53,429,331,728 Act 1,058,600: ứng viên rejoin: R350-0014 `Shebeastinem` (vắng từ 2026-11-09, 9 ngày, dKP 3.061% = 0.34%/ngày, dPower 1.29%); R350-0012 `VeloX` (vắng từ 2026-09-06, 73 ngày, dKP 94.849% = 1.299%/ngày, dPower 7.41%, CÙNG ID này cũng khớp dòng [6] → chưa giải quyết); R350-0250 `FinistBrFalcon` (vắng từ 2026-11-09, 9 ngày, dKP 36.061% = 4.007%/ngày, dPower -6.36%, CÙNG ID này cũng khớp dòng [6] → chưa giải quyết); R350-0019 `Kral38` (vắng từ 2026-09-01, 78 ngày, dKP 504.929% = 6.473%/ngày, dPower 27.49%, CÙNG ID này cũng khớp dòng [6] → chưa giải quyết) · ⚠ tên này xuất hiện trong `note` của snapshot gần đây — kiểm xem Ha có từng loại dòng này khỏi DB không
- Dòng D2 167 `Mqmr` P 140,656,053 KP 4,813,427,709 Act 1,004,681: ứng viên rejoin: R350-0177 `Piyush` (vắng từ 2026-09-06, 73 ngày, dKP 19.767% = 0.271%/ngày, dPower -10.81%); R350-0181 `Mqmr` (vắng từ 2026-11-09, 9 ngày, dKP 5.688% = 0.632%/ngày, dPower 0.67%); R350-0134 `darkhof` (vắng từ 2026-09-06, 73 ngày, dKP 77.838% = 1.066%/ngày, dPower -20.75%, CÙNG ID này cũng khớp dòng [191] → chưa giải quyết); R350-0149 `Jon Jones` (vắng từ 2026-09-06, 73 ngày, dKP 87.037% = 1.192%/ngày, dPower -9.17%, CÙNG ID này cũng khớp dòng [191] → chưa giải quyết); R350-0118 `ALANchik` (vắng từ 2026-09-06, 73 ngày, dKP 100.275% = 1.374%/ngày, dPower -8.43%, CÙNG ID này cũng khớp dòng [191] → chưa giải quyết) · ⚠ tên này xuất hiện trong `note` của snapshot gần đây — kiểm xem Ha có từng loại dòng này khỏi DB không
- Dòng D2 191 `dimon29epta` P 119,015,229 KP 3,236,827,577 Act 136,700: ứng viên rejoin: R350-0275 `dimon29epta` (vắng từ 2026-11-02, 16 ngày, dKP 0.0% = 0.0%/ngày, dPower 0.11%); R350-0134 `darkhof` (vắng từ 2026-09-06, 73 ngày, dKP 19.588% = 0.268%/ngày, dPower -32.94%, CÙNG ID này cũng khớp dòng [167] → chưa giải quyết); R350-0149 `Jon Jones` (vắng từ 2026-09-06, 73 ngày, dKP 25.775% = 0.353%/ngày, dPower -23.14%, CÙNG ID này cũng khớp dòng [167] → chưa giải quyết); R350-0118 `ALANchik` (vắng từ 2026-09-06, 73 ngày, dKP 34.677% = 0.475%/ngày, dPower -22.52%, CÙNG ID này cũng khớp dòng [167] → chưa giải quyết); R350-0088 `GRiZLiK 18 rus` (vắng từ 2026-09-06, 73 ngày, dKP 45.574% = 0.624%/ngày, dPower -30.27%) · ⚠ tên này xuất hiện trong `note` của snapshot gần đây — kiểm xem Ha có từng loại dòng này khỏi DB không
- Dòng D2 199 `Legion X` P 46,912,836 KP 93,809,943 Act 0: ứng viên rejoin: R350-0237 `Veterok116` (vắng từ 2026-09-06, 73 ngày, dKP 11.228% = 0.154%/ngày, dPower -31.93%); R350-0221 `Крез` (vắng từ 2026-09-06, 73 ngày, dKP 52.763% = 0.723%/ngày, dPower -28.7%); R350-0222 `MirrKa` (vắng từ 2026-08-24, 86 ngày, dKP 73.424% = 0.854%/ngày, dPower -16.5%); R350-0244 `Троцкий` (vắng từ 2026-09-06, 73 ngày, dKP 254.992% = 3.493%/ngày, dPower 8.54%)

### 3.4 Chưa giải quyết (không được ghi là đã khớp)
- R350-0115 `hab1st` ? `llllllllll`: ambiguous (Pass 2): dPower +2.45%, dKP +2.4933%, name similarity 0.12, competitors 7, neighbourhood_size 151; UNIQUENESS: FAILED
- R350-0044 `KatälønEc` ? `Хам`: renamed (Pass 2): dPower +6.96%, dKP +3.9827%, name similarity 0.00, competitors 1, neighbourhood_size 31; UNIQUENESS: FAILED

## 4. Rời tộc
- R350-0054 `Grace` P 142,487,482 KP 2,494,711,886 — bằng chứng **A**: Power falls between D2 rows 160 MarQ (142,490,905) and 161 ТагилРу (142,344,197), observed adjacent in the same panel: YES
- R350-0279 `FoxWarrior` P 108,846,077 KP 254,630,606 — bằng chứng **A**: Power falls between D2 rows 194 Anton152 (115,263,437) and 195 PrincessSunless (105,100,762), observed adjacent in the same panel: YES
- R350-0280 `VOZVR` P 76,086,590 KP 208,678,384 — bằng chứng **A**: Power falls between D2 rows 197 kira mean count (86,072,981) and 198 Nasty junior (59,068,156), observed adjacent in the same panel: YES

## 5. Điểm bất thường cần Ha để mắt (đã khớp nhưng đáng ghi chú)
- [act_reset] R350-0065 `Urethral Queef` → `Urethral Queef`: Act 59,400 -> 0 (leave/rejoin?)

## 6. Câu hỏi gửi Ha
1. Xác nhận `capture_date` và số thành viên trên UI game (nếu chưa).
2. Xác nhận / bác từng cặp ở 3.1, từng ứng viên ở 3.2, và cách xử lý từng ca ở 3.4.
3. Có dòng nào ở D2 cần loại khỏi DB không (farm, dòng chưa rõ)?
4. Đồng ý các ca rời tộc ở mục 4?
