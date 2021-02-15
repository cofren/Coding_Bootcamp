// // Exercise 1
// let lang = prompt("What´s your language bro?");
// console.log(lang);
// switch (lang) {
//     case "French":
//         alert("Bonjour")
//     break;

//     case "English":
//         alert("Hello")
//     break;

//     case "Hebrew":
//         alert("Shalom")
//     break;

//     default:
//         alert("01110011 01101111 01110010 01110010 01111001")
    
// }


// Exercise 2

let grade = prompt("What´s your grade?");
console.log(grade);
if (grade > 90) {
    alert("A")
}

else if (grade <= 90 && grade >=80){
    alert("B")
}


else if (grade <= 80 && grade >=70){
    alert("C")
}

else {
    alert("You suck")
}
// Exercise 3

let str = prompt("Enter a verb");
let len = str.length;
let last3 = str.slice(str.length -3);
console.log(len);
console.log(last3);
if (len < 3){
    alert(str)
}
else if (last3=="ing" && (len > 3 || len ==3)){
    alert(str + "ly")
}

else {
    alert(str + "ing")
}


