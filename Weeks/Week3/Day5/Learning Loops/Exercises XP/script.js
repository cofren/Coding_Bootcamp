// // Excercise 1

// let color = ["blue", "green", "red"];
//  for (i = 0; i < color.length; i++) {
    
//     console.log("My #" + (i+1) + " choice is " + color[i]);
// }


// let suffix = ["st","nd","rd"]
//  for (i = 0; i < color.length; i++) {
    
//     console.log("My"  + (i+1) + suffix[i] + " choice is " + color[i]);
// }

// // Excercise 2
// console.log("Exercise 2");
// let people = ["Greg", "Mary", "Devon", "James"];
// console.log(people);
// console.log("Remove Greg");
// people.splice(0,1);
// console.log(people);
// console.log("Jason for James");
// people.splice(2,1,"Jason");
// console.log(people);
// console.log("Add Amit");
// people.push("Amit");
// console.log(people);
// console.log("Exit after Jason");

// for (i of people) {
//     if (i == "Jason") {
//     break;
//     }
//     console.log(i);
// }
// console.log("Copy and not Mary and not my Name");
// console.log(people.slice(1,3));

// console.log("Index of Mary");
// console.log(people.indexOf("Mary"))

// console.log("Index of Foo");
// console.log(people.indexOf("Foo"))

// console.log("Variable \"last\"");
// let last = people.length;
// console.log(people[last-1]);

// // Excercise 3

// console.log("Exercise 3 - Repeat the Question");
// let num;
// do {
// num = prompt("Enter a number!");
// }
// while (num < 11);
// console.log("Finally bigger than 10!");

// Excercise 4

// console.log("Exercise 4 - Attendance");

// let guestList = {
//     randy: "Germany",
//     karla: "France",
//     wendy: "Japan",
//     norman: "England",
//     sam: "Argentina"
//   }

//   let name = prompt("Whats your Name?");

//   if (name in guestList) {
//       console.log("Hi! I'm " + name + ", and i'm from " + guestList[name]);
//   }
//   else {
//       console.log("I'm a guest")
//   }
 
// Excercise 5

console.log("Exercise 5 - Family");

let family = {
    carl: "dad",
    jen: "mom",
    lucie: "daugther",
    dori: "son"
};
for (x in family) {
    console.log(x);
};

for (x in family) {
    console.log(family[x]);
};

// Excercise 6

console.log("Exercise 6 - Secret Group");

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let first = [];
for (x of names) {
    first.push(x[0]);
   
};
first.sort();
first = first.join("");
console.log(first);

