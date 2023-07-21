import requests
import json
class Penjualan:
    def __init__(self):
        self.__id=None
        self.__nomerpenjualan = None
        self.__kodebarang = None
        self.__nama_barang = None
        self.__stok_barang = None
        self.__url = "http://localhost/Penjualan_api/penjualan_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def nomerpenjualan(self):
        return self.__nomerpenjualan
        
    @nomerpenjualan.setter
    def nomerpenjualan(self, value):
        self.__nomerpenjualan = value
    @property
    def kodebarang(self):
        return self.__kodebarang
        
    @kodebarang.setter
    def kodebarang(self, value):
        self.__kodebarang = value
    @property
    def nama_barang(self):
        return self.__nama_barang
        
    @nama_barang.setter
    def nama_barang(self, value):
        self.__nama_barang = value
    @property
    def stok_barang(self):
        return self.__stok_barang
        
    @stok_barang.setter
    def stok_barang(self, value):
        self.__stok_barang = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nomerpenjualan(self, nomerpenjualan):
        url = self.__url+"?nomerpenjualan="+nomerpenjualan
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__nomerpenjualan = item['nomerpenjualan']
            self.__kodebarang = item['kodebarang']
            self.__nama_barang = item['nama_barang']
            self.__stok_barang = item['stok_barang']
        return data
    def simpan(self):
        payload = {
            "nomerpenjualan":self.__nomerpenjualan,
            "kodebarang":self.__kodebarang,
            "nama_barang":self.__nama_barang,
            "stok_barang":self.__stok_barang
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nomerpenjualan(self, nomerpenjualan):
        url = self.__url+"?nomerpenjualan="+nomerpenjualan
        payload = {
            "nomerpenjualan":self.__nomerpenjualan,
            "kodebarang":self.__kodebarang,
            "nama_barang":self.__nama_barang,
            "stok_barang":self.__stok_barang
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nomerpenjualan(self,nomerpenjualan):
        url = self.__url+"?nomerpenjualan="+nomerpenjualan
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
