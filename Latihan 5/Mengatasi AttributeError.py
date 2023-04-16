class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
mahasiswa = Mahasiswa("Tegar", 20)
try:
    print(mahasiswa.alamat)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")