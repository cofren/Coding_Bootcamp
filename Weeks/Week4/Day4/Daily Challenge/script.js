// Daily Challenge 99 Bottles of Beer

// Ask user to enter the no. of bottles

let number = prompt("How many bottles of Beer?");

let falling = 1;
let newNumber = number;
console.log(newNumber + " bottles of beer on the wall");
console.log(newNumber + " bottles of beer");
console.log("Take " + falling + " down, pass it around");

while (newNumber > falling) {
    newNumber = newNumber - falling
    falling = falling + 1;
    console.log(newNumber + " bottles of beer on the wall");
    console.log(newNumber + " bottles of beer");
   
    if (newNumber > falling) {
        console.log("Take " + falling + " down, pass them around");
    } 
    else {
        console.log("Not enough bottles on beer on the wall to take down!")}
}

