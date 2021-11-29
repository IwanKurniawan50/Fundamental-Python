# 485 hari

# nyatakan dalam tahun, bulan, minggu  dan hari
# 1 bulan = 30 hari
# 1 tahun = 360 hari
import math

total = 485

tahun = 360
bulan = 30
#minggu = 7

year = (math.floor(total / tahun))
month = (math.floor(total % tahun) / bulan)
day = (math.floor(total % tahun) % bulan)

print(f"485 hari = {year} tahun, {month} bulan dan {day} hari")
