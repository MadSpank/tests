const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add("shown")
        } else {
            entry.target.classList.remove("shown")
        }
    })
})

hiddenElements = document.querySelectorAll(".hidden")

hiddenElements.forEach((hiddenElement) => observer.observe(hiddenElement));
// mainWrapper = document.getElementById("mainWrapper");


// container = document.getElementById("container");

// mainWrapper.addEventListener("mouseover", (e) => scrollUp(e));

// function scrollUp(e) {
//     childToAppend = document.createElement("div")
//     childToAppend.id = position
//     childToAppend.classList.add("child");
    
//     if ( position <100) {
//         position += 1;
//         container.appendChild(childToAppend);
//     };
//     console.log('it scrolls');
//     console.log(e);
// }

// function scrollDown(e) {
//     childToDelete = document.getElementById(position);
//     if ( position > 0) {
//         position -= 1;
//         container.removeChild(childToDelete)
//     }
// };

// window.bind('mousewheel', function(event) {
//     if (event.originalEvent.wheelDelta >= 0) {
//         console.log('Scroll up');
//     }
//     else {
//         console.log('Scroll down');
//     }
//     });
