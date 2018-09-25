var initialData = {
	radius: 150,
	angle: 0,
	angle2: 0,
	size: 1
}

function render(data, ctx){
	var sides = 15
	for(var i=0; i<sides; i++){
		for (var j = 0; j < sides; j++) {
			var a = data.angle + i/sides * Math.PI * 2
			var a2 = data.angle2 + j/sides *Math.PI;
			var r1 = data.radius
			ctx.point(r1 * Math.cos( a) * Math.sin( a2), r1 * Math.sin( a) * Math.sin( a2), {r:3 + 3*Math.cos( a2 )})
		}
	}
}         

g9(initialData, render)
	.align('center', 'center')
	.insertInto('#sphere')
