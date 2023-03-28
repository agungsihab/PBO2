#Nama	: Agung Sihab Malawi
#Kelas  : R1
#NIM	: 210511047

class Perpus:
    def __init__(self, name):
        self.name = name
    def speak(self): 
        print(f"{self.name} speaks")

class Penjaga(Perpus):
    def __init__(self, name, nip):
        super().__init__(name) 
        self.nip = nip
    def data(self):
        print(f"{self.name} dengan nip {self.nip}")

class Pengunjung(Penjaga):
    def __init__(self, name, nip, alamat): 
        super().__init__(name, nip) 
        self.alamat = alamat
    def speak(self):
        print(f"{self.name} Beralamatkan {self.alamat} berkunjungjung ke Perpustakaan")
        print("="*54)

Pengunjung = Pengunjung("Agung Sihab Malawi", 210511047, "Cirebon") 
Pengunjung.data()
Pengunjung.speak()
