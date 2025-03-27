# sort-1.py
import sys

# Masyvas laikyti duomenis, kad paskui juos išrikiuoti
isrikiuota = []

for line in sys.stdin:
  try:
    marsrutas, siuntu_skaicius, svoris = line.split("\t")
    isrikiuota.append([marsrutas, siuntu_skaicius, svoris[:-1]])
    # svoris[:-1] nes svoris baigiasi su \n
  except:
    continue

isrikiuota = sorted(isrikiuota, key=lambda x: x[0])
for marsrutas, siuntu_skaicius, svoris in isrikiuota:
  print(f"{marsrutas}\t{siuntu_skaicius}\t{svoris}")