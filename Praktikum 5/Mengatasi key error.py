data = {"Kucing": 11, "Ikan": 22, "Ayam": 43}
try:
    value = data["Kambing"]
except KeyError:
    print("Key yang dicari tidak ditemukan pada data!")