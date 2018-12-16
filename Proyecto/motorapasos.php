<?php
$a=exec('sudo python3 /var/www/html/pi/Proyecto/motorapasos.py '.$_POST['motor']);
echo $a;
header('location: frame1.html');
?>
