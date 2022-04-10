import $ from "https://cdn.skypack.dev/jquery@3.6.0";
//Accessiblity Feature - Dark/HighvContrast Mode
document.addEventListener('DOMContentLoaded', function () {
  var modeSwitch = document.querySelector('.mode-switch');
});

function confirmLogOutIntent() {
  $('a#logoutModal').click(function () {
    if (confirm('Are you sure to logout')) {
      return true;
    }
    return false;
  });
}

modeSwitch.addEventListener('click', function () {
  document.documentElement.classList.toggle('dark'); modeSwitch.classList.toggle('active');
});

//Enabling ToolTips Site Wide
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

function hider(element_id) {
  document.getElementById(element_id).setAttribute("hidden", "");
}
function shower(element_id) {
  document.getElementById(element_id).removeAttribute("hidden", "");
}

function hooverStart() {
  const element = document.getElementById('No-Password');
  element.addEventListener('onmouseover',hider(element));
}
function hooverEnd(){
  const element = document.getElementById('No-Password');
  element.addEventListener('onmouseleave', hider(element));

}

function getDate(){
  let currentYear = new Date().getFullYear(); 
  return currentYear
}