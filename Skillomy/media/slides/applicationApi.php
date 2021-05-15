<<?php 



$servername = "localhost";
$username = "root";
$password = "";
$dbname = "student";

// Database connection
$conn = new mysqli($servername, $username, $password, $dbname);


if($_SERVER['REQUEST_METHOD']=='POST'){

//Getting post data 
$id = $_POST['id'];

$name = $_POST['name'];

$country = $_POST['country'];

$contact = $_POST['contact'];

if($name == '' || $username == '' || $password == '' || $email == ''){


echo 'please fill all values';

        }else{

$contents = file_get_contents('jsonfile.json');
$json = json_decode($contents, true);
$user = array_search($username, array_column( $json, 'username' ) );

if( $user !== False ) 
$json[] = array("id" => $id,"name" => $name, "country" => $country, "contact" => $contact) ;
else
$json[] = array("id" => $id,"name" => $name, "country" => $country, "contact" => $contact) ;

$json = json_encode($json);

file_put_contents('jsonfile.json', $json);
}
}else{
echo "error";

}





 ?>