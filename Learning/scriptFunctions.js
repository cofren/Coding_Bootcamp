//FUNCTIONS

//DECLARING
// function myFunction(name, age) {

//     console.log("My name is " + name + " my age is " + age);
// }

// // //INVOKING or CALL
// myFunction('Isaac', 80);

// //Reuse
// myFunction("Sarah", 22);
// myFunction("Ben", 40);



// FUNCTIONS WITHOUT PARAMETERS

// Declare the function
// function greet (){

// 	alert('Hello World');

// }


// // // Execute the function
// greet();




// FUNCTIONS WITH PARAMETERS

// function sum(number1, number2){

//     var result = number1 + number2;

// 	console.log(result);

// }

// sum(21, 4);
// sum(10, 5);
// sum(5, 9);


//UNDEFINES (because dont ask her age)

// function myFunction(name, age) {

//     console.log("My name is " + name + " my age is "  + age) // age undefined 
// }

// myFunction("Sarah")



// Default values:
// function userInfo(name, age = 20) {
//     console.log("My name is " + name + " my age is "  + age) // age 20
// }

// userInfo("Sarah")








// Exercise 1
// 1. Create a structured html file linked to a js file

// 2. Write a JS function that takes a parameter: myAge

// 3. Console.log the age of my mum and my dad (my mum is twice my age, and my dad is 1.2 the age of my mum)

// 4. Call the function


// Solution:
// function myFunc(myAge){

//     console.log('My mom is ' + myAge*2 + ' and my dad is ' + (myAge*2)*1.2);

// }

// myFunc(28);




// FUNCTIONS WITH RETURN

// function sum(number1, number2){

//     var result = number1 + number2;

// 	return result;

// }

// console.log(sum(1, 2));



// function myFunction(name, age) {

//     var result = "My name is " + name + " my age is "  + age 

//     return result;
// }

// var girl = myFunction("Sarah", 22)

// console.log(girl) // girl  = result



// function myFunction(name, age) {

//     if (name == "Sarah") {

//         var result = "Hey " + name 

//         return result 

//     } else {

//         return "You are not the right person";
//     }
// }

// var girl = myFunction("Sarah", 22)

// console.log(girl) // girl  = Hey Sarah



//RETURN WILL STOP THE FUNCTION

// Every function in JavaScript returns undefined unless otherwise specified. 
// When a function returns a value, 
// it's returning a result The return value is "returned" back to the "caller" of the function


// function myFunction(name, age) {

//     var result = "My name is " + name + " my age is "  + age 

//     return "hey";

//     return result ;
// }


// var girl = myFunction("Sarah", 22);

// console.log(girl) // girl  = "hey";



// function myFunction(name, age) {

//     if (name != "Sarah") {

//         return;

//         return 'oh its that person again';
//     } 

//     alert ("You are not the right person");
// }

// var girl = myFunction("Isaac", 22)

// console.log(girl) // girl  = undefined




// Exercise 2
// 1. Create a structured html file linked to a js file

// 2. Write a JS function that takes a parameter: myAge

// 3. Return the age of my mum (my mum is twice my age)

// 4. Call the function

// 5. Console.log the age of my mum


// Solution:
// function myFunc(myAge){

//     return 'My mom is ' + myAge*2;

// }

// console.log(myFunc(28));






// SCOPE
// Scope refers to the visibility of variables. In other words, 
// which parts of your program can see or use it. Normally, 
// every variable has a global scope. 
// Once defined, every part of your program can access a variable.


//LOCAL VARIABLE


// function myFunction(name, age) {

//     var eye_color = "blue";

//     console.log("My name is " + name + " my age is "  + age + " I have " + eye_color + " eyes");
// }

// myFunction("Sarah", 22)

// console.log(eye_color) // undefined



// Local Variable - Declared inside a function

// function sayGooobye(){

// 	var saygooobye = 'Bye, see you later';

// 	alert(saygooobye);

// }

// //sayGooobye();

// console.log(saygooobye);



//GLOBAL

// Global Variable - Declared outside of a function

// var message = 'Hello, I am a variable';

// function greet (){

// 	alert(message);
// }

// //greet();

// console.log(message);



// var eye_color = "blue"

// function myFunction(name, age) {

//     console.log("My name is " + name + " my age is "  + age + " I have " + eye_color + " eyes")
// }

// myFunction("Sarah", 22);

// console.log(eye_color) // blue





////setInterval(function, time in milliseconds);

var secondHand = 0;


// function count(){

//     secondHand++;

//     console.log(secondHand);

// }

// count();



// setInterval(function(){

//     secondHand++;

//     console.log(secondHand);

// }, 3000);



// The Other way

// function func(){
//     console.log("Run")
//   }

// setInterval(func, 1000) //Runs the "func" function every second







//setTimeout(funcion, time in milliseconds);

// var text = 'Hello World';

// setTimeout(greet, 5000);

// function greet() {

//     console.log(text);
// }


//Countdown Example
// var timeleft = 10;
// var downloadTimer = setInterval(function(){
//   if(timeleft <= 0){
//     clearInterval(downloadTimer);
//     document.getElementById("countdown").innerHTML = "Finished";
//   } else {
//     document.getElementById("countdown").innerHTML = timeleft + " seconds remaining";
//   }
//   timeleft -= 1;
// }, 1000);





// Arrow Functions:


// Function Expression
// var funcName = function (parameters) {
//     // statement to execute

//   }

// funcName(arguments)

//Example:
// var funcName = function (name) {

//     // statement to execute
//     console.log('Hello', name);

//   }

// funcName('Isaac')



// ES6 Arrow Function:

// Syntax
// const funcName = () => {
//    statement to execute
// }

//Example:
// const show = (name, age) => {
//     console.log(name, age);
// }

// show("Sarah",20) 


// 1 Line Function
// Arrow functions allow you to have an implicit return 
//values are returned without having to use the return keyword.

//const show = (x, y) => x + y
//const show = (x, y) => x * y
//const show = x => x *2

//Example
//const show = (x, y) => x + y
//console.log(show(2, 5));





// Variables:

//Global scope
// function sayHello(){
//     var name = "Sarah"
// }
// console.log(name) // undefined


//The Problem Of The Keyword Var
// var age = 20

// if (age > 18) {
//     var canDrive = true 
//     console.log(canDrive); // true
// } 
// console.log(canDrive);  // true


//Redeclaration
// var name = "Sarah"
// var name = "Dan"
// console.log(name);  // "Dan"  



// The Solution With Of The Keyword Let
// Support Block Scope
// let age = 20

// if (age > 18) {
//     console.log(age) // 20
//     let canDrive = true 
//     console.log(canDrive); // true
// } 
// console.log(canDrive); //ReferenceError: canDrive is not defined


//Doesn’t Allow Redeclaration But The Variable Can Be Changed
// let name = "Sarah"
// let name = "Dan" // SyntaxError: Identifier 'name' has already been declared

// name = "David"
// console.log(name)


// The Solution With Of The Keyword Const
// Support Block Scope
// let age = 20

// if (age > 18) {
//     const canDrive = true 
//     console.log(canDrive); // true
// } 
// console.log(canDrive);  // ReferenceError: canDrive is not defined


//Doesn’t Allow Redeclaration And The Variable Can’t Be Changed
// const name = "Sarah"
// name = "David" // TypeError: Assignment to constant variable.


//Play
//What's the Difference Between var, let and const in JavaScript?
//https://alligator.io/js/var-let-const/




//String And Variable Concatenation (Template Strings):

//1st Way
// let name = "Lea"
// let greetings = "Hello "+ name
// console.log(greetings)

//2nd Way
// let name = "Lea"
// let greetings = `Hello ${name}`;
// console.log(greetings)



// The Keyword This

// let person= {
//     firstName : "Sarah",
//     eye_color: "blue",
//     eat : function () {
//         console.log("My name is " + this.firstName + " I love chocolate")
//     }
// }

//person.eat()

//console.log(Object.keys(person));
//console.log(Object.values(person));





