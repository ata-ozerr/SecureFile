import datetime    #kütüphaneyi eklemeliyiz. çünkü hata olduğunda saat bilgisi vermeliyiz.
import os          #Dosya islemlerini yapmak için gerekli

def anahtarKontrolu(anahtar):       #kullandıgimiz AES sisteminde anahtar uzunlugu sabit (128 192 256)
    if len(anahtar) != 32:           #kullanıcı yanlıs uzunlukta hata girmesin diye yapılıyor  
        return False
    return True


def dosyaVarMi (dosya_yolu):
    if os.path.exists(dosya_yolu): # bu kod bloğu dosyanin gerçekte olup olmadigini kontrol eder
        return True
    return False


def mesajYaz (mesaj):                 #hata ya da bilgi msajlarını file diye adlandırdıgımız dosyaya yazmak
    zaman =datetime.datetime.now ()               #su anki zamani alir 
    with open ("file.txt","a") as dosya:           # file dosaysını acar
        dosya.write(str(zaman) +"-" + mesaj + "\n")   #dosya.write nin görevi açılmış dosyaya yazı yazmaktır



        

