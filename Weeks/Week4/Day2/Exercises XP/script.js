// // Exercise 1

// console.log("Exercise 1: Keyless Car");
// function checkDriverAge(age) {
//     if (age < 18) {
//         alert("Your too young!")
//     }
//     else if (age > 18) {
//         alert("Your old enough")
//     }
//     else {
//         alert("Congrats on your first year of driving!")
//     }
// }
// checkDriverAge(92);


// // Exercise 2

// console.log("What's in my wallet ?");
// let whatYouHave;
// let enough;
// function changeEnough([quarters,dimes,nickels,pennies],sum) {
//     whatYouHave=quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01;
//     if (whatYouHave>=sum) {
//         enough=true
//     }
//     else {
//         enough=false
//     }
// }

// changeEnough([25, 20, 5, 0], 4.25);
// console.log(enough);
// changeEnough([2, 100, 0, 0], 14.11);
// console.log(enough);
// changeEnough([0, 0, 20, 5], 0.75)
// console.log(enough);


// // Exercise 3
// // i could not figure out, how to make the for statement stop automatically once it reaches 500
// console.log("Find the multiples of 23");

// let array=[];
// let newElement;
// function multiple(num) {
//     for (i=1; i<22; i++) {
//         let newElement = num*i;
//         console.log(newElement);
//         array.push(newElement);
        
//     }
//     return array;
// }
// const newArray = multiple(23);
// console.log(newArray);


// let sumOfArray = function(array) {
//    return array.reduce(function(a,b){
//     return a+b
//    },0)
// }
// sum = sumOfArray(newArray);
// console.log(sum);


// Exercise 4
// i did not figure out how to use the "in" keyword
// console.log("Amazon Shopping");

// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }

// let checkBasket = function() {
//     let whatItem = prompt("What item do you want?");
//     let afterCheck = whatItem;
//     return afterCheck
// }

// let result = checkBasket();
// console.log(result);

// Exercise 5

console.log("Shopping List");

let shoppingList = ["banana","orange","apple"]

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 