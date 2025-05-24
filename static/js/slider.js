; // Select the parent container of all cards
let left_arrow = document.querySelector(".left-arrow");
let right_arrow = document.querySelector(".right-arrow");
let i = 0;
let category_sliders =document.querySelectorAll('.category-slider')

let sliders = document.querySelectorAll('.slider')
//let sliderCards = document.querySelectorAll(".slider-card")

for (let i = 0; i < sliders.length; i++){
    let sliderCards= sliders[i].querySelectorAll(".slider-card")
    let right_arrow = category_sliders[i].querySelector(".right-arrow")
    let left_arrow = category_sliders[i].querySelector(".left-arrow")


    let current_count=0
    right_arrow.addEventListener("click", function() {

        if (i < 10 - 1) {
           current_count--;
           console.log(sliderCards)
        sliderCards.forEach(card => {

        card.style.transform = 'translateX('+current_count*850+'px)'; // Change the property for all cards
    });
        }
    });

    left_arrow.addEventListener("click", function() {
           current_count++;

            sliderCards.forEach(card => {
        card.style.transform = 'translateX('+current_count*920+'px)'; // Change the property for all cards
    });

    });

}