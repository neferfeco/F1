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

versenyzok = []

for sor in verseny_adatok:
    adatok = []
    if (sor[2],sor[1]) not in versenyzok.:
        adatok.append(sor[2])
        adatok.append(sor[1])
    else:
        pass    
        
    versenyzok.append(adatok)

print(versenyzok)

