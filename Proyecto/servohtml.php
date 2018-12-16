<?php
$a=exec('sudo python3 /var/www/html/pi/Proyecto/servohtml.py '.$_POST['servo']);
echo $a;
header("location: frame1.html");
?>
