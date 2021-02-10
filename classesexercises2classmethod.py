class calisan:
    zam_orani = 1.05
    per_say = 0
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+'@sirket.com'
        calisan.per_say = calisan.per_say + 1
    def tamad(self):
        return 'adi: {}  soyadi: {}'.format(self.ad, self.soyad)

    def arttir(self):
        self.maas = (self.maas * self.zam_orani)

    @classmethod
    def zam_orani_degis(cls, yeni_oran):
        cls.zam_orani = yeni_oran

    @classmethod  # Bu sinif metodu yeni bir nesne olusturmus oldu. 
    def ypersonel(cls, pbilgisi):
        ad, soyad, maas = pbilgisi.split('-')
        return  cls(ad, soyad, maas)

    @staticmethod
    def tel_no(telefon):
        return telefon.split(' ')

personel1 = calisan('Ali','Demir',2500)
personel2 = calisan('Alperen','Yigit',3200)


mpersonel1 = 'jan-Dondures-4000'
mpersonel2 = 'perez-vandame-3200'
ad, soyad, maas = mpersonel1.split('-')

#ypersonel1 = calisan(ad, soyad, maas)
ypersonel1 = calisan.ypersonel(mpersonel1)
print(ypersonel1.eposta)

gtelefon = '0123 456 78 90'
print(calisan.tel_no(gtelefon))
# calisan.zam_orani_degis(1.5)
# print('personel1 maasi: ',personel1.maas)
# personel1.arttir()
# print('personel1 maas zamli hali: ', personel1.maas)
# print('personel2 maasi: ', personel2.maas)
# personel2.arttir()
# print('personel2 zamli maasi: ',personel2.maas)