<?php
$a=exec('sudo python /var/www/html/pi/leds/apaga4.py');
echo $a;
header("location: formulario.html");
?>
