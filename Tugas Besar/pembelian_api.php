<?php
require_once 'database.php';
require_once 'Pembelian.php';
$db = new MySQLDatabase();
$pembelian = new Pembelian($db);
$id=0;
$nomerpembelian=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomerpembelian'])){
            $nomerpembelian = $_GET['nomerpembelian'];
        }
        if($id>0){    
            $result = $pembelian->get_by_id($id);
        }elseif($nomerpembelian>0){
            $result = $pembelian->get_by_nomerpembelian($nomerpembelian);
        } else {
            $result = $pembelian->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pembelian
        $pembelian->nomerpembelian = $_POST['nomerpembelian'];
        $pembelian->kodebarang = $_POST['kodebarang'];
        $pembelian->nama_pembeli = $_POST['nama_pembeli'];
        $pembelian->alamat = $_POST['alamat'];
        $pembelian->nomer_hp = $_POST['nomer_hp'];
        $pembelian->nama_barang = $_POST['nama_barang'];
        $pembelian->jumblah_barang = $_POST['jumblah_barang'];
       
        $pembelian->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pembelian created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pembelian not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomerpembelian'])){
            $nomerpembelian = $_GET['nomerpembelian'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $pembelian->nomerpembelian = $_PUT['nomerpembelian'];
        $pembelian->kodebarang = $_PUT['kodebarang'];
        $pembelian->nama_pembeli = $_PUT['nama_pembeli'];
        $pembelian->alamat = $_PUT['alamat'];
        $pembelian->nomer_hp = $_PUT['nomer_hp'];
        $pembelian->nama_barang = $_PUT['nama_barang'];
        $pembelian->jumblah_barang = $_PUT['jumblah_barang'];
        if($id>0){    
            $pembelian->update($id);
        }elseif($nomerpembelian<>""){
            $pembelian->update_by_nomerpembelian($nomerpembelian);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pembelian updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pembelian update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomerpembelian'])){
            $nomerpembelian = $_GET['nomerpembelian'];
        }
        if($id>0){    
            $pembelian->delete($id);
        }elseif($nomerpembelian>0){
            $pembelian->delete_by_nomerpembelian($nomerpembelian);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pembelian deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pembelian delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>