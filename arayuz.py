import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import os

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