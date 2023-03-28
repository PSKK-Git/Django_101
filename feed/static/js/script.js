$(document).ready(function() {

  // services click panna footer ku povum
  // Get the "Services" link
const servicesLink = document.querySelector('nav ul li:nth-child(3) a');

// Get the footer section
const footerSection = document.querySelector('footer');

// Add a click event listener to the "Services" link
servicesLink.addEventListener('click', (event) => {
  // Prevent the default link behavior
  event.preventDefault();
  
  // Scroll smoothly to the footer section
  footerSection.scrollIntoView({ behavior: 'smooth' });
});

  // This JavaScript code will add an event listener to each menu item and toggle the "active" class when the user clicks on it. The "active" class will add an underline to the menu item, and it will stay underlined until the user clicks on a different menu item.
  const currentLocation = location.href;
  const menuItem = document.querySelectorAll('a');
  const menuLength = menuItem.length;
  for (let i = 0; i < menuLength; i++) {
    if (menuItem[i].href === currentLocation) {
      menuItem[i].classList.add('active');
    }
    // Add the following code
    else {
      menuItem[i].classList.remove('active');
    }
  }

  //end
  
  
  
  
  // js for new navbar
  // Get the current page URL
var currentURL = window.location.href;

// Get all the menu items
var menuItems = document.querySelectorAll('nav a');

// Loop through the menu items
for (var i = 0; i < menuItems.length; i++) {
  
  // Check if the menu item URL matches the current page URL
  if (menuItems[i].href === currentURL) {
    
    // Add the 'active' class to the menu item
    menuItems[i].classList.add('active');
    
    // Exit the loop
    break;
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