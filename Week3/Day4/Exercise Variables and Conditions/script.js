// Exercise 1

let x = 5;
let y = 2;
if (x>y){
    console.log("x is the bigger then y")
}
else {
    console.log("x is not bigger then y")
}

// Exercise 2

let newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog=="Chihuahua") {
    console.log("I love Ch")
}
else {
    console.log("I dont like Ch")
}
// Exercise 3

let num = prompt("please enter a number");
let check = num % 2;
console.log(check);
if (check==0) {
    alert("even number")
}
else {
    alert("uneven number")
};

// Exercise 4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let number = users.length;
console.log(number);
if (number==0){
    alert("no one is online")
}
else if (number==1){
    alert(users[0] + " is online")
}
else if (number==2){
    alert(users[1] + " and" + users[2] + " are online")
}
else {
    alert(users[0] + ", " + users[1] + " and n-2 more are online")
};