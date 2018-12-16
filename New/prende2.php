<?php
$a=exec('sudo python /var/www/html/pi/leds/prende2.py');
echo $a;
header("location: formulario.html");
?>
