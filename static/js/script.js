sendButton.addEventListener("click", ()=>{
    // alert("hey Script is working")
    question= document.getElementById("question").value;
    document.getElementById("question").value= "";
    document.querySelector(".right2").style.display="block"
    document.querySelector(".right1").style.display="none"


})
