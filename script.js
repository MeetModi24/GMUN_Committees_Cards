const toggle = document.getElementById("toggleDark");
const body = document.querySelector("body");

toggle.addEventListener("click", function () {
  this.classList.toggle("bi-moon");
  if (this.classList.toggle("bi-brightness-high")) {
    body.style.background = "white";
    body.style.transition = "2s";
  } else {
    body.style.background = "rgb(6, 6, 117)";
    body.style.transition = "2s";
  }
});
