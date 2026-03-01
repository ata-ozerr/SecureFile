import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def sifreleme_aracı(a):#iki farklı yerde kullanılan anahtarla yapılan şifreleme aracı kısmının fonksiyonu
    b = AESGCM(a)
    return b

def sifrele(duzmetin):#"duzmetin" alıcıdan alınan metin
    bytemetin = duzmetin.encode('utf-8')#alınan metni bilgisayarın anlayacağı şekle çevirdi türkçe sorun olmasın diye utf-8 kullanıldı

    anahtar = os.urandom(32)#rastgele 32 byte anahtar oluşturuyor
    tka = os.urandom(12)#rastgele 12 byte tek kullanımlık anahtar(nonce) oluşturuyor

    safs=sifreleme_aracı(anahtar)#fonksiyona yonlendiriyor
    sifrelenmis_metin=safs.encrypt(tka, bytemetin, associated_data=None)#meni sifreliyor

    okunabilir_sifrelenmis_hal=sifrelenmis_metin.hex()#makine dilini okunabilir hexadecimal harf sayıara döker
    okunabilir_anahtar=anahtar.hex()
    okunabilir_tka=tka.hex()

    return okunabilir_sifrelenmis_hal,okunabilir_anahtar,okunabilir_tka


def cozucu(sifreli_gelen_metinh , anahtar2h , tka2h):

    sifreli_gelen_metin=bytes.fromhex(sifreli_gelen_metinh)#metni tekrar makine diline çevirir
    anahtar2=bytes.fromhex(anahtar2h)
    tka2=bytes.fromhex(tka2h)

    safs2=sifreleme_aracı(anahtar2)#fonksiyona yonlendiriyor
    cozulmus_metin_byte=safs2.decrypt(tka2 ,sifreli_gelen_metin, associated_data=None)#şifrelemeyi çözer
    cozulmus_metin=cozulmus_metin_byte.decode('utf-8')#şifrelemeyi insan diline çevrir

    return cozulmus_metin









