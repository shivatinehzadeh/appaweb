
function openNav() {
  document.getElementById("respnavbar").style.width = "100%";
  document.getElementById("open").style.display = "block";
  document.getElementById("slideshow").style.display = "block";
}

function closeNav() {
  document.getElementById("respnavbar").style.width = "0";
    document.getElementById("open").style.display = "block";
    document.getElementById("slideshow").style.display = "block";

}
function show() {

  if ( document.getElementById("socialmedia").className=== "social2")  {
   document.getElementById("socialmedia").className="social";
document.getElementById("socialmedia").style.display = "block";
document.getElementById("btnsocial").style.marginTop = "-25px";


  }
  else{
    document.getElementById("socialmedia").className="social2";
document.getElementById("socialmedia").style.display = "block";
document.getElementById("btnsocial").style.marginTop = "-25px";


  }
}

window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (window.innerWidth > 980) {
    if (currentScrollPos > 70) {
      document.getElementById("animationDiv").className = "khdmt div container";
    }
       if (currentScrollPos > 1150) {
      document.getElementById("blog").className = "blog div container";
    }
  }
  if (window.innerWidth < 980) {
    if (currentScrollPos > 450) {
      document.getElementById("animationDiv").className = "khdmt";
    }
        if (currentScrollPos > 3000) {
      document.getElementById("blog").className = "blog";
    }
  }
    if (currentScrollPos > 250) {
 document.getElementById("goTop").style.display = "block";
  }
  else {
 document.getElementById("goTop").style.display = "none";
  }
}

function register() {
    alert('لطفا وارد سایت شوید')
}


