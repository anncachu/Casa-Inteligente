<?php
$a=exec('sudo python /var/www/html/pi/leds/apaga7.py');
echo $a;
header("location: formulario.html");
?>
