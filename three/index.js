var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(
	75,
	window.innerWidth / window.innerHeight,
	0.1,
	1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
renderer.setClearColorHex( 0x000000, 1 );
document.body.appendChild( renderer.domElement );


var geometry = new THREE.SphereGeometry( 1.5,32,32);
var material = new THREE.MeshBasicMaterial( { color: 0xffff00 } );
var sphere = new THREE.Mesh( geometry, material );
scene.add( sphere );

camera.position.z = 5;

var animate = function () {
	requestAnimationFrame( animate );

	//cube.rotation.x += 0.01;
	//cube.rotation.y += 0.01;

	renderer.render( scene, camera );
};

animate();
