<?php
$a=exec('sudo python3 /var/www/html/pi/servo/servohtml.py '.$_POST['servo']);
echo $a;
header("location: servohtml.html");
?>
