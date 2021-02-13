// Hangman Game

console.log("Hangman-Game");

// Enter a word (exactly 8 letters) and display it and display it as stars (*).

// declare global variables

let hiddenWord;
let wordArray;
let wordLength;
let letter;
let regGuess;
// let regConstructor = new RegExp(regPattern, "g, i")


// prompt word 8 letter
function askWord () {
        hiddenWord = prompt("Enter your secret word. At least 8 letters.");
        wordLength = hiddenWord.length;
       
}

// check if 8 letters
function checkLetters () {
        while ( wordLength < 8) {
                hiddenWord = prompt("Your word needs to be at least 8 letters long. Please enter again");
                wordLength = hiddenWord.length;
                wordArray = hiddenWord.split("");
        }
}

// display word as stars
function stars() {
        console.log("*".repeat(wordLength));
}


// Player 2 guess letters
function guess () {
        letter = prompt("Please guess a letter");
}


// Check if letter in hidden word
regPattern = "/"+guess+"/"


askWord();
checkLetters();
stars();
guess();



console.log(hiddenWord);
console.log(wordLength);

// check if 8 letters. if not prompt again

// Guess a letter. 10 guesses max. Wrong guess 1 life less



// Check if letter in word
// Check if letter was already used
// If letter in word, change the or that star(s) to the letter.
// If letter not in word show all letters that wrongly guessed


// log success/failure


