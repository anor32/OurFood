let left_arrow = document.querySelector(".left-arrow");
let right_arrow = document.querySelector(".right-arrow");

max_slide = 1
let category_sliders =document.querySelectorAll('.category-slider')

let sliders = document.querySelectorAll('.slider')

for (let i = 0; i < sliders.length; i++){
    let sliderCards= sliders[i].querySelectorAll(".slider-card")
    let right_arrow = category_sliders[i].querySelector(".right-arrow")
    let left_arrow = category_sliders[i].querySelector(".left-arrow")
    let current_count = 1;


    right_arrow.addEventListener("click", function() {

        if (current_count != -max_slide) {
           current_count--;
           console.log(current_count)

        sliderCards.forEach(card => {

        card.style.transform = 'translateX('+current_count*880+'px)';
    });
        }
    });

    left_arrow.addEventListener("click", function() {
        console.log(current_count)
        if (current_count <0 ) {
           current_count++;

            sliderCards.forEach(card => {
        card.style.transform = 'translateX('+current_count*880+'px)';
    });
        }
    });

}

window.addEventListener('beforeunload', function() {
        sessionStorage.setItem('scrollPosition', window.scrollY);
});


window.addEventListener('load', function() {
    const scrollPosition = sessionStorage.getItem('scrollPosition');
    if (scrollPosition) {
        window.scrollTo(0, parseInt(scrollPosition));
    }
})