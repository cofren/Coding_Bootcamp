

var contenedorParrafos = document.getElementsByClassName('flexbox')[0],
left = document.getElementById('left'),
center = document.getElementById('center'),
right = document.getElementById('right');


	left.addEventListener('click', function() {
	contenedorParrafos.style.justifyContent = 'flex-start';
});

center.addEventListener('click', function() {
	contenedorParrafos.style.justifyContent = 'center';
});

right.addEventListener('click', function() {
	contenedorParrafos.style.justifyContent = 'flex-end';
});

