import json
telefoni=[]
videja_cena=[]
with open("uzd4.json",encoding="utf-8")

LMT=[{"modelis":"iPhone 15 Pro","cena":1199.00}]

Tet=[{"modelis":"iPhone 15 Pro","cena":1075.00}]

Euronics=[{"modelis":"iPhone 15 Pro","cena":1075.00}]



LMT1=[{"modelis":"Galaxy S24 Ultra","cena":1419.00}]

Tet1=[{"modelis":"Galaxy S24 Ultra","cena":1419.00}]

Euronics1=[{"modelis":"Galaxy S24 Ultra","cena":1459.00}]



LMT2=[{"modelis":"Pixel 8 Pro","cena":1050.00}]

Tet2=[{"modelis":"Pixel 8 Pro","cena":1075.00}]

Euronics2=[{"modelis":"Pixel 8 Pro","cena":1099.00}]



LMT3=[{"modelis":"Xiaomi 14 Ultra","cena":1449.00}]

Tet3=[{"modelis":"Xiaomi 14 Ultra","cena":1460.00}]

Euronics3=[{"modelis":"Xiaomi 14 Ultra","cena":1499.00}]



LMT4=[{"modelis":"Xperia 1 V","cena":1250.00}]

Tet4=[{"modelis":"Xperia 1 V","cena":1250.00}]

Euronics4=[{"modelis":"Xperia 1 V","cena":1299.00}]



LMT5=[{"modelis":"OnePlus 12","cena":929.00}]

Tet5=[{"modelis":"OnePlus 12","cena":945.00}]

Euronics5=[{"modelis":"OnePlus 12","cena":969.00}]



LMT6=[{"modelis":"Nokia G42","cena":229.00}]

Tet6=[{"modelis":"Nokia G42","cena":235.00}]

Euronics6=[{"modelis":"Nokia G42","cena":249.00}]


trīskompānijas= LMT+Tet+Euronics
videja_cena=sum(x["cena"] for x in trīskompānijas)

trīskompānijas= LMT1+Tet1+Euronics1
videja_cena=sum(x["cena"] for x in trīskompānijas)

trīskompānijas= LMT2+Tet2+Euronics2
videja_cena=sum(x["cena"] for x in trīskompānijas)

trīskompānijas= LMT3+Tet3+Euronics3
videja_cena=sum(x["cena"] for x in trīskompānijas)

trīskompānijas= LMT4+Tet4+Euronics4
videja_cena=sum(x["cena"] for x in trīskompānijas)

trīskompānijas= LMT5+Tet5+Euronics5
videja_cena=sum(x["cena"] for x in trīskompānijas)

trīskompānijas= LMT6+Tet6+Euronics6
videja_cena=sum(x["cena"] for x in trīskompānijas)
