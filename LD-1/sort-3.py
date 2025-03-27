# sort-3.py
import sys

# Masyvas laikyti duomenis, kad paskui juos išrikiuoti
isrikiuota = []

for line in sys.stdin:
  try:
    zona, diena, klientai, siuntu_skaicius = line.split("\t")
    isrikiuota.append([zona, diena, klientai, siuntu_skaicius[:-1]])
    # siuntu_skaicius[:-1] nes svoris baigiasi su \n
  except:
    continue

isrikiuota = sorted(isrikiuota, key=lambda x: (x[0], x[1]))
for zona, diena, klientai, siuntu_skaicius in isrikiuota:
  print(f"{zona}\t{diena}\t{klientai}\t{siuntu_skaicius}")