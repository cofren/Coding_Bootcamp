// Welcome
let bodyTag = document.querySelector("body");
bodyTag.style.fontFamily = "Helvetica";

let divHello = document.createElement("div");
divHello.setAttribute("id", "hello");
divHello.style.cssText = "font-size: 30px; color: black; background-color: lightgray";
let welcomeText = document.createTextNode("Hello and Welcome to your JS Playground! This website is 100% JS!!!");
divHello.appendChild(welcomeText);
bodyTag.appendChild(divHello);

let lineBreak = document.createElement("br");
bodyTag.appendChild(lineBreak);



// Loop

// Repeat a text x-times
bodyTag.appendChild(document.createTextNode("Repeat a text x-times"));

    // Create Form
let form = document.createElement("Form");

    // Text Input
let input1Label = document.createTextNode("Text to repeat:")
form.appendChild(input1Label);
let input1 = document.createElement("input");
input1.setAttribute("id","input1")
input1.setAttribute("type","text");
input1.setAttribute("name","what");
form.appendChild(input1);

    // No. of Repeat Input
let input2Label = document.createTextNode("Number of Repeat:");
form.appendChild(input2Label);
let input2 = document.createElement("input");
input2.setAttribute("id","input2")
input2.setAttribute("type","repeat");
input2.setAttribute("name","howOften");
form.appendChild(input2);
form.appendChild(lineBreak);

    // Button
let button = document.createElement("input");
button.setAttribute("id", "button")
button.setAttribute("type","button");
button.setAttribute("value","Click to Submit")
form.appendChild(button);

    // Append form to Body
bodyTag.appendChild(form);

    // show result
bodyTag.appendChild(document.createTextNode("Here are the result:"));
let result = document.createElement("div")
result.setAttribute("id","resultDiv")
bodyTag.appendChild(result);


// take input from form and display
let userInput = document.querySelector("#button");
userInput.addEventListener("click", saveAndDisplay);

function saveAndDisplay() {
    let text = document.getElementById("input1").value;
    let number = document.getElementById("input2").value;
    for (i=1; i<=number; i++) {
        let para = document.createElement("p");
        para.setAttribute("id","result"+i)
        let resultText = document.createTextNode(text);
        para.appendChild(resultText);
        console.log(para);
        result.appendChild(para);
    }
}
