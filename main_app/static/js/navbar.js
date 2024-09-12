// static/recipes/js/navbar.js

let lastScrollTop = 0;
const navbar = document.querySelector('header');

window.addEventListener('scroll', function () {
  let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

  if (currentScroll > lastScrollTop) {
    // Scrolling down, hide navbar
    navbar.style.top = '-100px'; // Adjust as needed based on navbar height
  } else {
    // Scrolling up, show navbar
    navbar.style.top = '0';
  }
  lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // Prevent negative scroll values
});
