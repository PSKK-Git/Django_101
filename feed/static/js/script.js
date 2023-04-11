$(document).ready(function() {


 
  
  // search products
  const searchIcon = document.querySelector(".fa-search");
const searchInput = document.querySelector("input[type='text']");

searchIcon.addEventListener("click", function() {
  if (searchInput.style.display === "none") {
    searchInput.style.display = "block";
  } else {
    searchInput.style.display = "none";
  }
});



  
  
  
  
  // js for new navbar
// Get the current page URL
var currentURL = window.location.href;

// Get all the menu items
var menuItems = document.querySelectorAll('nav a');

// Loop through the menu items
for (var i = 0; i < menuItems.length; i++) {
  
  // Check if the menu item URL matches the current page URL or contains the path to the products page
  if (menuItems[i].href === currentURL || currentURL.indexOf('/products') > -1) {
    
    // Add the 'active' class to the menu item
    menuItems[i].classList.add('active');
    
  } else {
    
    // Remove the 'active' class from the menu item
    menuItems[i].classList.remove('active');
  }
}



  // end js for new navbar

// full page
  $(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});

  $(".option").click(function(){
    $(".option").removeClass("active");
    $(this).addClass("active");
    
 });
//  end
   $('.my-div a').click(function(e) {
     e.preventDefault();
     $(this).toggleClass("clicked");
   });
 
   $('.my-div a').blur(function() {
     $(this).removeClass("clicked");
   });
 });

 