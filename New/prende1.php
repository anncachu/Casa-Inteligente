<?php
$a=exec('sudo python /var/www/html/pi/leds/prende1.py');
echo $a;
header("location: formulario.html");
?>
