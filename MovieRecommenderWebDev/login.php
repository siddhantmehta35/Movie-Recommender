<?php


$servername = "localhost";
$username = "root";
$password = "";
$dbname= "userdb";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
$uname=$_GET["username"];
$pw=$_GET["password"];


$query=" SELECT * FROM userdb where uname='$uname' and pass='$pw'";
$result = $conn->query($query);
/*if ($result->num_rows > 0) {
	$_SESSION["username"]=$uname;
    header('location:login.html');
}
else
{	
    header('location:homepage.php');
}*/
if(mysqli_num_rows($result)==0) {
    header('Location: http://localhost/wp/login.html');
}
while($row=mysqli_fetch_assoc($result))
{
session_start();
$_SESSION["username"]=$uname;
header('Location: http://localhost/wp/homepage.html');
}



?>
