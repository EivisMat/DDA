# map-1.py
import sys

# Kuriuos požymius ištrauksime iš duomenų bylos
to_extract = ['marsrutas=', 'siuntu skaicius=', 'svoris=']

for line in sys.stdin:
  try:
    # Split'iname eilutę, norint gauti kiekvieną individualų sustojimą
    # Pirmas splitas visada bus ['', {{...}}, ...]
    splitted = line.split("{{")[1:]

    # Tikriname visus sustojimus
    for i in splitted:
      extracted = []

      # Pereiname per ieškomus požymius
      for item in to_extract:
        # Jeigu split'inus ilgis daugiau negu 1, reiškia požymis yra
        if len(i.split(item)) > 1:
          # Tikriname ar paramentras ne tuščias
          if i.split(item)[1].split("}")[0] != "":
            extracted.append(i.split(item)[1].split("}")[0])
          else:
            extracted.append("-")
        else:
          # Jei nerasta maršruto, išspausdinti '-'
          if item == "marsrutas=":
            extracted.append('-')
          else:
            # Jei nerandame siuntu skaičiaus ar svorio, sakome kad jie yra 0
            extracted.append('0')
      print("\t".join(extracted))
  except:
    continue