<?php
$a=exec('sudo python /var/www/html/pi/leds/prende4.py');
echo $a;
header("location: formulario.html");
?>
