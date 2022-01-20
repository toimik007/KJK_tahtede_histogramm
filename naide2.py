sisend = open("sisend.txt", "r")
rida = 0
teksti_ridu = -1
histogram_tahed = [] #tähtede nimekiri
histogram_kodused = [] #tähtede kogused
tahtede_loendur = 0 #mitu erinevat tähte on leitud?

sisend_rida = sisend.readline() #sisend_rida on list. List tähtedest / märkidest, mis on ühel real.
teksti_ridu = int(sisend_rida)

for r in range(0, teksti_ridu):
    sisend_rida = sisend.readline() #järgmine rida failist
    reapikkus = len(sisend_rida) #tähtede kogus mida läbivaatame
    for taht in range(0, reapikkus): #vaatame tähed ükshaavaal
        print(sisend_rida[taht])
        for asukoht in range(0, len(histogram_tahed)):
            if histogram_tahed[asukoht] == sisend_rida[taht]:
                histogram_tahed[tahtede_loendur] = sisend_rida[taht]
                histogram_kodused[tahtede_loendur]+histogram_kodused[tahtede_loendur] + 1
