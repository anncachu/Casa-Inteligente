<?php
$a=exec('sudo python /var/www/html/pi/leds/apaga6.py');
echo $a;
header("location: formulario.html");
?>
