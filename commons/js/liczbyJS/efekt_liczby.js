var c = document.getElementById("c");


var ctx = c.getContext("2d");

//making the canvas full screen
c.height = window.innerHeight;
c.width = window.innerWidth;


var losowane_liczby = "10";
losowane_liczby = losowane_liczby.split("");

var font_size = 21;
var kolumny = c.width/font_size; 

var drops = [];

for(var x = 0; x < kolumny; x++)
	drops[x] = 1; 


function draw()
{

	ctx.fillStyle = "rgba(0, 0, 0, 0.08)";
	ctx.fillRect(0, 0, c.width, c.height);
	//var colors = ["#0F0", "rgba(0, 220, 90, 1)"];

	//var colors = ['#1067f5', '#0646af'];
	//var tmp_color = Math.floor((Math.random() * 2) + 0); // *2 jeżeli dwa kolory
	//ctx.fillStyle = colors[tmp_color]; //green text
	ctx.fillStyle ="#0F0"
	//ctx.fillStyle = "#0F0";
	ctx.font = font_size + "px Cern";

	for(var i = 0; i < drops.length; i++)
	{
	
		var text = losowane_liczby[Math.floor(Math.random()*losowane_liczby.length)];
	
		ctx.fillText(text, i*font_size, drops[i]*font_size);
		

		if(drops[i]*font_size > c.height && Math.random() > 0.974)
			drops[i] = 0;
		

		drops[i]++;
	}
}

setInterval(draw, 140);