var initialData = {
	radius: 150,
	angle: 0,
	angle2: 0,
	size: 1
}

function render(data, ctx){
	var sides1 = 20
	var sides2 = 30
	var a1 = data.angle2 // 0 to pi
	var a2 = data.angle2 // 0 to 2pi
	r1 = 300
	for(var a1=0; a1 < Math.PI; a1 += Math.PI / sides1){
		for (var a2 = 0; a2 < 2*Math.PI; a2 += Math.PI / sides2) {
			ctx.point(r1 * Math.cos( a1) * Math.sin( a2), r1 * Math.sin( a1) * Math.sin( a2), {r:2 + 2*Math.cos( a2 )})
			ctx.point(r1 * Math.cos( a1) * Math.sin( a2), r1 * Math.sin( a1) * Math.sin( a2), {r:1 + 1*Math.cos( a2 ), fill:"yellow"})
		}
	}
}         

g9(initialData, render)
	.align('center', 'center')
	.insertInto('#sphere')
