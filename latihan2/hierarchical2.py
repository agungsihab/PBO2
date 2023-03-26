#Nama	: Agung Sihab Malawi
#Kelas  : R1
#NIM	: 210511047

class Ekspedisi:
    def __init__(self, nama, umur, gaji): 
        self.nama = nama
        self.umur = umur 
        self.gaji = gaji

    def get_nama(self): 
        return self.nama
    def get_umur(self): 
        return self.umur
    def get_gaji(self): 
        return self.gaji
 
    def speak(self): 
        print(f"{self.nama} speaks")

class Kurir(Ekspedisi):
    def __init__(self, nama, umur, gaji, department): 
        super().__init__(nama, umur, gaji) 
        self.department = department
    def get_department(self): 
        return self.department

class Datakurir(Ekspedisi):
    def __init__(self, nama, umur, gaji, alamat): 
        super().__init__ (nama, umur, gaji) 
        self.alamat = alamat
    def get_alamat(self): 
        return self.alamat

# Hierarchical Inheritance
class SeniorDatakurir(Datakurir):
    def __init__(self, nama, umur, gaji, alamat, ekspedisi): 
        super().__init__(nama, umur, gaji, alamat) 
        self.ekspedisi = ekspedisi
    def get_ekspedisi(self): 
        return self.ekspedisi
    def data(self):
        print(f"{self.nama} Berumur {self.umur} tahun berpenghasilan Rp{self.gaji} /Bulan, alamat pengantaran {self.alamat} dengan ekspedisi {self.ekspedisi}.")
print("="*54)

Pengunjung = SeniorDatakurir("Agung Sihab Malawi", 20, 5000.000, "Cirebon", "JNE")
Pengunjung.data()
