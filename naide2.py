sisend = open("sisend.txt", "r")
rida = 0
teksti_ridu = -1
histogram_tahed = [] #tähtede nimekiri
histogram_kodused = [] #tähtede kogused
tahtede_loendur = 0 #mitu erinevat tähte on leitud?
leidsin_tahe=0

sisend_rida = sisend.readline() #sisend_rida on list. List tähtedest / märkidest, mis on ühel real.
teksti_ridu = int(sisend_rida)

for r in range(0, teksti_ridu):
    sisend_rida = sisend.readline() #järgmine rida failist
    reapikkus = len(sisend_rida) #tähtede kogus mida läbivaatame
    for taht in range(0, reapikkus): #vaatame tähed ükshaavaal
        leidsin_tahe=0
        for asukoht in range(0, len(histogram_tahed)): #tsülkkel, kus vaatame läbi siiani leitud tähed ja trükima ainult siis, kui leiame uue.
            if histogram_tahed[asukoht] == sisend_rida[taht]: # kui täht on leitud, siis loeme ta ära.
                histogram_kodused[asukoht] += 1 # kui täht on juba histogrammis, siis loeme ta ära
                leidsin_tahe=1 # täht leitud histogrammist
        if leidsin_tahe==0: #kui tähte ei leidnud histogrammist, siis lisame ta sinna.
             histogram_tahed.append(sisend_rida[taht])#histogrammi tähtedele üks täht juurde
             histogram_kodused.append(1) #loendur ka üks juurde.
sisend.close() #faili sulgemine, et ei jääks mällu ripakile.

valjund = open("val.txt", "w")#siia faili tuleb tulemus trükkida

        #TODO:vaja kirjutada histogramm väljundfaili etteandtud kujul.

valjund.close()#sulgeme selle faili ka ja siis on kõik tehtud



