<?php
$foco = 8;
$file = "switch.py";
$command = escapeshellcmd("python3 ../../python/$file $foco");
exec($command, $output);
echo json_encode($output);
?>
