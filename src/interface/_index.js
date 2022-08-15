let capture1 = document.getElementById('capture1');
let capture2 = document.getElementById('capture2');


setInterval(function(){
    document.getElementById('text-iframe').contentWindow.location.reload();
}, 1000)

document.getElementById('form1').addEventListener('submit', (event) => {
    event.preventDefault()
    console.log("camera 1 registered photo action")      
    let signalsModal = document.getElementById("modal");
    signalsModal.style.display = "block";
    window.onclick = function(event) {
        if (event.target == signalsModal) {
            signalsModal.style.display = "none";
        }
    }
    fetch('http://0.0.0.0:9000/photo')
    .then(response => {
        responseJson = response.json().then(data => {
            let index = data['Photo Index']

            // // console.log(data)
            // for(i=0;i<index;i++){
            //     appendHTMLElement1("camera1", index)
            //     finalize()
            // }
            return data;
        })     
        let signalsModal = document.getElementById("modal");
        // var modalBtn = document.getElementById("modalBtn");
        let modalSpan = document.getElementsByClassName("close")[0];
        signalsModal.style.display = "block";
        // signalsModal.style.display = "block";
        window.onclick = function(event) {
            if (event.target == signalsModal) {
                signalsModal.style.display = "none";
            }
        }
    }).catch(response => {
        console.error(response)
    })
})

document.getElementById('form2').addEventListener('submit', (event) => {
    event.preventDefault()
    console.log("camera 2 registered photo action")      
    let signalsModal = document.getElementById("modal");
    signalsModal.style.display = "block";
    window.onclick = function(event) {
        if (event.target == signalsModal) {
            signalsModal.style.display = "none";
        }
    }
    fetch('http://0.0.0.0:10000/photo')
    .then(response => {
        responseJson = response.json().then(data => {
            let index = data['Photo Index']

            // // console.log(data)
            // for(i=0;i<index;i++){
            //     appendHTMLElement1("camera1", index)
            //     finalize()
            // }
            return data;
        })     
        let signalsModal = document.getElementById("modal");
        // var modalBtn = document.getElementById("modalBtn");
        let modalSpan = document.getElementsByClassName("close")[0];
        signalsModal.style.display = "block";
        // signalsModal.style.display = "block";
        window.onclick = function(event) {
            if (event.target == signalsModal) {
                signalsModal.style.display = "none";
            }
        }
    }).catch(response => {
        console.error(response)
    })
})


function onPhotoDisplay(){
    var signalsModal = document.getElementById("modal");
    // var modalBtn = document.getElementById("modalBtn");
    var modalSpan = document.getElementsByClassName("close")[0];
    signalsModal.style.display = "block";
    // signalsModal.style.display = "block";
    window.onclick = function(event) {
        if (event.target == signalsModal) {
            signalsModal.style.display = "none";
            chartDiv.innerHTML = ""
        }
    }
}

function appendHTMLElement1(camera, index){
    var divHead = document.getElementById("divHead")
    var divElementHead = document.createElement("div")
    divElementHead.setAttribute("class", "mySlides fade")
    var divElementChild = document.createElement("div")
    divElementChild.setAttribute("class", "numbertext")
    // innerHTML missing
    var img = document.createElement("img")
    img.setAttribute("src", "/" + camera + "/img" + index + ".png")
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