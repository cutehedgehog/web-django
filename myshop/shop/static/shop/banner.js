const banners = document.querySelectorAll('.banner');
let currentIndex = 0;

const storedInterval = localStorage.getItem('bannerInterval');
let interval = storedInterval ? parseInt(storedInterval) : 5000; 

function rotateBanners() {
  banners[currentIndex].classList.remove('active');
  const randomIndex = Math.floor(Math.random() * banners.length);
  currentIndex = randomIndex !== currentIndex ? randomIndex : (currentIndex + 1) % banners.length;
  banners[currentIndex].classList.add('active');
}

let rotationInterval = setInterval(rotateBanners, interval);
const intervalInput = document.getElementById('interval');
intervalInput.value = interval / 1000;

const confirmBtn = document.getElementById('confirmBtn');
confirmBtn.addEventListener('click', function () {
  interval = parseInt(intervalInput.value) * 1000;
  localStorage.setItem('bannerInterval', interval);
  clearInterval(rotationInterval);
  rotationInterval = setInterval(rotateBanners, interval);
});

let isPageFocused = true;

window.addEventListener('focus', function () {
  isPageFocused = true;
  rotationInterval = setInterval(rotateBanners, interval);
});

window.addEventListener('blur', function () {
  isPageFocused = false;
  clearInterval(rotationInterval);
});
