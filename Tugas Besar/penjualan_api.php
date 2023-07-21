<?php
require_once 'database.php';
require_once 'Penjualan.php';
$db = new MySQLDatabase();
$penjualan = new Penjualan($db);
$id=0;
$nomerpenjualan=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomerpenjualan'])){
            $nomerpenjualan = $_GET['nomerpenjualan'];
        }
        if($id>0){    
            $result = $penjualan->get_by_id($id);
        }elseif($nomerpenjualan>0){
            $result = $penjualan->get_by_nomerpenjualan($nomerpenjualan);
        } else {
            $result = $penjualan->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new penjualan
        $penjualan->nomerpenjualan = $_POST['nomerpenjualan'];
        $penjualan->kodebarang = $_POST['kodebarang'];
        $penjualan->nama_barang = $_POST['nama_barang'];
        $penjualan->stok_barang = $_POST['stok_barang'];
       
        $penjualan->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Penjualan created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Penjualan not created.';
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
        if(isset($_GET['nomerpenjualan'])){
            $nomerpenjualan = $_GET['nomerpenjualan'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $penjualan->nomerpenjualan = $_PUT['nomerpenjualan'];
        $penjualan->kodebarang = $_PUT['kodebarang'];
        $penjualan->nama_barang = $_PUT['nama_barang'];
        $penjualan->stok_barang = $_PUT['stok_barang'];
        if($id>0){    
            $penjualan->update($id);
        }elseif($nomerpenjualan<>""){
            $penjualan->update_by_nomerpenjualan($nomerpenjualan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Penjualan updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Penjualan update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomerpenjualan'])){
            $nomerpenjualan = $_GET['nomerpenjualan'];
        }
        if($id>0){    
            $penjualan->delete($id);
        }elseif($nomerpenjualan>0){
            $penjualan->delete_by_nomerpenjualan($nomerpenjualan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Penjualan deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Penjualan delete failed.';
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