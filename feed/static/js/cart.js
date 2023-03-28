var cart = [];

function addToCart(id, name, image, price, discount, discountedPrice) {
  var item = {
    id: id,
    name: name,
    image: image,
    price: price,
    discount: discount,
    discountedPrice: discountedPrice
  };
  cart.push(item);
  localStorage.setItem('cart', JSON.stringify(cart));
  updateCartCount();
}

function updateCartCount() {
  var cartCount = document.getElementById('cart-count');
  cartCount.innerHTML = cart.length;
}

function loadCart() {
  var cartData = localStorage.getItem('cart');
  if (cartData !== null) {
    cart = JSON.parse(cartData);
    updateCartCount();
  }
}

loadCart();

var addToCartButtons = document.getElementsByClassName('add-to-cart-btn');
for (var i = 0; i < addToCartButtons.length; i++) {
  addToCartButtons[i].addEventListener('click', function() {
    var id = this.getAttribute('data-id');
    var name = this.getAttribute('data-name');
    var image = this.getAttribute('data-image');
    var price = this.getAttribute('data-price');
    var discount = this.getAttribute('data-discount');
    var discountedPrice = this.getAttribute('data-discounted-price');
    addToCart(id, name, image, price, discount, discountedPrice);
  });
}
