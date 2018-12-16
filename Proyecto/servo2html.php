<?php
$a=exec('sudo python3 /var/www/html/pi/Proyecto/servo2html.py '.$_POST['servo']);
echo $a;
header("location: frame1.html");
?>
