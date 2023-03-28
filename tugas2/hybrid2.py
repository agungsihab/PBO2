class Hewan:
    def __init__(self, nama, habitat):
        self.nama = nama
        self.habitat = habitat
    def Makan(self):
        print(f"{self.nama} sedang mematuk biji jagung")
class Unggas(Hewan):
    def __init__(self, nama, habitat, makanan):
        super().__init__(self, nama, habitat)
        self.makanan = makanan
    def Terbang(self):
        print(f"{self.nama} itu terbang untuk memakan {self.makanan} ")
class Kaki_Dua (Hewan):
    def __init__(self, nama, habitat, suara):
        super().__init__( nama, habitat)
        self.suara = suara
    def Mematuk (self):
        print(f"{self.nama} itu terbang mengejar {self.makanan} sambil berkokok {self.suara}")

class Ayam(Unggas, Kaki_Dua):
    def __init__(self, nama, habitat, makanan, suara):
        Unggas.__init__(self, nama, habitat, makanan)
        Kaki_Dua.__init__(self, nama, habitat, suara)
    def Berkokok(self):
        print(f"{self.nama} berkokok di pagi hari untuk membangunkan orang")

ayamA = Ayam("Ayam jantan", "Peternakan", "Dedak", "Kukuruyuk")
ayamA.Berkokok()
ayamA.Mematuk()
ayamA.Terbang()
ayamA.Makan()
