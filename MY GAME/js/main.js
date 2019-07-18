var can1;
var can2;

var ctx1;
var ctx2;

var canvasWidth;

var lastTime;
var deltaTime;

var bgPic = new Image();

var ane;
var fruit;

var mom;
var baby;

var mx;
var my;

var babyTail = []
var babyEye = []
var babyBody = []

var momTail = []
var momEye = []
var momBodyOra = []
var momBodyBule = []

var data;

var wave;

document.body.onload = game;

function game() {
	init();
	lastTime = Date.now();
	deltaTime = 0;
	gameloop();
}

function init() {
	//获得canvas context
	can1 = document.getElementById("canvas1"); //fishes,dust,UI,cirale
	ctx1 = can1.getContext("2d");
	can2 = document.getElementById("canvas2"); //background,one,fruits
	ctx2 = can2.getContext("2d");
	
	can1.addEventListener('mousemove',onMouseMove,false);

	bgPic.src = "./src/background.jpg";

	canWidth = can1.width;
	canHeight = can1.height;
	
	ane = new aneObj();
	ane.init();
	
	fruit = new fruitObj();
	fruit.init();
	
	mom = new momObj();
	mom.init();
	
	baby = new babyObj();
	baby.init();
	
	mx = canWidth*0.5;
	my = canHeight*0.5;

	for(var i = 0;i < 8; i++){
		babyTail[i] = new Image();
		babyTail[i].src = "./src/babyTail" + i + ".png"
	}

	for(var i = 0;i < 2; i++){
		babyEye[i] = new Image();
		babyEye[i].src = "./src/babyEye" + i + ".png"
	}
	for(var i = 0;i < 20; i++){
		babyBody[i] = new Image();
		babyBody[i].src = "./src/babyFade" + i + ".png"
	}

	for(var i = 0;i < 8; i++){
		momTail[i] = new Image();
		momTail[i].src = "./src/bigTail" + i + ".png"
	}

	for(var i = 0;i < 2; i++){
		momEye[i] = new Image();
		momEye[i].src = "./src/bigEye" + i + ".png"
	}
	data = new dataObj();

	for(var i = 0;i < 8; i++){
		momBodyOra[i] = new Image();
		momBodyBule[i] = new Image();
		momBodyOra[i].src = "./src/bigSwim"+i+".png"
		momBodyBule[i].src = "./src/bigSwimBlue"+i+".png"
	}

    ctx1.font = "30px Verdana";
	ctx1.textAlign = "center";
	
	wave = new waveObj();
	wave.init();
}

function gameloop() {
	window.requestAnimationFrame(gameloop); //setInterval,setTimeout
	var now = Date.now();
	deltaTime = now - lastTime;
	lastTime = now;
	if(deltaTime>40) deltaTime = 40;

	drawBackground();
	ane.draw();
	fruitMonitor();
	fruit.draw();
	
	ctx1.clearRect(0,0,canWidth,canHeight);
	mom.draw();
	baby.draw();
	momFruitsCollision();
	momBobyCollision();

	data.draw();
	wave.draw();
}

function onMouseMove(e)
{
	if(!data.gameOver){
		if(e.OffSetX||e.layerX)
		{
			mx = e.offSetX == undefined ? e.layerX : e.offSetX;
			my = e.offSetY == undefined ? e.layerY : e.offSetY;
		}
	}
}