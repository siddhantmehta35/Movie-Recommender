<?php

session_start();
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

$username=$_GET["username"];
$name=$_GET["name"];
$password=$_GET["password"];
$email=$_GET["email"];

$sql="INSERT INTO Userdb(uname,names,pass,email) VALUES('$username','$name','$password','$email')";
if ($conn->query($sql) === TRUE) {
    header('location:login.html');
}
else
{
	header('location:register.html');
}



$conn->close();
?>
