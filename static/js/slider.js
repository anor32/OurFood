let numbers = ["num1.jpg", "num2.jpg", "num3.jpg"];
let sliderCard = document.querySelector(".slider-card");
let left_arrow = document.querySelector(".left-arrow");
let right_arrow = document.querySelector(".right-arrow");
let i = 0;

right_arrow.addEventListener("click", function() {
  console.log('click');

  if (i < numbers.length - 1) { // Проверка, чтобы не выйти за пределы массива
    i++;
    sliderCard.style.transform = `translate(${-100 * i}px)`; // Используйте шаблонные строки
    updateArrows();
  }
});

left_arrow.addEventListener("click", function() {
  i--

  sliderCard.style.transform = `translate(${100 * i}px)`;

  updateArrows();

})


function updateArrows() {
  if (i <=0) {
    left_arrowSvg.style.opacity = "0.2"
  }
  else if (i === 2) {
    right_arowSvg.style.opacity = "0.2"
  }
  else if (i > 0 && i < 2) {
    left_arrowSvg.style.opacity = "1"
    right_arrowSvg.style.opacity = "1"

  }



}