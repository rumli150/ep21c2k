# 1.feladat//////////////////////////////////////////////////////////////////////////////
file = open("valaszok.txt", "r")
sor = file.readline()
valaszok = []
nevek = []
valaszok.append(sor)

while sor:
    valaszok.append(sor[6:])
    nevek.append(sor[:5])
    sor = file.readline()

valaszok.pop(1)
nevek.pop(0)
helyes = valaszok.pop(0)
file.close()

# for i in range(len(valaszok)):
#     print(nevek[i],end=" ")
#     print(valaszok[i],end="")

# print(helyes)
print("1. feladat: Az adatok beolvasása.")
# 2.feladat//////////////////////////////////////////////////////////////////////////////
print(f"2. feladat: A versenyen {len(nevek)} versenyző indult.")
# 3.feladat//////////////////////////////////////////////////////////////////////////////
azon = input("3. feladat: Kérem adja meg a versenyző azonosítóját: (2 betű 3 szám pl: AB123) ")
hiba = 0
negyes_vizsgalat = ""
for i in range(len(nevek)):
    if nevek[i] == azon:
        negyes_vizsgalat = valaszok[i]
        print(valaszok[i])
        hiba = 1

if hiba == 0:
    print("Ilyen kóddal nem indult versenyző.")
# 4.feladat//////////////////////////////////////////////////////////////////////////////
print("4. feladat: A helyes megoldás:")
print(helyes,end="")
if hiba == 0:
    negyes_vizsgalat = valaszok[0]

for char in range(len(negyes_vizsgalat)-1):
    if negyes_vizsgalat[char] == helyes[char]:
        print("+",end="")
    else:
        print(" ",end="")
# 5.feladat//////////////////////////////////////////////////////////////////////////////
print("\n")
sorszam = int(input("5. feladat: Kérem adja meg a feladat sorszámát: (1-től 14-ig) "))

while sorszam < 1 or sorszam > 14:
    sorszam = int(input("5. feladat: Kérem adja meg a feladat sorszámát: (1-től 14-ig) "))

helyes_sum = 0
for i in valaszok:
    if i[sorszam-1] == helyes[sorszam-1]:
        helyes_sum+=1
egy_szazalek = float(len(valaszok)/100)
szazalek = helyes_sum/egy_szazalek
szazalek = round(szazalek,2)
print(f"A feladatra {helyes_sum} fő, a versenyzők {szazalek}%-a adott helyes választ.")
# 6.feladat//////////////////////////////////////////////////////////////////////////////
print("6. feladat: A versenyzők pontszámának meghatározása.")
file = open("pontok.txt", "w")
pontok = []
for i in valaszok:
    pontok.append(0)
k = 0
for row in valaszok:
    j = 0
    for char in row:
        # print(char)
        if char == helyes[j]:
            if j < 5:
                pontok[k] += 3
            elif j > 4 and j < 10:
                pontok[k] += 4
            elif j > 9 and j < 13:
                pontok[k] += 5
            elif j == 13:
                pontok[k] += 6
        j+=1
    # print(row)
    k+=1
# print(pontok)


for i in range(len(nevek)):
    file.write(nevek[i])
    file.write(" ")
    file.write(str(pontok[i]))
    file.write("\n")


file.flush()
file.close()
# 7.feladat//////////////////////////////////////////////////////////////////////////////
print("7. feladat: A verseny legjobbjai:")
dij = 1
while dij <4:
    maxos = pontok.index(max(pontok))
    print(f"{dij}. díj ({max(pontok)} pont): {nevek[maxos]}")
    oh = pontok[maxos]
    pontok.pop(maxos)
    nevek.pop(maxos)
    if(max(pontok)!=oh):
        dij += 1