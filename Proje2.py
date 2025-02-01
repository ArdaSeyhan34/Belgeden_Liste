

with open("../../../../AppData/Roaming/JetBrains/PyCharmCE2024.2/scratches/ornek_metin.txt", encoding="utf-8") as f:
    hepsi = f.readlines()
    isimlerListesi = []
    soyisimlerListesi = []
    bolumlerListesi=[]
    toplamnotlarListesi=[]
    ortalamaListesi = []
    gecmeDurumu = []

    for i in hepsi[1:]:
        tamisim = i.split(" ")[0]
        ayırma = tamisim.replace("-"," ")
        ayırma2 = ayırma.split(" ")
        soyisimlerListesi.append(ayırma2.pop())
        isimlerListesi.append(" ".join(ayırma2))


    for i in hepsi[1:]:
            bolumisim= i.split(" ")
            if bolumisim[2].startswith("M"):
                totalbolum = bolumisim[1] + " " +bolumisim[2]
                bolumlerListesi.append(totalbolum)
            else:
                bolumlerListesi.append(bolumisim[1])

    for i in hepsi[1:]:
        toplamnotlar = i.split(" ")[-1]
        toplamnotlarListesi.append(toplamnotlar)


    for i in toplamnotlarListesi:
        vize1 = i.split("/")[0]
        vize2 = i.split("/")[1]
        final = i.split("/")[2]
        ortalama0 = float(vize1) * 0.3 + float(vize2) * 0.3 + float(final) * 0.4
        ortalama = round(ortalama0,1)
        ortalamaListesi.append(ortalama)
        if ortalama >= 70 and float(final) >= 70:
            gecmeDurumu.append("Geçti")
        else:
            gecmeDurumu.append("Kaldı")

    print(f"{'Ad':<20}{'Soyad':<20}{'Bolum':<20}{'Ortalaması':<20}{'Durum':<20}")
    print("-" * 86 )

    for Ad, Soyad, Bolum, Ortalama, Durum in zip(isimlerListesi, soyisimlerListesi, bolumlerListesi, ortalamaListesi,gecmeDurumu):
        print(f"{Ad:<20}{Soyad:<20}{Bolum:<20}{Ortalama:<20}{Durum:<20}")













