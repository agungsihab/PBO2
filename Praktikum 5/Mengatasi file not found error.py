try:
    with open("File.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File yang anda buka tidak ditemukan!")