import sys
predchozi_radek = None
for radek in sys.stdin:
    if predchozi_radek != radek:
        print(radek, end="")
    predchozi_radek = radek