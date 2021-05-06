import sys
predchozi_radek = None
pocitadlo = 0
for radek in sys.stdin:
    if predchozi_radek in (None, radek):
        pocitadlo += 1 
    else:
        print(f"{str(pocitadlo).rjust(3)} {predchozi_radek}", end="")
        pocitadlo = 1
    predchozi_radek = radek

print(f"{str(pocitadlo).rjust(3)} {predchozi_radek}", end="")