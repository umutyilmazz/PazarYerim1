import time
from urun_stok import urunStok
# Class
class UrunMenusu:
    def __init__(self):
        self.urunStok = urunStok

    def urun_ekle(self, ad):
        print("--Ürün Kayıt Etme--\n")
        urun_adi_listesi = [urun["urun_adi"] for urun in self.urunStok]
        
        if ad in urun_adi_listesi:
            print(f"{ad} Adında Bir Ürün Zaten Mevcut!")
        else:
            fiyat = float(input("Ürün Fiyatını Giriniz: "))
            while True:
                stok = int(input("Ürünün Stok Miktarı: "))
                if not type(stok) == int:
                    print("Stok Miktarı Tam Sayı Olmak Zorundadır!\n")
                else:
                    break
            sinif = input("Ürünün Sınıfı: ")
            yeni_urun = {
                "urun_adi": ad,
                "urun_fiyati": fiyat,
                "stok_miktari": stok,
                "sinif": sinif
            }
            self.urunStok.append(yeni_urun)
            print(f"{ad} Başarıyla Eklendi.\n")

            
    def urun_duzenleme(self,ad):
        print("--Ürün Düzenleme--\n")
        urun_adi_listesi = [urun["urun_adi"] for urun in self.urunStok]
        
        if not ad in urun_adi_listesi:
            print(f"{ad} Adında Bir Ürün Bulunamadı!\n")
        else:
            adYeni = input("Ürünün Yeni Adını Giriniz: ")
            while True:
                fiyat = int(input("Ürünün Yeni Fiyat Miktarı: "))
                if not type(fiyat) == int:
                    print("Fiyat Tam Sayı Olmak Zorundadır!\n")
                else:
                    break
            while True:
                stok = int(input("Ürünün Yeni Stok Miktarı: "))
                if not type(stok) == int:
                    print("Stok Miktarı Tam Sayı Olmak Zorundadır!\n")
                else:
                    break
            sinif = input("Ürünün Yeni Sınıfı: ")
            for urun in self.urunStok:
                if urun["urun_adi"] == ad:
                    urun["urun_adi"] = adYeni
                    urun["urun_fiyati"] = fiyat
                    urun["stok_miktari"] = stok
                    urun["sinif"] = sinif
                    print(f"{ad} Adlı Ürün Düzenlendi!\n")

    def urun_sil(self, urun_adi):
        print("--Ürün Silme--\n")
        for urun in self.urunStok:
            if urun['urun_adi'] == urun_adi:
                    self.urunStok.remove(urun)
                    print(f"{urun_adi} başarıyla silindi.\n")
                    return
        if not any(urun['urun_adi'] == urun_adi for urun in self.urunStok):
            print(f"{urun_adi} İsminde Bir Ürün Bulunamadı!\n")
            
    def stok_duzenleme(self,urun_adi):
        print("--Ürün Stok Düzenleme--\n")
        for urun in self.urunStok:
            if urun['urun_adi'] == urun_adi:
                while True:
                    yeni_stok = int(input("Ürünün Yeni Stok Miktarı: "))
                    if not type(yeni_stok) == int:
                        print("Stok Miktarı Tam Sayı Olmak Zorundadır!\n")
                    else:
                        break
                urun['stok_miktari'] = yeni_stok
                print(f"Yeni Stok Miktarı: {yeni_stok}\n")
                return
        if not any(urun['urun_adi'] == urun_adi for urun in self.urunStok):
            print(f"{urun_adi} İsminde Bir Ürün Bulunamadı!\n")

    def urunleri_listele(self):
        print("--Ürün Listele--\n")
        if not self.urunStok:
            print("Stokta Ürün Bulunmamaktadır.\n")
        else:
            print("Stoktaki Ürünler:\n")
            for i, urun in enumerate(self.urunStok, start=1):
                print(f"Ürün {i}:")
                print(f"Adı: {urun['urun_adi']}")
                print(f"Fiyatı: {urun['urun_fiyati']}")
                print(f"Stok Miktarı: {urun['stok_miktari']}")
                print(f"Sınıfı: {urun['sinif']}")
                print()
                time.sleep(1)

class SiparisMenu(UrunMenusu):
    def __init__(self):
        self.siparisler = [{
            "siparis_numarasi" : "1",
            "icerik" : ["Güneş Kremi","Versace Dylan Blue"],
            "adet" : [1,1],
            "fiyat" : 1900,
            "durum" : "Hazırlanıyor..."
        }]
        self.bekleyenIslem = [{
            "siparis_numarasi" : "2",
            "icerik" : ["Güneş Kremi"],
            "adet" : [1],
            "fiyat" : 400,
            "durum" : "Onay Bekliyor..."
        }]
        self.iadeBekleyen = [{
            "siparis_numarasi" : "3",
            "icerik" : ["Versace Dylan Blue"],
            "adet" : [1],
            "fiyat" : 1500,
            "durum" : "İade İşlemi Başlatıldı!"
        }]
        self.iadeIslem = [{
            "siparis_numarasi" : "4",
            "icerik" : ["Versace Dylan Blue"],
            "adet" : [2],
            "fiyat" : 3000,
            "durum" : "İade Onaylandı."
        }]
        UrunMenusu.__init__(self)
        

    def siparis_durum_degisiklik(self):
        print("--Sipariş Durum Değişikliği--\n")
        print("Onaylanan Siparişler:\n")
        for i, numara in enumerate(self.siparisler, start=1):
                print(f"Sipariş {i}:")
                print(f"Sipariş Numarası: {numara['siparis_numarasi']}")
                print(f"İçerik: {numara['icerik']}")
                print(f"Adet: {numara['adet']}")
                print(f"Fiyat: {numara['fiyat']}")
                print(f"Durum: {numara['durum']}")
                print()
                time.sleep(1)
        numara = input("Değişiklik Yapılacak Sipariş Numarası: ")
        for siparis in self.siparisler:
            if siparis["siparis_numarasi"] == numara:
                    yeni_durum = input("Yeni Sipariş Durumu (1-Onaylandı 2-Hazırlanıyor 3-Kargoya Verildi 4-Teslim Edildi 5-İade İşlemi Başlatıldı) : ")
                    if yeni_durum == "1":
                        siparis["durum"] = "Onaylandı..."
                    elif yeni_durum == "2":
                        siparis["durum"] = "Hazırlanıyor..."
                    elif yeni_durum == "3":
                        siparis["durum"] = "Kargoya Verildi..."
                    elif yeni_durum == "4":
                        siparis["durum"] = "Teslim Edildi."
                    elif yeni_durum == "5":
                        siparis["durum"] = "İade İşlemi Başlatıldı!"
                        self.siparisler.remove(siparis)
                        self.iadeBekleyen.append(siparis)
                    else: 
                        print("Hatalı İşlem Girişi Yaptınız!\n")

                    print(f"{numara} Numaralı Siparişin Yeni Durumu: {siparis['durum']}\n")
                    break
        if not any(siparis['siparis_numarasi'] == numara for siparis in self.siparisler or self.iadeBekleyen):
            print(f"{numara} Numaralı Bir Sipariş Bulunamadı!\n")
    
    def siparis_listele(self):
        print("--Sipariş Listele--\n")
        if not self.siparisler and not self.bekleyenIslem:
            print("Sipariş Bulunmamaktadır.\n")
        else:
            print("Onaylanan Siparişler:\n")
            for i, numara in enumerate(self.siparisler, start=1):
                print(f"Sipariş {i}:")
                print(f"Sipariş Numarası: {numara['siparis_numarasi']}")
                print(f"İçerik: {numara['icerik']}")
                print(f"Adet: {numara['adet']}")
                print(f"Fiyat: {numara['fiyat']}")
                print(f"Durum: {numara['durum']}")
                print()
                time.sleep(1)
            print()
            print("Onay Bekleyen Siparişler:\n")
            for i, numara in enumerate(self.bekleyenIslem, start=1):
                print(f"Sipariş {i}:")
                print(f"Sipariş Numarası: {numara['siparis_numarasi']}")
                print(f"İçerik: {numara['icerik']}")
                print(f"Adet: {numara['adet']}")
                print(f"Fiyat: {numara['fiyat']}")
                print(f"Durum: {numara['durum']}")
                print()
                time.sleep(1)
    
    def siparis_onaylama(self):
        self.urunStok = UrunMenusu().urunStok
        print("--Sipariş Onaylama--\n")
        if len(self.bekleyenIslem) == 0:
            print("Onaylanması Gereken İşlem Bulunmamaktadır!\n")
        elif len(self.bekleyenIslem) == 1:
            for numara in self.bekleyenIslem:
                no = numara["siparis_numarasi"]
                icerik = numara["icerik"]
                fiyat = numara["fiyat"]
                adet = numara["adet"]
                print(f"Sipariş Bilgileri:\nSipariş Numarası : {no}\nİçerik: {icerik}\nAdet: {adet}\nFiyat: {fiyat}\n")
                onay = input("Onaylamak İçin 'onay' Yazınız: ")
                if onay == "ONAY" or onay == "onay":
                        numara["durum"] = "Onaylandı..."
                        print("Sipariş Onaylandı!\n")
                        self.bekleyenIslem.remove(numara)
                        self.siparisler.append(numara)
                        break
                else:
                        print("Sipariş Onaylanmadı!\n")
        else:
            print("Onay Bekleyen Siparişler:\n")
            for i, numara in enumerate(self.bekleyenIslem, start=1):
                print(f"Bekleyen Sipariş {i}:\n")
                print(f"Sipariş Numarası: {numara['siparis_numarasi']}")
                print(f"İçerik: {numara['icerik']}")
                print(f"Adet: {numara['adet']}")
                print(f"Fiyat: {numara['fiyat']}")
                print(f"Durum: {numara['durum']}")
                print()
                time.sleep(1)
            while True:
                onay_bekleyen_siparis_listesi = [siparis["siparis_numarasi"] for siparis in self.bekleyenIslem]
                if len(onay_bekleyen_siparis_listesi) == 0:
                    print("Onay Bekleyen Sipariş Kalmadı!\n")
                    break
                siparisNo = input("Onaylamak İstediğiniz Sipariş Numarasını Giriniz(Çıkış İçin Q): ")
                if siparisNo in onay_bekleyen_siparis_listesi:
                    for numara in self.bekleyenIslem:
                        if numara["siparis_numarasi"] == siparisNo:
                            onay = input("Onaylamak İçin 'onay' Yazınız: ")
                            if onay == "ONAY" or onay == "onay":
                                    numara["durum"] = "Onaylandı..."
                                    print("Sipariş Onaylandı!\n")
                                    self.bekleyenIslem.remove(numara)
                                    self.siparisler.append(numara)
                                    break
                            else:
                                    print("Sipariş Onaylanmadı!\n")
                elif siparisNo == "Q" or siparisNo == "q":
                    print("Başarıyla Çıkış Yapıldı!\n")
                    break
                else:
                    print("Sipariş Numarası Bulunamadı!\n")
    
    def iade_islem(self):
        print("--İade İşlemleri--\n")
        if len(self.iadeBekleyen) == 0:
            print("İadesi Kabul Edilecek Sipariş Bulunamadı!\n")
        elif len(self.iadeBekleyen) == 1:
            for numara in self.iadeBekleyen:
                no = numara["siparis_numarasi"]
                icerik = numara["icerik"]
                fiyat = numara["fiyat"]
                adet = numara["adet"]
                print(f"Sipariş Bilgileri:\nSipariş Numarası : {no}\nİçerik: {icerik}\nAdet: {adet}\nFiyat: {fiyat}\n")
                while True:
                    iade = input("Ürün İade Koşullarını Karşılıyor Mu? (evet-(e)/hayır-(h)): ")
                    if iade == "e" or iade == "E":
                            numara["durum"] = "İade Onaylandı."
                            durum = numara["durum"]
                            print(f"Sipariş Durumu Değiştirildi:\n{no} Numaralı Siparişin Yeni Durumu: {durum}\n")
                            self.iadeBekleyen.remove(numara)
                            self.iadeIslem.append(numara)
                            break
                    elif iade == "h" or iade == "H":
                            numara["durum"] = "İade Koşulları Sağlanmadığı İçin Müşteriye Geri Gönderildi."
                            durum = numara["durum"]
                            print(f"Sipariş Durumu Değiştirildi:\n{no} Numaralı Siparişin Yeni Durumu: {durum}\n")
                            self.iadeBekleyen.remove(numara)
                            self.iadeIslem.append(numara)
                            break
                    else:
                        print("Hatalı Giriş Yaptınız!")
        else:
            print("Onay Bekleyen İadeler:\n")
            for i, numara in enumerate(self.iadeBekleyen, start=1):
                print(f"İade Onay Bekleyen Sipariş {i}:\n")
                print(f"Sipariş Numarası: {numara['siparis_numarasi']}")
                print(f"İçerik: {numara['icerik']}")
                print(f"Adet: {numara['adet']}")
                print(f"Fiyat: {numara['fiyat']}")
                print(f"Durum: {numara['durum']}")
                print()
                time.sleep(1)
            while True:
                onay_bekleyen_iade_listesi = [iade["siparis_numarasi"] for iade in self.iadeBekleyen]
                no = numara["siparis_numarasi"]
                siparisNo = input("Onaylamak İstediğiniz İade İşleminin Sipariş Numarasını Giriniz(Çıkış İçin Q): ")
                if siparisNo in onay_bekleyen_iade_listesi:
                    for numara in self.iadeBekleyen:
                        if numara["siparis_numarasi"] == siparisNo:
                            while True:
                                iade = input("Ürün İade Koşullarını Karşılıyor Mu? (evet-(e)/hayır-(h)): ")
                                if iade == "e" or iade == "E":
                                        numara["durum"] = "İade Onaylandı."
                                        durum = numara["durum"]
                                        print(f"Sipariş Durumu Değiştirildi:\n{no} Numaralı Siparişin Yeni Durumu: {durum}\n")
                                        self.iadeBekleyen.remove(numara)
                                        self.iadeIslem.append(numara)
                                        break
                                elif iade == "h" or iade == "H":
                                        numara["durum"] = "İade Koşulları Sağlanmadığı İçin Müşteriye Geri Gönderildi."
                                        durum = numara["durum"]
                                        print(f"Sipariş Durumu Değiştirildi:\n{no} Numaralı Siparişin Yeni Durumu: {durum}\n")
                                        self.iadeBekleyen.remove(numara)
                                        self.iadeIslem.append(numara)
                                        break
                                else:
                                    print("Hatalı Giriş Yaptınız!")

                elif siparisNo == "Q" or siparisNo == "q":
                    print("Başarıyla Çıkış Yapıldı!\n")
                    break
                else:
                    print("Hatalı İşlem Girişi!\n")
        
    def iade_listele(self):
        print("--İadeleri Listele--\n")
        if not self.iadeIslem:
            print("İade Edilen Sipariş Bulunmamaktadır.\n")
        else:
            print("İade Siparişler:\n")
            for i, numara in enumerate(self.iadeIslem, start=1):
                print(f"İade Sipariş {i}:")
                print(f"İçerik: {numara['icerik']}")
                print(f"Adet: {numara['adet']}")
                print(f"Fiyat: {numara['fiyat']}")
                print(f"Durum: {numara['durum']}")
                print()
                time.sleep(1)

    def siparis_olustur(self):
        print("--Sipariş Oluştur--\n")
        print("---Ürünler---")
        for i,urun in enumerate(self.urunStok,start = 1):
            print(f"{i}. Ürün")
            print(urun["urun_adi"])
            time.sleep(1)
        cesitSayi = int(len(self.urunStok))
        urunCesit = int(input(f"Ürün Çeşit Sayısı (max {cesitSayi}): "))
        toplam = 0
        i = 0
        icerikListe = []
        adetListe = []
        while i < urunCesit:
                urunAd = int(input(f"Sipariş Edilecek Ürün (1-{cesitSayi}) : "))
                urunStoktakiAd = self.urunStok[urunAd-1]["urun_adi"]
                urunStokMiktar = self.urunStok[urunAd-1]["stok_miktari"]
                icerikListe.append(urunStoktakiAd)
                if not type(urunAd) == int :
                    print("Hatalı Giriş Yaptınız!\n")
                else:
                    while True:
                        urunAdet = int(input("Seçilen Ürünün Adeti: "))
                        if urunAdet <= urunStokMiktar:
                            if not type(urunAdet) == int:
                                print("Hatalı Giriş Yaptınız!\n")
                            else:
                                adetListe.append(urunAdet)
                                self.urunStok[urunAd-1]["stok_miktari"] = urunStokMiktar - urunAdet
                                urunFiyat = self.urunStok[urunAd-1]["urun_fiyati"]
                                toplam += (urunFiyat * urunAdet)
                                break
                        else: 
                            print(f"Ürünün Stok Miktarı İstenenden Düşük!\n{urunStoktakiAd} Ürününün Stok Miktarı: {urunStokMiktar}")
                i += 1

        if not len(icerikListe) == 0 and not len(adetListe) == 0:
            bekleyenNo = self.bekleyenIslem[-1]["siparis_numarasi"]
            siparislerNo = self.siparisler[-1]["siparis_numarasi"]
            iadeBekleyenNo = self.iadeBekleyen[-1]["siparis_numarasi"]
            iadeIslemNo = self.iadeIslem[-1]["siparis_numarasi"]
            noListe = [bekleyenNo,siparislerNo,iadeBekleyenNo,iadeIslemNo]
            siparisNo = int(max(noListe)) + 1
            siparis = {
                "siparis_numarasi" : str(siparisNo),
                "icerik" : icerikListe,
                "adet" : adetListe,
                "fiyat" : toplam,
                "durum" : "Onay Bekliyor..."
            }
            self.bekleyenIslem.append(siparis)
            print("Sipariş Başarıyla OLuşturuldu!\nDurum: Onay Bekliyor...\n")
        else:
            print("Sipariş Oluşturulamadı!\n")

urunMenusu = UrunMenusu()
siparisMenusu = SiparisMenu()

# Menü
print("PazarYerim'e HoşGeldiniz!".center(50,"-"))
while True:
    print("---Ana Menü---\n1-Ürün Yönetimi\n2-Sipariş Yönetimi\n3-Çıkış Yap\n")
    islem1 = input("Yapacağınız İşlem'in Numarasını Seçiniz (1-3): ")
    print()
    if islem1 == "1":
        while True:
            print("--İşlem Menüsü--\n1-Ürün Kayıt Etme\n2-Ürün Düzenleme\n3-Ürün Silme\n4-Stok Düzenleme\n5-Ürün/Stok Bilgisi Görüntüleme\n6-Çıkış Yap\n")
            islem = input("Yapacağınız İşlem'in Numarasını Seçiniz (1-6): ")
            print()
            if islem == "1":
                ad = input("Eklenecek Ürün Adı: ")
                urunMenusu.urun_ekle(ad)

            elif islem == "2":
                urun = input("Düzenlenecek Ürün Adı: ")
                urunMenusu.urun_duzenleme(urun)

            elif islem == "3":
                urun = input("Kaldırılacak Ürünün Adı: ")
                urunMenusu.urun_sil(urun)

            elif islem == "4":
                ad = input("Stok Düzenlenecek Ürün Adı: ")
                urunMenusu.stok_duzenleme(ad)

            elif islem == "5":
                urunMenusu.urunleri_listele()

            elif islem == "6":
                print("Ürün Yönetimi Menüsünden Başarıyla Çıkış Yapıldı.\n")
                break

            else:
                print("Hatalı İşlem Numarası Girişi Yaptınız. Tekrar Deneyin!\n")
    elif islem1 == "2":
        while True:
            print("--İşlem Menüsü--\n1-Sipariş Onaylama\n2-Sipariş Durum Değişikliği\n3-Sipariş Listele\n4-İade İşlemleri\n5-Sipariş Oluştur\n6-İadeleri Listele\n7-Çıkış Yap\n")
            islem2 = input("Yapacağınız İşlem'in Numarasını Seçiniz (1-7): ")
            print()
            if islem2 == "1":
                siparisMenusu.siparis_onaylama()
            elif islem2 == "2":
                siparisMenusu.siparis_durum_degisiklik()
            elif islem2 == "3":
                siparisMenusu.siparis_listele()
            elif islem2 == "7":
                print("Sipariş Yönetimi Menüsünden Başarıyla Çıkış Yapıldı.")
                break
            elif islem2 == "4":
                siparisMenusu.iade_islem()
            elif islem2 == "5":
                siparisMenusu.siparis_olustur()
            elif islem2 == "6":
                siparisMenusu.iade_listele()
            else:
                print("Hatalı İşlem Numarası Girişi Yaptınız. Tekrar Deneyin!")

    elif islem1 == "3":
        print("PazarYerim'den Çıkış Yapıldı.")
        break
    else:
        print("Hatalı Giriş Yaptınız!\n")