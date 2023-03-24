$(document).ready(function() {
   $('.my-div a').click(function(e) {
     e.preventDefault();
     $(this).toggleClass("clicked");
   });
 
   $('.my-div a').blur(function() {
     $(this).removeClass("clicked");
   });
 });