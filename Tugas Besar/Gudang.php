<?php
//Simpanlah dengan nama file : Gudang.php
require_once 'database.php';
class Gudang 
{
    private $db;
    private $table = 'gudang';
    public $nomergudang = "";
    public $kodebarang = "";
    public $nama_barang = "";
    public $stok_barang = "";
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
    public function get_by_nomergudang(int $nomergudang)
    {
        $query = "SELECT * FROM $this->table WHERE nomergudang = $nomergudang";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nomergudang`,`kodebarang`,`nama_barang`,`stok_barang`) VALUES ('$this->nomergudang','$this->kodebarang','$this->nama_barang','$this->stok_barang')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nomergudang = '$this->nomergudang', kodebarang = '$this->kodebarang', nama_barang = '$this->nama_barang', stok_barang = '$this->stok_barang' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nomergudang($nomergudang): int
    {
        $query = "UPDATE $this->table SET nomergudang = '$this->nomergudang', kodebarang = '$this->kodebarang', nama_barang = '$this->nama_barang', stok_barang = '$this->stok_barang' 
        WHERE nomergudang = $nomergudang";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nomergudang($nomergudang): int
    {
        $query = "DELETE FROM $this->table WHERE nomergudang = $nomergudang";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>