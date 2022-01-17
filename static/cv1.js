
function openPDF() {
    var pdf = "SHANI_FREIMAN_CV.pdf";
    window.open(pdf);
}
function openLinkCV(){
    var htmlCV = "cv2.html";
    window.open(htmlCV);
}
function openContactPage(){
    var contact = "cv11.html";
    window.open(contact);
}

function checkAPI(){
    const inputP = document.getElementById("phone");
    if(!inputP.checkValidity()){
        document.getElementById("demo").innerHTML = inputP.validationMessage;
    }else{
        document.getElementById("demo").innerHTML = "Input OK";
    }
}
