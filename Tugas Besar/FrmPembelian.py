import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pembelian import *
class FrmPembelian:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='NOMERPEMBELIAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBARANG:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_PEMBELI:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NOMER_HP:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_BARANG:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUMBLAH_BARANG:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNomerpembelian = Entry(mainFrame) 
        self.txtNomerpembelian.grid(row=0, column=1, padx=5, pady=5)
        self.txtNomerpembelian.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtKodebarang = Entry(mainFrame) 
        self.txtKodebarang.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtNama_pembeli = Entry(mainFrame) 
        self.txtNama_pembeli.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtNomer_hp = Entry(mainFrame) 
        self.txtNomer_hp.grid(row=4, column=1, padx=5, pady=5)
        # Combo Box
        self.txtNama_barang = StringVar()
        Cbo_nama_barang = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtNama_barang) 
        Cbo_nama_barang.grid(row=5, column=1, padx=5, pady=5)
        # Adding nama_barang combobox drop down list
        Cbo_nama_barang['values'] = ('Buku','Pensil','Pulpen','Penghapus','Penggaris')
        Cbo_nama_barang.current()
        # Textbox
        self.txtJumblah_barang = Entry(mainFrame) 
        self.txtJumblah_barang.grid(row=6, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','nomerpembelian','kodebarang','nama_pembeli','alamat','nomer_hp','nama_barang','jumblah_barang')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nomerpembelian', text='NOMERPEMBELIAN')
        self.tree.column('nomerpembelian', width="30")
        self.tree.heading('kodebarang', text='KODEBARANG')
        self.tree.column('kodebarang', width="30")
        self.tree.heading('nama_pembeli', text='NAMA_PEMBELI')
        self.tree.column('nama_pembeli', width="80")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="80")
        self.tree.heading('nomer_hp', text='NOMER_HP')
        self.tree.column('nomer_hp', width="50")
        self.tree.heading('nama_barang', text='NAMA_BARANG')
        self.tree.column('nama_barang', width="50")
        self.tree.heading('jumblah_barang', text='JUMBLAH_BARANG')
        self.tree.column('jumblah_barang', width="30")
        # set tree position
        self.tree.place(x=0, y=250)
        
    def onClear(self, event=None):
        self.txtNomerpembelian.delete(0,END)
        self.txtNomerpembelian.insert(END,"")
        self.txtKodebarang.delete(0,END)
        self.txtKodebarang.insert(END,"")
        self.txtNama_pembeli.delete(0,END)
        self.txtNama_pembeli.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.txtNomer_hp.delete(0,END)
        self.txtNomer_hp.insert(END,"")
        self.txtNama_barang.set("")
        self.txtJumblah_barang.delete(0,END)
        self.txtJumblah_barang.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pembelian
        obj = Pembelian()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["nomerpembelian"],d["kodebarang"],d["nama_pembeli"],d["alamat"],d["nomer_hp"],d["nama_barang"],d["jumblah_barang"]))
    def onCari(self, event=None):
        nomerpembelian = self.txtNomerpembelian.get()
        obj = Pembelian()
        a = obj.get_by_nomerpembelian(nomerpembelian)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nomerpembelian = self.txtNomerpembelian.get()
        obj = Pembelian()
        res = obj.get_by_nomerpembelian(nomerpembelian)
        self.txtNomerpembelian.delete(0,END)
        self.txtNomerpembelian.insert(END,obj.nomerpembelian)
        self.txtKodebarang.delete(0,END)
        self.txtKodebarang.insert(END,obj.kodebarang)
        self.txtNama_pembeli.delete(0,END)
        self.txtNama_pembeli.insert(END,obj.nama_pembeli)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.txtNomer_hp.delete(0,END)
        self.txtNomer_hp.insert(END,obj.nomer_hp)
        self.txtNama_barang.set(obj.nama_barang)
        self.txtJumblah_barang.delete(0,END)
        self.txtJumblah_barang.insert(END,obj.jumblah_barang)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        nomerpembelian = self.txtNomerpembelian.get()
        kodebarang = self.txtKodebarang.get()
        nama_pembeli = self.txtNama_pembeli.get()
        alamat = self.txtAlamat.get()
        nomer_hp = self.txtNomer_hp.get()
        nama_barang = self.txtNama_barang.get()
        jumblah_barang = self.txtJumblah_barang.get()
        # create new Object
        obj = Pembelian()
        obj.nomerpembelian = nomerpembelian
        obj.kodebarang = kodebarang
        obj.nama_pembeli = nama_pembeli
        obj.alamat = alamat
        obj.nomer_hp = nomer_hp
        obj.nama_barang = nama_barang
        obj.jumblah_barang = jumblah_barang
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nomerpembelian(nomerpembelian)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nomerpembelian = self.txtNomerpembelian.get()
        obj = Pembelian()
        obj.nomerpembelian = nomerpembelian
        if(self.ditemukan==True):
            res = obj.delete_by_nomerpembelian(nomerpembelian)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPembelian(root2, "Aplikasi Data Pembelian")
    root2.mainloop()
