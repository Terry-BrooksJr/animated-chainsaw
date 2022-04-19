import $ from "https://cdn.skypack.dev/jquery@3.6.0";
//Accessiblity Feature - Dark/HighvContrast Mode
document.addEventListener('DOMContentLoaded', function () {
  var modeSwitch = document.querySelector('.mode-switch');

element=getele
  element.addEventListener('click', function() { /* do stuff here*/ }, false);

function confirmLogOutIntent(){
    $('a#logoutModal').click(function(){
        if(confirm('Are you sure to logout')) {
            return true;
        }
        return false;
    });
});
}

  modeSwitch.addEventListener('click', function () {document.documentElement.classList.toggle('dark');modeSwitch.classList.toggle('active');
  });
  
  //Enabling ToolTips Site Wide
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})



  // var listView = document.querySelector('.list-view');
  // var gridView = document.querySelector('.grid-view');
  // var projectsList = document.querySelector('.project-boxes');
  
  // listView.addEventListener('click', function () {
  //   gridView.classList.remove('active');
  //   listView.classList.add('active');
  //   projectsList.classList.remove('jsGridView');
  //   projectsList.classList.add('jsListView');
  // });
  
  // gridView.addEventListener('click', function () {
  //   gridView.classList.add('active');
  //   listView.classList.remove('active');
  //   projectsList.classList.remove('jsListView');
  //   projectsList.classList.add('jsGridView');
  // });
  
//   document.querySelector('.messages-btn').addEventListener('click', function () {
//     document.querySelector('.messages-section').classList.add('show');
//   });
  
//   document.querySelector('.messages-close').addEventListener('click', function() {
//     document.querySelector('.messages-section').classList.remove('show');
//   });
 });