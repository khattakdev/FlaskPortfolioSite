//js for the hamburger menu
const menuIcons = document.querySelectorAll("#hamburger");
const side = document.getElementById("side");
var menuEnabled = false;
menuIcons.forEach( (t) => t.addEventListener("click", (ev) => {
	console.log("got hit" )
  if (menuEnabled) {
    side.style.left = "-100%";
    menuEnabled = false;
  } else {
    side.style.left = "0";
    menuEnabled = true;
	}
}))
