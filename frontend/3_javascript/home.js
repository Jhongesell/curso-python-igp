//alert('hola');

//console.log($);

$(function(){
	console.log('Nuevo Hola');

	$('button#btnAccion1').click(function(){
		$('#lblAccion1').html('Click!!');
	});

	$('#btnNuevaFila').on('click',function(){
		$('.frmMultiple').append('<div class="fila"><input /><a class="btnBorrar">X</a></div>')
		borrarFn();
	});


	borrarFn = function(){
		$('.btnBorrar').on('click',function(){
			//console.log();
			$(this).parent().slideUp();


		});
	};

	borrarFn();


});

