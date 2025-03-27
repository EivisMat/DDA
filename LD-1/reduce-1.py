# reduce-1.py
import sys

dabartinis_marsrutas = ""

for line in sys.stdin:
  try:
    marsrutas, siuntu_skaicius, svoris = line.split("\t")

    if dabartinis_marsrutas == "":
      dabartinis_marsrutas = marsrutas
      siuntu_skaicius_b = 0
      svoris_b = 0

    # Paverčiame į skaičius norint juos sudėti
    siuntu_skaicius = int(siuntu_skaicius) if siuntu_skaicius != "-" else 0
    svoris = float(svoris[:-1]) if svoris[:-1] != "-" else 0
    # svoris[:-1] nes nenorime pagauti \n

    if marsrutas == dabartinis_marsrutas:
      siuntu_skaicius_b += siuntu_skaicius
      svoris_b += svoris
    else:
      print(f"{dabartinis_marsrutas}\t{siuntu_skaicius_b}\t{svoris_b}")
      dabartinis_marsrutas = ""
  except:
    continue