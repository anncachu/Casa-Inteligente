<?php
$a=exec('sudo python /var/www/html/pi/leds/apaga2.py');
echo $a;
header("location: formulario.html");
?>
