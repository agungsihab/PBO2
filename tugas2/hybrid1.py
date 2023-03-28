class Hewan:
    def __init__(self, nama, habitat):
        self.nama = nama
        self.habitat = habitat
    def Makan(self):
        print(f"{self.nama} sedang makan")
class Karnivora(Hewan):
    def __init__(self, nama, habitat, makanan):
        super().__init__(self, nama, habitat)
        self.makanan = makanan
    def mencakar(self):
        print(f"{self.nama} itu memangsa {self.makanan} untuk dimakan")
class Kaki_Empat (Hewan):
    def __init__(self, nama, habitat, suara):
        super().__init__( nama, habitat)
        self.suara = suara
    def memangsa (self):
        print(f"{self.nama} itu berlari mengejar {self.makanan} sambil mengaung {self.suara}")

class Harimau(Karnivora, Kaki_Empat):
    def __init__(self, nama, habitat, makanan, suara):
        Karnivora.__init__(self, nama, habitat, makanan)
        Kaki_Empat.__init__(self, nama, habitat, suara)
    def Mengaung(self):
        print(f"{self.nama} mengaung sangat keras")

harimauA = Harimau("Harimau Sumatra", "Hutan Sumatra", "Daging", "Rarrrrrr")
harimauA.Mengaung()
harimauA.memangsa()
harimauA.mencakar()
harimauA.Makan()