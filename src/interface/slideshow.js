var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

function appendHTMLElement(imgPath){
    var divHead = document.getElementById("divHead")
    var divElementHead = document.createElement("div")
    divElementHead.setAttribute("class", "mySlides fade")
    var divElementChild = document.createElement("div")
    divElementChild.setAttribute("class", "numbertext")
    // innerHTML missing
    var img = document.createElement("img")
    img.setAttribute("src", imgPath)
    img.setAttribute("style", "width: 100%")
    var divLast = document.createElement("div")
    divLast.setAttribute("class", "text")
    // divLast.innerHTML = 

    divElementHead.appendChild(divElementChild)
    divElementHead.appendChild(img)
    divElementHead.appendChild(divLast)

    divHead.appendChild(divElementHead)

}

function finalize(){
    var divHead = document.getElementById("divHead")
    var aPrev = document.createElement("a")
    var aNext = document.createElement("a")
    aPrev.setAttribute("class", "prev")
    aPrev.setAttribute("onclick", "plusSlides(-1)")
    aPrev.innerHTML = "&#10094"
    aNext.setAttribute("class", "next")
    aNext.setAttribute("onclick", "plusSlides(1)")
    aNext.innerHTML = "&#10095"

    divHead.appendChild(aPrev)
    divHead.appendChild(aNext)
}

// console.log(fs.readdirSync("../scripts/camera1"))

// appendHTMLElement("img3.jpg")
// appendHTMLElement("img2.png")
// appendHTMLElement("img3.jpg")
