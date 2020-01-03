// If scrolled, change background color of the nav.
window.onscroll = () => {
   if (window.scrollY >= 70) {
       document.querySelector("#nav_container").style.backgroundColor = "black";
   }
   else {
     document.querySelector("#nav_container").style.backgroundColor = "transparent";
   }
};

// Functions to validate form submissions
function validate_pizza_cart(){

}
