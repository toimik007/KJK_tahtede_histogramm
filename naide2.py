sisend = open("sisend.txt", "r")
rida = 0
teksti_ridu = -1
histogram_tahed = [] #tahtede nimekiri
histogram_kodused = [] #tahtede kogused
tahtede_loendur = 0 #mitu erinevat tahte on leitud?
leidsin_tahe = 0

sisend_rida = sisend.readline() #sisend_rida on list. List tahtedest / markidest, mis on uhel real.
teksti_ridu = int(sisend_rida)

for r in range(0, teksti_ridu):
    sisend_rida = sisend.readline() #jargmine rida failist
    reapikkus = len(sisend_rida) #tahtede kogus mida labivaatame
    for taht in range(0, reapikkus): #vaatame tahed ukshaavaal
        print(taht)
        leidsin_tahe = 0
        for asukoht in range(0, len(histogram_tahed)): #tsulkkel, kus vaatame labi siiani leitud tahed ja trukima ainult siis, kui leiame uue.
            if histogram_tahed[asukoht] == sisend_rida[taht]: # kui taht on leitud, siis loeme ta ara.
                histogram_kodused[asukoht] += 1 # kui taht on juba histogrammis, siis loeme ta ara
                leidsin_tahe = 1 # taht leitud histogrammist
        if leidsin_tahe == 0 and not sisend_rida[taht].isspace(): #kui tahte ei leidnud histogrammist, siis lisame ta sinna.
             histogram_tahed.append(sisend_rida[taht])#histogrammi tahtedele uks taht juurde
             histogram_kodused.append(1) #loendur ka uks juurde.
sisend.close() #faili sulgemine, et ei jaaks mallu ripakile.

#print(*histogram_tahed,sep=', ')

valjund = open("val.txt", "w")#siia faili tuleb tulemus trukkida
valjund.write("Tere maailm"+"Ilus ilm"+"\r")













#TODO:vaja kirjutada histogramm valjundfaili etteandtud kujul.

valjund.close()#sulgeme selle faili ka ja siis on koik tehtud



