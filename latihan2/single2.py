#Nama   : Agung Sihab Malawi
#Kelas  : R1
#Nim    : 210511047
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def presentasi(self):
        print(f"{self.nama} sedang presentasi.")

class Dosen(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim
    def mengajar(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang presentasi.")
dosenA = Dosen("Agung Sihab Malawi", 20, "210511047")
dosenA.presentasi() 
dosenA.mengajar() 