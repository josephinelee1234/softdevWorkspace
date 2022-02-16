/*
    Team Sheeps :: Josephine Lee, Ivan Lam
    SoftDev pd2
    K30 -- canvas based JS drawing
    2022-02-14
*/
var c = document.getElementById("slate")

var ctx = c.getContext("2d");


var mode = "rect";


var toggleMode = (e) => {
	if (mode === "rect") {
		mode = "circ";
		document.getElementById('buttonToggle').innerHTML = "Circle";
	} else {
		mode = "rect";
		document.getElementById('buttonToggle').innerHTML = "Rectangle";
	}
}

var drawRect = function(e) {
	var mouseX = e.offsetX;
	var mouseY = e.offsetY;
	ctx.beginPath();
	ctx.rect(mouseX, mouseY, 200, 200);
	ctx.fillStyle = '#ff0000'; 
	ctx.fill();
	ctx.stroke();
	console.log("mouseclick registered at ", mouseX, mouseY);
}

var drawCircle = (e) => {
	var mouseX = e.offsetX;
	var mouseY = e.offsetY;
	ctx.beginPath();
	ctx.arc(mouseX, mouseY, 50, 2 * Math.PI, false);
	ctx.fillStyle = '#00ff00';
	ctx.fill();
	ctx.stroke();
	console.log("mouseclick registered at ", mouseX, mouseY);
	
}


var draw = (e) => {
	if (mode === "rect") {
		drawRect(e);
	} else {
		drawCircle(e);
	}
}


var wipeCanvas = () => {
	ctx.clearRect(0, 0, slate.width, slate.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);