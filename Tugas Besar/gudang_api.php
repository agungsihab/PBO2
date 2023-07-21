<?php
require_once 'database.php';
require_once 'Gudang.php';
$db = new MySQLDatabase();
$gudang = new Gudang($db);
$id=0;
$nomergudang=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomergudang'])){
            $nomergudang = $_GET['nomergudang'];
        }
        if($id>0){    
            $result = $gudang->get_by_id($id);
        }elseif($nomergudang>0){
            $result = $gudang->get_by_nomergudang($nomergudang);
        } else {
            $result = $gudang->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new gudang
        $gudang->nomergudang = $_POST['nomergudang'];
        $gudang->kodebarang = $_POST['kodebarang'];
        $gudang->nama_barang = $_POST['nama_barang'];
        $gudang->stok_barang = $_POST['stok_barang'];
       
        $gudang->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Gudang created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Gudang not created.';
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
        if(isset($_GET['nomergudang'])){
            $nomergudang = $_GET['nomergudang'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $gudang->nomergudang = $_PUT['nomergudang'];
        $gudang->kodebarang = $_PUT['kodebarang'];
        $gudang->nama_barang = $_PUT['nama_barang'];
        $gudang->stok_barang = $_PUT['stok_barang'];
        if($id>0){    
            $gudang->update($id);
        }elseif($nomergudang<>""){
            $gudang->update_by_nomergudang($nomergudang);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Gudang updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Gudang update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomergudang'])){
            $nomergudang = $_GET['nomergudang'];
        }
        if($id>0){    
            $gudang->delete($id);
        }elseif($nomergudang>0){
            $gudang->delete_by_nomergudang($nomergudang);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Gudang deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Gudang delete failed.';
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