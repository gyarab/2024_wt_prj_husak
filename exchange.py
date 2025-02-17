import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
r = httpx.get(url)

def check_convert_input(input):
   return input in meny

def check_num_input(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

lines = r.text.strip().split("\n")

rows = []
for line in lines:
    rows.append(line.split("|"))

rows = rows[2:]

meny = {}
for row in rows:
    meny[row[3]] = float(str(row[4]).replace(',', '.')) / float(row[2])

meny['CZK'] = 1

convert_to = input("Zadejte, DO ktere meny checete konvertovat: ")
while not check_convert_input(convert_to):
    convert_to = input("Prosim, zadejte platni vstup: ")
        
convert_from = input("Zadejte, ZE ktere meny checete konvertovat: ")
while not check_convert_input(convert_from):
    convert_from = input("Prosim, zadejte platni vstup: ")
        
castka = input("Zadejte castku: ")
while not check_num_input(castka):
    castka = input("Prosim, zadejte platni vstup: ")

castka = float(castka)


vysledek = round(meny[convert_from] * castka / meny[convert_to], 2)


print(f"Vysledek převodu {castka} {convert_from} -> {convert_to} je {vysledek} {convert_to}")




