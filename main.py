import datetime    #kütüphaneyi eklemeliyiz. çünkü saat bilgisi vermeliyiz hata oldugunda.
import os          #Dosya islemlerini yapmak için gerekli

def anahtarKontrolu(anahtar):       #kullandıgimiz AES sisteminde anahtar uzunlugu sabit (128 192 256)
    if len(anahtar) != 32:           #kullanıcı yanlıs uzunlukta hata girmesin diye yapılıyor  
        return False
    return True


def dosyaVarMi (dosya_yolu):
    if os.path.exists(dosya_yolu): # bu kod bloğu dosyanin gerçekte olup olmadigini kontrol eder
        return True
    return False

