<?php
$movie=$_GET["movie"];
file_put_contents("test.txt",$movie);
$result=exec("python3 recc.py \"C:\xampp\htdocs\WP\recc.py\"");
$title=exec("python3 title.py \"C:\xampp\htdocs\WP\title.py\"");
/*$rm=file_get_contents("finalrm.txt");
$arr= explode('&',$rm);*/
header('Location: http://localhost/wp/rpage.php');
?>