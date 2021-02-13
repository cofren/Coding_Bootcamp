var newParagraph = document.createElement('p');

var newText = document.createTextNode('Hello, I am a new text');

newParagraph.appendChild(newText);

newParagraph.setAttribute('class', 'text');

// // -------------------------------------------

var paragraphs = document.getElementsByClassName('text');

var parentParagraphs = paragraphs[0].parentNode;

console.log(parentParagraphs);


// // Replacing an element
// // 

//parentParagraphs.replaceChild(newParagraph, paragraphs[2]);


// // Deleting an element

//parentParagraphs.removeChild(paragraphs[0]);



