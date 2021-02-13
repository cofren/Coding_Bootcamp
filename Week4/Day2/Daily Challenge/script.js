// Exercise Mini-Project
let calcDisplay = document.getElementById('display')
console.log(calcDisplay);
let calcString = ("");

// receive numbers and symbols

function my_f(button) {
    // console.log(button);
    calcString = calcString + button;
    calcDisplay.innerHTML = calcString;
    console.log(calcString);
}

function result () {
    let calcResult = eval(calcString);
    console.log(calcResult);
    calcDisplay.innerHTML = calcResult;
}



// hints: use new function called "results" when you click on the "=" sign in the calculator"