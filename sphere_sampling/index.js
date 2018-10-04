var initialData = {
	radius: 150,
	angle: 0,
	angle2: 0,
	size: 1
}

function render(data, ctx){
	var sides1 = 50
	var sides2 = 30
	var a1 = 0 // 0 to pi
	var a2 = 0 // 0 to 2pi
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


function render2(data, ctx){
	var sides1 = 50
	var sides2 = 30
	var a1 = 0 // 0 to pi
	var a2 = 0 // 0 to 2pi
	r1 = 300
	for(var a1=0; a1 < Math.PI; a1 += Math.PI / sides1){
		for (var a2 = 0; a2 < 2*Math.PI; a2 += Math.PI / sides2) {
			ctx.point(r1 * Math.cos( a1) * Math.sin( a2), r1 * Math.cos( a2), {r:2 + 2*Math.sin(a1)*Math.sin( a2 )})
			ctx.point(r1 * Math.cos( a1) * Math.sin( a2), r1 * Math.cos( a2), {r:1 + 1*Math.sin(a1)*Math.sin( a2 ), fill:"yellow"})
		}
	}
}         

g9(initialData, render2)
	.align('center', 'center')
	.insertInto('#sphere2')


function render3(data, ctx){
	var sides1 = 100
	var sides2 = 100
	var a1 = 0 // 0 to pi
	var a2 = 0 // 0 to 2pi
	r1 = 300
	for(var a1=0; a1 < Math.PI; a1 += Math.PI / sides1){
		for (var a2 = 0; a2 < 2*Math.PI; a2 += Math.PI / sides2) {
			ctx.point(r1 * Math.cos( a1) * Math.sin( a2), r1 * Math.sin( a1) * Math.sin( a2), {r:1})
		}
	}
}         

g9(initialData, render3)
	.align('center', 'center')
	.insertInto('#sphere3')


function render4(data, ctx){
	var sides1 = 100
	var sides2 = 100
	var a1 = 0 // 0 to pi
	var a2 = 0 // 0 to 2pi
	r1 = 300
	for(var a1=0; a1 < Math.PI; a1 += Math.PI / sides1){
		for (var a2 = 0; a2 < 2*Math.PI; a2 += Math.PI / sides2) {
			ctx.point(r1 * Math.sin( a1) * Math.cos( a2), r1 * Math.sin( a2), {r:1})
		}
	}
}         

g9(initialData, render4)
	.align('center', 'center')
	.insertInto('#sphere4')
