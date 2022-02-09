sisend = open("sisend.txt", "r")
print(sisend)
rida = 0 # muutuja rida, int, pole kasutatud.
teksti_ridu = -1 #int, failise loetud ridade arv
histogram_tahed = [] #  tahtede nimekiri
histogram_kodused = [] #  tahtede koguse
tahtede_loendur = 0 #mitu erinevat tahte on leitud?
leidsin_tahe = 0

sisend_rida = sisend.readline() #sisend_rida on list. List tahtedest / markidest, mis on uhel real.
teksti_ridu = int(sisend_rida)

for r in range(0, teksti_ridu):
    sisend_rida = sisend.readline() #jargmine rida failist
    reapikkus = len(sisend_rida) #tahtede kogus mida labivaatame, Kas seda reapikkust vaja on?
    for taht in range(0, reapikkus): #vaatame tahed ukshaavaal
        leidsin_tahe = 0
        for asukoht in range(0, len(histogram_tahed)): #tsulkkel, kus vaatame labi siiani leitud tahed ja trukima ainult siis, kui leiame uue.
            if histogram_tahed[asukoht] == sisend_rida[taht]: # kui taht on leitud, siis loeme ta ara.
                histogram_kodused[asukoht] += 1 # kui taht on juba histogrammis, siis loeme ta ara
                leidsin_tahe = 1 # taht leitud histogrammist
        if leidsin_tahe == 0 and not sisend_rida[taht].isspace(): #kui tahte ei leidnud histogrammist, siis lisame ta sinna.
             histogram_tahed.append(sisend_rida[taht])#histogrammi tahtedele uks taht juurde
             histogram_kodused.append(1) #loendur ka uks juurde.
sisend.close() #faili sulgemine, et ei jaaks mallu ripakile.


valjund = open("val.txt", "w")#siia faili tuleb tulemus trukkida

valjund.write("Tere maailm"+"Ilus ilm"+"\r")


rida = 0
for ch in histogram_tahed:#kuniks listis tähti
    valjund.write(ch+" "+str(histogram_kodused[rida])+"\r") #kirjutame faili nimekirja, igale reale täht ja tema kogus.
    rida += 1 #anname teada, et järmine rida.

#TODO:vaja kirjutada histogramm valjundfaili etteandtud kujul.

valjund.close()#sulgeme selle faili ka ja siis on koik tehtud











#muutujate nimekiri
#sisend *tyyp on IOwrapper, mis sisaldab andmeid faili kohta "sisend.txt"
#rida *int, väljundi kirjutamisel loeb ridu, et koguses saaksid õigele reale.
#teksti_ridu *int, sisendfaili esimeselt realt loetud ridade arv.
#histogram_tahed *list, kuhu lisatakse tähed, mis on omakorda str vormaadis
#histogram_kodused *list, kuhu liidetakse tähe leidmisel kogused int vormaadis
#tahtede_loendur *int tähti reas.
#r *int teksti rea number failis
#leidsin_tahe *int, kui on 1 siis leiti uus täht, kui 0, siis ei leitud. kontrollitakse real 22
#sisend_rida * str, terve rida failist.
#reapikkus * int rea pikkus failist.
#asukoht * int, for tsüklis asukoht real. (pole vaja kasutada isegi.)
#ch *str täht listist histogram tähed.
#valjund * tyyp on IOwrapper, mis sisaldab andmeid faili kohta "val.txt"