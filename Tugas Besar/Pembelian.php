<?php
//Simpanlah dengan nama file : Pembelian.php
require_once 'database.php';
class Pembelian 
{
    private $db;
    private $table = 'pembelian';
    public $nomerpembelian = "";
    public $kodebarang = "";
    public $nama_pembeli = "";
    public $alamat = "";
    public $nomer_hp = "";
    public $nama_barang = "";
    public $jumblah_barang = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_nomerpembelian(int $nomerpembelian)
    {
        $query = "SELECT * FROM $this->table WHERE nomerpembelian = $nomerpembelian";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nomerpembelian`,`kodebarang`,`nama_pembeli`,`alamat`,`nomer_hp`,`nama_barang`,`jumblah_barang`) VALUES ('$this->nomerpembelian','$this->kodebarang','$this->nama_pembeli','$this->alamat','$this->nomer_hp','$this->nama_barang','$this->jumblah_barang')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nomerpembelian = '$this->nomerpembelian', kodebarang = '$this->kodebarang', nama_pembeli = '$this->nama_pembeli', alamat = '$this->alamat', nomer_hp = '$this->nomer_hp', nama_barang = '$this->nama_barang', jumblah_barang = '$this->jumblah_barang' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nomerpembelian($nomerpembelian): int
    {
        $query = "UPDATE $this->table SET nomerpembelian = '$this->nomerpembelian', kodebarang = '$this->kodebarang', nama_pembeli = '$this->nama_pembeli', alamat = '$this->alamat', nomer_hp = '$this->nomer_hp', nama_barang = '$this->nama_barang', jumblah_barang = '$this->jumblah_barang' 
        WHERE nomerpembelian = $nomerpembelian";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nomerpembelian($nomerpembelian): int
    {
        $query = "DELETE FROM $this->table WHERE nomerpembelian = $nomerpembelian";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>