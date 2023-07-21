import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Penjualan import *
class FrmPenjualan:
    
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
        Label(mainFrame, text='NOMERPENJUALAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBARANG:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_BARANG:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STOK_BARANG:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNomerpenjualan = Entry(mainFrame) 
        self.txtNomerpenjualan.grid(row=0, column=1, padx=5, pady=5)
        self.txtNomerpenjualan.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtKodebarang = Entry(mainFrame) 
        self.txtKodebarang.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtNama_barang = StringVar()
        Cbo_nama_barang = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtNama_barang) 
        Cbo_nama_barang.grid(row=2, column=1, padx=5, pady=5)
        # Adding nama_barang combobox drop down list
        Cbo_nama_barang['values'] = ('Buku','Pensil','Pulpen','Penghapus','Penggaris')
        Cbo_nama_barang.current()
        # Textbox
        self.txtStok_barang = Entry(mainFrame) 
        self.txtStok_barang.grid(row=3, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','nomerpenjualan','kodebarang','nama_barang','stok_barang')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nomerpenjualan', text='NOMERPENJUALAN')
        self.tree.column('nomerpenjualan', width="50")
        self.tree.heading('kodebarang', text='KODEBARANG')
        self.tree.column('kodebarang', width="50")
        self.tree.heading('nama_barang', text='NAMA_BARANG')
        self.tree.column('nama_barang', width="50")
        self.tree.heading('stok_barang', text='STOK_BARANG')
        self.tree.column('stok_barang', width="50")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNomerpenjualan.delete(0,END)
        self.txtNomerpenjualan.insert(END,"")
        self.txtKodebarang.delete(0,END)
        self.txtKodebarang.insert(END,"")
        self.txtNama_barang.set("")
        self.txtStok_barang.delete(0,END)
        self.txtStok_barang.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data penjualan
        obj = Penjualan()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["nomerpenjualan"],d["kodebarang"],d["nama_barang"],d["stok_barang"]))
    def onCari(self, event=None):
        nomerpenjualan = self.txtNomerpenjualan.get()
        obj = Penjualan()
        a = obj.get_by_nomerpenjualan(nomerpenjualan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nomerpenjualan = self.txtNomerpenjualan.get()
        obj = Penjualan()
        res = obj.get_by_nomerpenjualan(nomerpenjualan)
        self.txtNomerpenjualan.delete(0,END)
        self.txtNomerpenjualan.insert(END,obj.nomerpenjualan)
        self.txtKodebarang.delete(0,END)
        self.txtKodebarang.insert(END,obj.kodebarang)
        self.txtNama_barang.set(obj.nama_barang)
        self.txtStok_barang.delete(0,END)
        self.txtStok_barang.insert(END,obj.stok_barang)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        nomerpenjualan = self.txtNomerpenjualan.get()
        kodebarang = self.txtKodebarang.get()
        nama_barang = self.txtNama_barang.get()
        stok_barang = self.txtStok_barang.get()
        # create new Object
        obj = Penjualan()
        obj.nomerpenjualan = nomerpenjualan
        obj.kodebarang = kodebarang
        obj.nama_barang = nama_barang
        obj.stok_barang = stok_barang
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nomerpenjualan(nomerpenjualan)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nomerpenjualan = self.txtNomerpenjualan.get()
        obj = Penjualan()
        obj.nomerpenjualan = nomerpenjualan
        if(self.ditemukan==True):
            res = obj.delete_by_nomerpenjualan(nomerpenjualan)
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
    aplikasi = FrmPenjualan(root2, "Aplikasi Data Penjualan")
    root2.mainloop()
