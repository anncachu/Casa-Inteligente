<?php
$a=exec('sudo python3 /var/www/html/pi/Proyecto/switch.py '.'4');
echo $a;
header('location: frame1.html');
?>
