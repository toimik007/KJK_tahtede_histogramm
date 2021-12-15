sisend = open("sisend.txt", "r")
rida = 0
teksti_ridu = -1
while 1:

    sisend_rida = sisend.readline()
    if rida == 0:
        teksti_ridu = int(sisend_rida)
    else:
        print(sisend_rida)
    if not sisend_rida or rida >= teksti_ridu:
        break
    rida += 1

sisend.close()

valjund = open("val.txt", "w")

