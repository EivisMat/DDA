# reduce-3.py
import sys

dabartine_zona = ""
dabartine_diena = 0

for line in sys.stdin:
  try:
    zona, diena, klientai, siuntu_skaicius = line.split("\t")

    klientai = int(klientai) if klientai != "-" else 0
    siuntu_skaicius = int(siuntu_skaicius) if siuntu_skaicius != "-" else 0

    if dabartine_zona == "":
      dabartine_zona = zona
      dabartine_diena = diena
      klientai_b = 0
      siuntos_b = 0

    if zona == dabartine_zona:
      if diena == dabartine_diena:
        klientai_b += klientai
        siuntos_b += siuntu_skaicius
      else:
        print(f"{dabartine_zona}\t{dabartine_diena}\t{klientai_b}\t{siuntos_b}")
        dabartine_diena = diena
        klientai_b = 0
        siuntos_b = 0
    else:
      print(f"{dabartine_zona}\t{dabartine_diena}\t{klientai_b}\t{siuntos_b}")
      dabartine_zona = ""
  except:
    continue