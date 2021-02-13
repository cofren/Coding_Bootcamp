// https://www.youtube.com/watch?v=VrT3TRDDE4M
// https://www.youtube.com/watch?v=baTwIcyMvh8

// It does not matter if the Regex is build through the Constructor or Literal Method
// It becomes either way a RegEx Object.
// Once it is a RegEx Object 2 Constructor Methods or 6 different String Methods can be used
// Constructor: Regex, Method, String : reConstructor.test(str1))
// String: String, Method, Regex: str1.search(reConstructor))

let reLiteral;
let reConstructor;
let pattern1;
let pattern2;
let flags;
let str;

// Constructor

pattern1 = "\\matchthis$";
pattern2 = "\\w+";
pattern3 = /matchthis/;
pattern4 = "matchthis";
pattern5 = /\d+/;
flags = "i";
str1 = "matchthis";

// Constructor - RegexObjectMethod
reConstructor = new RegExp(pattern4, flags);
console.log(reConstructor.test(str1)) //

// Constructor - StringObjectMethod

// Literal - StringObjectMethod
console.log(str1.search(pattern3))
console.log(str1.search(reConstructor))

console.log(pattern3.exec(str1))

// Use cases

// Validation
pattern = "\\d+";
let phone = "4645411";
reConstructor = new RegExp(pattern,flags);

console.log(reConstructor.test(phone)) //

// Extraction
pattern = "//(david)/ig"
let text = "This is a Text about David. And also David. More David is here. and David"
// reConstructor = new RegExp(pattern,flags);

console.log(text.match(/(david)/ig));
// console.log(text.match(/(david)/ig));


// Method	Description

// Constructor or Literal


// RegExp()
// exec()	Executes a search for a match in a string. It returns an array of information or null on a mismatch.
// test()	Tests for a match in a string. It returns true or false.


// String
// match()	Returns an array containing all of the matches, including capturing groups, or null if no match is found.
// matchAll()	Returns an iterator containing all of the matches, including capturing groups.
// search()	Tests for a match in a string. It returns the index of the match, or -1 if the search fails.
// replace()	Executes a search for a match in a string, and replaces the matched substring with a replacement substring.
// replaceAll()	Executes a search for all matches in a string, and replaces the matched substrings with a replacement substring.
// split()	Uses a regular expression or a fixed string to break a string into an array of substrings.