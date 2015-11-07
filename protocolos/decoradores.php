<?php
$f =  function() {
  echo("Hola\n");
};

$llamar_dos_veces = function($f) {
    return function() use ($f) {
       $f();
       $f();
    };
};

$f = $llamar_dos_veces($f);
$f();

?>
