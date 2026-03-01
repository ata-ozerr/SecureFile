import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import os
import aes_şfreleme # Kendi şifreleme modülümüzü dahil ettik

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SecureFile - Ana Menü")
        self.root.geometry("900x500")
        self.root.configure(fg_color="white")
        self.root.resizable(False, False)

        try:
            self.bg_image = Image.open("laptop.png") 
            self.bg_image = self.bg_image.resize((320, 480))
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)

            self.bg_label = ctk.CTkLabel(self.root, image=self.bg_photo, text="")
            self.bg_label.place(x=510, y=40)
        except:
            print("Fotoğraf yüklenemedi, klasörü kontrol et!")

        self.baslik = ctk.CTkLabel(self.root, text="SECURE FILE", font=("Impact", 35), text_color="#3498db", justify="left")
        self.baslik.place(x=120, y=80)

        btn_style = {"width": 250, "height": 50, "corner_radius": 8, "font": ("Arial", 14, "bold")}

        self.btn_sifrele = ctk.CTkButton(self.root, text="ENCRYPTION (ŞİFRELE)", command=self.sifrele_ekrani, **btn_style)
        self.btn_sifrele.place(x=120, y=180)

        self.btn_coz = ctk.CTkButton(self.root, text="DECRYPTION (ŞİFRE ÇÖZ)", command=self.coz_ekrani, **btn_style)
        self.btn_coz.place(x=120, y=250)

        self.btn_cikis = ctk.CTkButton(self.root, text="EXIT", command=self.root.quit, fg_color="#e74c3c", hover_color="#c0392b", **btn_style)
        self.btn_cikis.place(x=120, y=320)

    def sifrele_ekrani(self):
        self.root.withdraw() 
        self.yeni_pencere("Şifreleme İşlemi", "sifrele")

    def coz_ekrani(self):
        self.root.withdraw() 
        self.yeni_pencere("Şifre Çözme İşlemi", "coz")

    def yeni_pencere(self, baslik, islem_tipi):
        pencere = ctk.CTkToplevel(self.root)
        pencere.title(baslik)
        pencere.geometry("800x500")
        pencere.configure(fg_color="white")
        
        pencere.protocol("WM_DELETE_WINDOW", lambda: self.menuya_don(pencere))

        ctk.CTkLabel(pencere, text=baslik.upper(), font=("Arial", 24, "bold")).pack(pady=30)
        
        yol_kutusu = ctk.CTkEntry(pencere, width=450, height=40, placeholder_text="Dosya yolu...")
        yol_kutusu.pack(pady=20)

        def sec():
            yol = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if yol:
                yol_kutusu.delete(0, "end")
                yol_kutusu.insert(0, yol)

        def baslat():
            girdi = yol_kutusu.get()
            if not girdi: return
            
            try:
                if islem_tipi == "sifrele":
                    # Metin dosyasını okuyoruz
                    with open(girdi, 'r', encoding='utf-8') as f: 
                        duzmetin = f.read()

                    # AES ŞİFRELEME (Gerçek fonksiyona yolluyoruz)
                    sifreli_hex, anahtar_hex, tka_hex = aes_şfreleme.sifrele(duzmetin)

                    cikti = os.path.dirname(girdi) + "/sifreli_" + os.path.basename(girdi)
                    
                    # Şifreyi çözebilmek için anahtar ve tka'yı da dosyaya kaydediyoruz
                    with open(cikti, 'w', encoding='utf-8') as f: 
                        f.write(f"{anahtar_hex}\n{tka_hex}\n{sifreli_hex}")

                    messagebox.showinfo("Başarılı", f"Dosya Şifrelendi!\nKonum: {cikti}")

                else:
                    # Şifreli metin dosyasını okuyoruz
                    with open(girdi, 'r', encoding='utf-8') as f:
                        satirlar = f.read().split('\n')

                    if len(satirlar) < 3:
                        messagebox.showerror("Hata", "Dosya formatı hatalı veya şifreli değil!")
                        return

                    # Kaydettiğimiz sıraya göre verileri geri çekiyoruz
                    anahtar_hex = satirlar[0]
                    tka_hex = satirlar[1]
                    sifreli_hex = satirlar[2]

                    # AES DEŞİFRE
                    cozulmus_metin = aes_şfreleme.cozucu(sifreli_hex, anahtar_hex, tka_hex)

                    temiz_isim = os.path.basename(girdi).replace("sifreli_", "")
                    cikti = os.path.dirname(girdi) + "/cozulmus_" + temiz_isim
                    
                    with open(cikti, 'w', encoding='utf-8') as f: 
                        f.write(cozulmus_metin)

                    messagebox.showinfo("Başarılı", f"Şifre Çözüldü!\nKonum: {cikti}")
                
                self.menuya_don(pencere) 
                
            except Exception as error: # Hata veren typo düzeltildi
                messagebox.showerror("Hata", f"İşlem sırasında bir hata oluştu: {error}")

        ctk.CTkButton(pencere, text="DOSYA SEÇ", command=sec, width=150).pack(pady=10)
        ctk.CTkButton(pencere, text="İŞLEMİ BAŞLAT", command=baslat, fg_color="#2ecc71", width=200, height=40).pack(pady=30)
        ctk.CTkButton(pencere, text="GERİ DÖN", command=lambda: self.menuya_don(pencere), fg_color="gray").pack()

    def menuya_don(self, pencere):
        pencere.destroy() 
        self.root.deiconify() 

if __name__ == "__main__":
    root = ctk.CTk()
    app = CipherApp(root)
    root.mainloop()