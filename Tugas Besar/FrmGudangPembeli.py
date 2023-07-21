import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Gudang import *
class FrmGudangPembeli:
    
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
        Label(mainFrame, text='NOMERGUDANG:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBARANG:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_BARANG:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STOK_BARANG:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNomergudang = Entry(mainFrame) 
        self.txtNomergudang.grid(row=0, column=1, padx=5, pady=5)
        self.txtNomergudang.bind("<Return>",self.onCari) # menambahkan event Enter key
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
        self.btnSimpan = Button(mainFrame, text='Cari Barang', command=self.onCari, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','nomergudang','kodebarang','nama_barang','stok_barang')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nomergudang', text='NOMERGUDANG')
        self.tree.column('nomergudang', width="80")
        self.tree.heading('kodebarang', text='KODEBARANG')
        self.tree.column('kodebarang', width="80")
        self.tree.heading('nama_barang', text='NAMA_BARANG')
        self.tree.column('nama_barang', width="80")
        self.tree.heading('stok_barang', text='STOK_BARANG')
        self.tree.column('stok_barang', width="80")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNomergudang.delete(0,END)
        self.txtNomergudang.insert(END,"")
        self.txtKodebarang.delete(0,END)
        self.txtKodebarang.insert(END,"")
        self.txtNama_barang.set("")
        self.txtStok_barang.delete(0,END)
        self.txtStok_barang.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data gudang
        obj = Gudang()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["nomergudang"],d["kodebarang"],d["nama_barang"],d["stok_barang"]))
    def onCari(self, event=None):
        nomergudang = self.txtNomergudang.get()
        obj = Gudang()
        a = obj.get_by_nomergudang(nomergudang)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nomergudang = self.txtNomergudang.get()
        obj = Gudang()
        res = obj.get_by_nomergudang(nomergudang)
        self.txtNomergudang.delete(0,END)
        self.txtNomergudang.insert(END,obj.nomergudang)
        self.txtKodebarang.delete(0,END)
        self.txtKodebarang.insert(END,obj.kodebarang)
        self.txtNama_barang.set(obj.nama_barang)
        self.txtStok_barang.delete(0,END)
        self.txtStok_barang.insert(END,obj.stok_barang)
        
                 
    def onSimpan(self, event=None):
        # get the data from input
        nomergudang = self.txtNomergudang.get()
        kodebarang = self.txtKodebarang.get()
        nama_barang = self.txtNama_barang.get()
        stok_barang = self.txtStok_barang.get()
        # create new Object
        obj = Gudang()
        obj.nomergudang = nomergudang
        obj.kodebarang = kodebarang
        obj.nama_barang = nama_barang
        obj.stok_barang = stok_barang
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nomergudang(nomergudang)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nomergudang = self.txtNomergudang.get()
        obj = Gudang()
        obj.nomergudang = nomergudang
        if(self.ditemukan==True):
            res = obj.delete_by_nomergudang(nomergudang)
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
    aplikasi = FrmGudangPembeli(root2, "Aplikasi Data Gudang")
    root2.mainloop()
