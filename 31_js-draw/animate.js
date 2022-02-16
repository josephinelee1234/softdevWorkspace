/*
    Team Sheeps :: Josephine Lee, Ivan Lam
    SoftDev pd2
    K31 -- JS animation
    2022-02-16
*/

// model for HTML5 canvas-based animation

// SKEELTON

//access canvas and buttons via DOM
var c = document.getElementById("playground");// GET CANVAS
var dotButton = document.getElementById("buttonCircle");// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop");// GET STOP BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");// YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = '#75E6DA' // YOUR CODE HERE

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  // console.log("clear invoked...")
  ctx.clearRect(0, 0, c.width, c.height);
  // YOUR CODE HERE
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
  // console.log("drawDot invoked...")
  clear(event);
  ctx.beginPath();
  ctx.arc((playground.width)/2, (playground.height)/2, radius, 2 * Math.PI, false);
  ctx.fill();
  ctx.stroke();

  if (growing) {
    radius += 1;
  } else {
    radius -= 1;
  }

  if (radius >= playground.width/2) {
    growing = false;
  } else if (radius === 0) {
    growing = true;
  }

  if (requestID) {
    window.cancelAnimationFrame(requestID);
  }
  
  requestID = window.requestAnimationFrame(drawDot);
  
  // YOUR CODE HERE

  /*
    ...to
    Wipe the canvas,
    Repaint the circle,

    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()

   */
};


//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);

  // YOUR CODE HERE
  /*
    ...to
    Stop the animation

    You will need
    window.cancelAnimationFrame()
  */
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );