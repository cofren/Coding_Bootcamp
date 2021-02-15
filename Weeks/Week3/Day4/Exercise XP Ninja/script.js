// // // Exercise 1
// console.log("Exercise 1");


// // // Exercise 2
// console.log("Exercise 2 - ZipCodes");
// let reg = /\d{5}/;
// let zip = prompt("Enter your 5 digit ZipCode");
// if (reg.test(zip)) {
//     console.log("good")
// }
// else {
//     console.log("bad")
// }

// // Exercise 3
console.log("Exercise 3 - Secret Word");
let word = prompt("Please enter a word!");
let rege = /[a,e,i,o,u]/g;
console.log(word.replace(rege,""))
