<?php
$foco = 5;
$file = "switch.py";
$command = escapeshellcmd("python3 ../../python/$file $foco");
exec($command, $output);
echo json_encode($output);
?>
