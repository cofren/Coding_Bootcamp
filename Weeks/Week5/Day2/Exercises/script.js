// Exercise 1


// add class = para_article
let newClass = document.querySelectorAll("p");
// console.log(newClass);

for (i=0; i<newClass.length; i++) {
    newClass[i].classList.add("para_article");
}

// // QUESTION: Why does this not work?
// for (let i of newClass) {
//     newClass[i].classList.add("para_article")
// }


// remove last paragraph in article
let last = document.querySelectorAll("p")[3];
last.remove();

// remove h2 when clicked
document.querySelector("h2").addEventListener("click", removeH2);
function removeH2() {
    document.querySelector("h2").remove()
}

// new font size h1
document.querySelector("h1").style.fontSize = "30px";

console.log(document.querySelector("h2"));

// hide first paragraph when clicked
document.querySelector("p").addEventListener("click", hideP)
function hideP() {
    this.style.visibility = "hidden";
}

// get values from inputs and append inside a table
// create attribute "value"
document.querySelectorAll("input")[0].setAttribute("value", "");

let userName = document.querySelectorAll("input")[0].value;
document.write(userName);


// console.log(userName);
// let opinion = document.querySelectorAll("input")[1].value;
// console.log(opinion);

