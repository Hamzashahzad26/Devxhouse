const menuToggle = document.querySelector('.menu-burger');
const menuItems = document.querySelector('.menu-items');

menuToggle.addEventListener('click', () => {
  menuItems.classList.toggle('show');
  console.log("hello")
});

document.addEventListener('click', (event) => {
    const isClickInside = menuToggle.contains(event.target) || menuItems.contains(event.target);
    if (!isClickInside && menuItems.classList.contains('show')) {
      menuItems.classList.remove('show');
    }
  });




/* aniamte omg up and down */
// Optional: Adjust the animation duration in milliseconds
const animationDuration = 900; // 5 seconds

const image = document.querySelector('.image-container img');
image.style.animationDuration = animationDuration + 'ms';
