# reduce-2.py
import sys

dabartinis_marsrutas = ""

for line in sys.stdin:
  try:
    marsrutas, siuntu_skaicius, svoris, zona = line.split("\t")

    if dabartinis_marsrutas == "":
      dabartinis_marsrutas = marsrutas
      siuntu_skaicius_b = 0
      svoris_b = 0
      zonos = {}

    # Paverčiame į skaičius norint juos sudėti
    siuntu_skaicius = int(siuntu_skaicius) if siuntu_skaicius != "-" else 0
    svoris = float(svoris) if svoris != "-" else 0
    zona = zona[:-1]
    # zona[:-1] nes nenorime pagauti \n

    if marsrutas == dabartinis_marsrutas:
      siuntu_skaicius_b += siuntu_skaicius
      svoris_b += svoris
      if zona not in zonos.keys():
        zonos[zona] = 0
      zonos[zona] += 1
    else:
      print(f"{dabartinis_marsrutas}\t{siuntu_skaicius_b}\t{svoris_b}\t{zonos}")
      dabartinis_marsrutas = ""
  except:
    continue