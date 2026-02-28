import tkinter as tk
from tkinter import filedialog, messagebox
import os

def dosya_secim_ekrani():
    yol = filedialog.askopenfilename(title="İşlem yapılacak dosyayı seçin")
    if yol:
        dosya_kutusu.delete(0, tk.END)
        dosya_kutusu.insert(0, yol)
        durum_yazisi.config(text=f"Seçildi: {os.path.basename(yol)}", fg="blue")

def dosyayi_sifrele():
    girdi = dosya_kutusu.get()
    
    if not girdi:
        messagebox.showwarning("Uyarı", "Lütfen önce bir dosya seçin!")
        return

    try:
        with open(girdi, 'rb') as file:
            ilk_veri = file.read()

        # AES ŞİFRELEME 
        sifreli_veri = ilk_veri # Deneme yapabilmek için yazdım.
        iv = b"16_BYTE_IV_TEST!" # AES için gereken 16 byte'lık örnek IV
  

        cikti = os.path.dirname(girdi) + "/sifreli_" + os.path.basename(girdi)
        
        with open(cikti, 'wb') as file:
            file.write(iv + sifreli_veri)

        messagebox.showinfo("Başarılı", f"Dosya Şifrelendi:\n{cikti}")
        durum_yazisi.config(text="Şifreleme Başarılı!", fg="green")

    except Exception as error:
        messagebox.showerror("Hata", f"Okuma/Yazma hatası: {error}")

def sifreyi_coz():
    girdi = dosya_yolu_kutusu.get()
    
    if not girdi:
        messagebox.showwarning("Uyarı", "Lütfen şifreli dosyayı seçin!")
        return

    try:
        with open(girdi, 'rb') as file:
            icerik = file.read()

        if len(icerik) < 16:
            messagebox.showerror("Hata", "Dosya çok kısa veya şifreli değil!")
            return
            
        iv = icerik[:16]
        sifreli_kisim = icerik[16:]

        # AES DEŞİFRE 
        
        cozulmus_veri = sifreli_kisim #Geçici, denemek için koydum.

        yeni_isim = os.path.basename(girdi).replace("sifreli_", "")
        cikti = os.path.dirname(girdi) + "/cozulmus_" + yeni_isim
        
        with open(cikti, 'wb') as file:
            file.write(cozulmus_veri)

        messagebox.showinfo("Başarılı", f"Şifre Çözüldü:\n{cikti}")
        durum_yazisi.config(text="Şifre Çözme Başarılı!", fg="green")

    except Exception as error:
        messagebox.showerror("Hata", f"İşlem hatası: {error}")
        

