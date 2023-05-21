// Example POST method implementation:
async function postData(url = "", data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
        headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }

sendButton.addEventListener("click", async ()=>{
    // alert("hey Script is working")
    questionInput= document.getElementById("questionInput").value;
    document.getElementById("questionInput").value= "";
    document.querySelector(".right2").style.display="block"
    document.querySelector(".right1").style.display="none"

    question1.innerHTML = questionInput;
    question2.innerHTML = questionInput;


    // getting the answer & populate it.
    let result= await postData("/api",{"param1":questionInput})
    solution.innerHTML = result.result
})
