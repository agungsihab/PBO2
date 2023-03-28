#Nama	: Agung Sihab Malawi
#Kelas  : R1
#NIM	: 210511047

class Perusahaan:
    def __init__(self, name):  
        self.name = name
    def speak(self): 
        print(f"{self.name} speaks")

class Karyawan(Perusahaan):
    def __init__(self, name, nip): 
        super().__init__(name) 
        self.nip = nip
    def data(self):
        print(f"{self.name} dengan nip {self.nip}")

class Informasi(Karyawan):
    def __init__(self, name, nip, alamat, perusahaan): 
        super(). __init__(name, nip)
        self.alamat = alamat 
        self.perusahaan = perusahaan
    def speak(self):
        print(f"{self.name} Beralamatkan {self.alamat}, bekerja di perusahaan {self.perusahaan}")
        print("="*54)

Informasi = Informasi("Agung Sihab Malawi", 210511047, "Cirebon", "PT Microsoft Indonesia")
Informasi.data() 
Informasi.speak()
