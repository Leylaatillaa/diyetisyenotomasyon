import tkinter as tk
from tkinter import messagebox

class RandevuAl:
    def __init__(self, root):
        self.window = root
        self.window.title("Randevu Al")

        self.label_ad = tk.Label(self.window, text="Ad:")
        self.label_ad.grid(row=0, column=0, padx=10, pady=10)
        self.entry_ad = tk.Entry(self.window)
        self.entry_ad.grid(row=0, column=1, padx=10, pady=10)

        self.label_soyad = tk.Label(self.window, text="Soyad:")
        self.label_soyad.grid(row=1, column=0, padx=10, pady=10)
        self.entry_soyad = tk.Entry(self.window)
        self.entry_soyad.grid(row=1, column=1, padx=10, pady=10)

        self.label_tarih = tk.Label(self.window, text="Randevu Tarihi:")
        self.label_tarih.grid(row=2, column=0, padx=10, pady=10)
        self.entry_tarih = tk.Entry(self.window)
        self.entry_tarih.grid(row=2, column=1, padx=10, pady=10)

        self.button_randevu_al = tk.Button(self.window, text="Randevu Al", command=self.randevu_al)
        self.button_randevu_al.grid(row=3, column=0, columnspan=2, pady=10)

    def randevu_al(self):
        ad = self.entry_ad.get()
        soyad = self.entry_soyad.get()
        tarih = self.entry_tarih.get()

        if ad and soyad and tarih:
            bilgi = f"Randevu Bilgileri:\nAd: {ad}\nSoyad: {soyad}\nTarih: {tarih}"
            messagebox.showinfo("Randevu Alındı", bilgi)
        else:
            messagebox.showwarning("Hata", "Lütfen tüm bilgileri doldurun.")

class GirisFormu:
    def __init__(self, root):
        self.window = root
        self.window.title("Kullanıcı Girişi")
        self.label_kullanici = tk.Label(self.window, text="Kullanıcı Adi:")
        self.label_kullanici.grid(row=0, column=0, padx=10, pady=10)
        self.entry_kullanici = tk.Entry(self.window)
        self.entry_kullanici.grid(row=0, column=1, padx=10, pady=10)

        self.label_sifre = tk.Label(self.window, text="Şifre:")
        self.label_sifre.grid(row=1, column=0, padx=10, pady=10)
        self.entry_sifre = tk.Entry(self.window, show="*")
        self.entry_sifre.grid(row=1, column=1, padx=10, pady=10)

        self.button_giris = tk.Button(self.window, text="Giriş Yap", command=self.kullanici_giris_kontrol)
        self.button_giris.grid(row=2, column=0, columnspan=2, pady=10)

    def kullanici_giris_kontrol(self):
        ad = self.entry_kullanici.get()
        sifre = self.entry_sifre.get()

        if ad.lower() == "leyla" and sifre == "1234":
            self.window.destroy()
            self.acik_kayit_penceresi()
        else:
            self.label_sonuc = tk.Label(self.window, text="Kullanıcı adı veya şifre yanlış!")
            self.label_sonuc.grid(row=3, column=0, columnspan=2, pady=10)

    def acik_kayit_penceresi(self):
        root = tk.Tk()
        app = DiyetisyenOtomasyonuGUI(root)
        root.mainloop()

class DiyetisyenOtomasyonuGUI:

    def diyet_listesi_vki_18_alti(self):
        return {
            "Kahvaltı": [
                "1 su bardağı süt / 4 kaşık yoğurt",
                "1 porsiyon meyve / 2 kaşık yulaf",
                "1 yemek kaşığı fıstık ezmesi / 2 ceviz / 10 badem",
                "Tarçın"
            ],
            "Ara Öğün": [
                "Yeşil Çay / Kahve"
            ],
            "Akşam": [
                "2 köfte kadar et / tavuk göğüs / balık / hindi",
                "6 kaşık az yağlı sebze yemeği",
                "Mevsim Yeşillikleri",
                "1 kepçe çorba / 1 dilim tam buğday ekmek"
            ],
            "motivasyon": [
                "Siz bu değişiklikleri yapacak güce ve iradeye sahipsiniz. Hayalinizdeki sağlıklı yaşama bir adım daha yaklaşıyorsunuz. Devam edin, çünkü sizin başarınız benim için çok değerli!"
            ]

        }

    def diyet_listesi_vki_18_25(self):
        return {
            "Kahvaltı": [
                "1 haşlanmış yumurta",
                "Yarım yağlı beyaz peynir",
                "Mevsim yeşilliği",
                "Zeytin",
                "Tam buğday ekmek"
            ],
            "Öğle": [
                "Izgara köfte / balık / Tavuk göğüs / Hindi",
                "Yeşillik",
                "Çorba"
            ],
            "Ara": [
                "1 porsiyon meyve",
                "Çiğ Kuruyemiş"
            ],
            "Akşam": [
                "Kurubaklagil / Sebze Yemeği",
                "Mevsim Salatası",
                "Pilav / Tam Buğday Ekmek",
                "Yoğurt"
            ],

            "motivasyon": [
                "Her başlangıç, yeni bir fırsattır. Sağlıklı alışkanlıklar edinmeye başlamak, en değerli yatırımlarınızdan biridir. Siz bunu başarabilirsiniz!"         
            ]
        }

    def diyet_listesi_vki_25_30(self):
        return {
            "Kahvaltı": [
                "1 haşlanmış yumurta",
                "Yarım yağlı beyaz peynir",
                "Mevsim yeşilliği",
                "Zeytin",
                "Tam buğday ekmek"
            ],
            "Öğle": [
                "Izgara köfte / balık / Tavuk göğüs / Hindi",
                "Yeşillik",
                "Çorba"
            ],
            "Ara": [
                "1 porsiyon meyve",
                "Çiğ Kuruyemiş"
            ],
            "Akşam": [
                "Kurubaklagil / Sebze Yemeği",
                "Mevsim Salatası",
                "Pilav / Tam Buğday Ekmek",
                "Yoğurt"
            ],

            "motivasyon": [
                "Başlangıç noktanız neresi olursa olsun, şimdiye kadar attığınız her adım, daha sağlıklı ve mutlu bir geleceğe bir adım daha yaklaşmanız demektir."        
            ]
        }
        
    def diyet_listesi_vki_30_35(self):
        return {
            "Kahvaltı": [
                "1 haşlanmış yumurta",
                "Yarım yağlı beyaz peynir",
                "Mevsim yeşilliği",
                "Zeytin",
                "Tam buğday ekmek"
            ],
            "Öğle": [
                "Izgara köfte / balık / Tavuk göğüs / Hindi",
                "Yeşillik",
                "Çorba"
            ],
            "Ara": [
                "1 porsiyon meyve",
                "Çiğ Kuruyemiş"
            ],
            "Akşam": [
                "Kurubaklagil / Sebze Yemeği",
                "Mevsim Salatası",
                "Pilav / Tam Buğday Ekmek",
                "Yoğurt"
            ],
            "Ara Öğün": [
                "1 porsiyon meyve",
                "Süt / Kefir"
            ],
            "Egzersiz": [
                "Haftada 4-5 gün düzenli egzersiz"
            ],
            "motivasyon": [
                "Başlangıç noktanız neresi olursa olsun, şimdiye kadar attığınız her adım, daha sağlıklı ve mutlu bir geleceğe bir adım daha yaklaşmanız demektir."
            ]
        }

    def __init__(self, root):
        self.window = root
        self.window.title("Diyetisyen Otomasyonu")

        self.label_kilo = tk.Label(self.window, text="Kilo (kg):")
        self.label_kilo.grid(row=0, column=0, padx=10, pady=10)
        self.entry_kilo = tk.Entry(self.window)
        self.entry_kilo.grid(row=0, column=1, padx=10, pady=10)

        self.label_boy = tk.Label(self.window, text="Boy (cm):")
        self.label_boy.grid(row=1, column=0, padx=10, pady=10)
        self.entry_boy = tk.Entry(self.window)
        self.entry_boy.grid(row=1, column=1, padx=10, pady=10)

        self.button_hesapla = tk.Button(self.window, text="Vücut Kitle Endeksi Hesapla", command=self.hesapla)
        self.button_hesapla.grid(row=2, column=0, columnspan=2, pady=10)

        self.button_randevu = tk.Button(self.window, text="Randevu Al", command=self.randevu_ekrani_ac)
        self.button_randevu.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_randevu.grid_remove()

        self.label_sonuc = tk.Label(self.window, text="")
        self.label_sonuc.grid(row=4, column=0, columnspan=2, pady=10)

    def hesapla(self):
        try:
            kilo = float(self.entry_kilo.get())
            boy = float(self.entry_boy.get()) / 100
            vki = kilo / (boy ** 2)
            sonuc = f"Vücut Kitle Endeksi: {vki:.2f}"
            self.label_sonuc.config(text=sonuc)

            if vki >= 18:
                self.button_randevu.grid()
            else:
                self.button_randevu.grid_remove()

        except Exception as e:
            self.label_sonuc = tk.Label(self.window, text=f"Bir hata oluştu: {e}")

    def randevu_ekrani_ac(self):
        self.randevu_penceresi = tk.Toplevel(self.window)
        app = RandevuAl(self.randevu_penceresi)

if __name__ == "__main__":
    root = tk.Tk()
    giris_formu = GirisFormu(root)
    root.mainloop()