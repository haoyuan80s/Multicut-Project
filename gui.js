
var myAutoplay;
var i = 1
var autoplaying = false;
function myfirst() {
    document.getElementById("iter" + i).style = "display: none;"
    document.getElementById("iter" + 1).style = ""
    i = 1
}
function mylast() {
    document.getElementById("iter" + i).style = "display: none;"
    document.getElementById("iter" + MAX).style = ""
    i = MAX
}
function myprev() {
    if (i > 1) {
        document.getElementById("iter" + i).style = "display: none;"
        document.getElementById("iter" + (i - 1)).style = ""
        i = i - 1
    }
}
function mynext() {
    if (i < MAX) {
        document.getElementById("iter" + i).style = "display: none;"
        document.getElementById("iter" + (i + 1)).style = ""
        i = i + 1
    }
}
function autoplay() {
    if (autoplaying == false) {
        myAutoplay = setInterval(mynext, 100);
        autoplaying = true;
    }else{
    	myfirst()	    
    }
}
function stopautoplay() {
    clearInterval(myAutoplay);
    autoplaying = false;
}

