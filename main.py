sisend = open("sisend.txt", "r")
rida = 0
teksti_ridu = -1
while 1:
    sisend_rida = sisend.readline() #sisend_rida on list. List tähtedest / märkidest, mis on ühel real.
    if not sisend_rida or rida >= teksti_ridu:
        break
    if rida == 0:
        teksti_ridu = int(sisend_rida)
    else:
        print(sisend_rida)
        reapikkus=len(sisend_rida)
        #nüüd teame kui pikk on rida, saame for tsükli teha.

        #teine võimalus on kasutada for taht in sisend_rida:
        #sellisel juhul korratakse tsüklit kuni on tähti reas


        #siin on teksti read 1-1000 tükki
        #rida võib pidada listiks ehk kui meil on reaks sisend_rida="Jõuluvanal puna nina", siis sisend_rida[0] on J täht jne
        #listi pikkuse saab nääiteks käsuga len rea_pikkus=len(sisend_rida)
        #TODO: tuleb rida realt ja täht tähelt kokku lugeda kõikide tähtede kogused.
        #TODO:for tsükkel 0-rea pikkus
        #todo:teha list, kus iga tähe järel on esinemis kordade number

    rida += 1

sisend.close() #faili sulgemine, et ei jääks mällu ripakile.

valjund = open("val.txt", "w")#siia faili tuleb tulemus trükkida

#TODO:vaja kirjutada histogramm väljundfaili etteandtud kujul.

valjund.close()#sulgeme selle faili ka ja siis on kõik tehtud

