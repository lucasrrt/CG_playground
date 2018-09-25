function main(){
	const canvas = document.querySelector("#glCanvas");
	const gl = canvas.getContext("webgl");

	var vertices = [
		-0.5,0.5,0.0,
		0.0,0.5,0.0
		-0.25,0.25,0.0,
	]

	gl.clearColor(0, 0, 0, 1);
	gl.clear(gl.COLOR_BUFFER_BIT)
}

function getShader(gl, id) {
	var shaderScript, theSource, currentChild, shader;

	shaderScript = document.getElementById(id);

	if(!shaderScript) {
		return null;
	}

	theSource = "";
	currentChild = shaderScript.firstChild;

	while(currentCHild) {
		if(currentChild.nodeType == currentChild.TEXT_NODE) {
			theSource += currentChild.textContext;
		}

		currentChild = currentChild.nextSibling;
	}
}

function initShaders() {
	var fragmentShader = getShader(gl, "shader-fs");
	var vertexShader = getShader(gl, "shader-vs");

	// Cria o progrma shader

	shaderProgram = gl.createProgram();
	gl.attachShader(shaderProgram, vertexShader);
	gl.attachShader(shaderProgram, fragmentShader);
	gl.linkProgram(shaderProgram);

	// Se falhar ao criar o progrma shader, alerta

	if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
		alert("Não foi possível inicializar o programa shader.");
	}

	gl.useProgram(shaderProgram);

	vertexPositionAttribute = gl.getAttribLocation(shaderProgram, "aVertexPosition");
	gl.enableVertexAttribArray(vertexPositionAttribute);
}

main();
