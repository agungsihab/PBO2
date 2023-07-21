import requests
import json
class Pembelian:
    def __init__(self):
        self.__id=None
        self.__nomerpembelian = None
        self.__kodebarang = None
        self.__nama_pembeli = None
        self.__alamat = None
        self.__nomer_hp = None
        self.__nama_barang = None
        self.__jumblah_barang = None
        self.__url = "http://localhost/Penjualan_api/pembelian_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def nomerpembelian(self):
        return self.__nomerpembelian
        
    @nomerpembelian.setter
    def nomerpembelian(self, value):
        self.__nomerpembelian = value
    @property
    def kodebarang(self):
        return self.__kodebarang
        
    @kodebarang.setter
    def kodebarang(self, value):
        self.__kodebarang = value
    @property
    def nama_pembeli(self):
        return self.__nama_pembeli
        
    @nama_pembeli.setter
    def nama_pembeli(self, value):
        self.__nama_pembeli = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    @property
    def nomer_hp(self):
        return self.__nomer_hp
        
    @nomer_hp.setter
    def nomer_hp(self, value):
        self.__nomer_hp = value
    @property
    def nama_barang(self):
        return self.__nama_barang
        
    @nama_barang.setter
    def nama_barang(self, value):
        self.__nama_barang = value
    @property
    def jumblah_barang(self):
        return self.__jumblah_barang
        
    @jumblah_barang.setter
    def jumblah_barang(self, value):
        self.__jumblah_barang = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nomerpembelian(self, nomerpembelian):
        url = self.__url+"?nomerpembelian="+nomerpembelian
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__nomerpembelian = item['nomerpembelian']
            self.__kodebarang = item['kodebarang']
            self.__nama_pembeli = item['nama_pembeli']
            self.__alamat = item['alamat']
            self.__nomer_hp = item['nomer_hp']
            self.__nama_barang = item['nama_barang']
            self.__jumblah_barang = item['jumblah_barang']
        return data
    def simpan(self):
        payload = {
            "nomerpembelian":self.__nomerpembelian,
            "kodebarang":self.__kodebarang,
            "nama_pembeli":self.__nama_pembeli,
            "alamat":self.__alamat,
            "nomer_hp":self.__nomer_hp,
            "nama_barang":self.__nama_barang,
            "jumblah_barang":self.__jumblah_barang
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nomerpembelian(self, nomerpembelian):
        url = self.__url+"?nomerpembelian="+nomerpembelian
        payload = {
            "nomerpembelian":self.__nomerpembelian,
            "kodebarang":self.__kodebarang,
            "nama_pembeli":self.__nama_pembeli,
            "alamat":self.__alamat,
            "nomer_hp":self.__nomer_hp,
            "nama_barang":self.__nama_barang,
            "jumblah_barang":self.__jumblah_barang
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nomerpembelian(self,nomerpembelian):
        url = self.__url+"?nomerpembelian="+nomerpembelian
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
