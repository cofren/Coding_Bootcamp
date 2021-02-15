let sentence = "This coding thingy is really not a bad thing to do";
let wordnot = sentence.indexOf("not");
console.log(wordnot);
let wordbad = sentence.indexOf("bad");
console.log(wordbad);
let length = wordbad - wordnot;
console.log(length);
if (wordbad > wordnot){
    let list = sentence.split("");
    console.log(list);
    list.splice(wordnot,length + 4,"g","o","o","d"," ");
    console.log(list);
    list.join("");
    console.log(list);
    
}
else {
    console.log(sentence)
}