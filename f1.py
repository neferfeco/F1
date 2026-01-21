verseny_adatok = []

try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        fajl.readline()
        
        for sor in fajl:
            sornyi_adat = sor.strip().split(",")
            
            sornyi_adat[0] = int(sornyi_adat[0])
            sornyi_adat[1] = int(sornyi_adat[1])
            
            verseny_adatok.append(sornyi_adat)       
        
except IOError as ex:
    print(f"IO hiba: {ex}")

#print(verseny_adatok)

versenyzo_adatok = []

elso = [verseny_adatok[0][2], verseny_adatok[0][1]]
versenyzo_adatok.append(elso)

for i in range(1, len(verseny_adatok)):
    j = 0
    while j < len(versenyzo_adatok) and versenyzo_adatok[j][0] != verseny_adatok[i][2]:
        j += 1

    if j >= len(versenyzo_adatok):
        uj = [verseny_adatok[i][2], verseny_adatok[i][1]]
        versenyzo_adatok.append(uj)
    else:
        if versenyzo_adatok[j][1] > verseny_adatok[i][1]:
            versenyzo_adatok[j][1] = verseny_adatok[i][1]

#print(versenyzo_adatok)

i = 0
while i < len(versenyzo_adatok) and versenyzo_adatok[i][1] == 1:
    i +=1

if i >= len(versenyzo_adatok):
    print(f"Minden versenyzo volt elso helyezett!")
else:
    print(f"Nem minden versenyzo volt elso helyezett! Pl.: {versenyzo_adatok[i][0]}")



