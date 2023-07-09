4 .Create a Node.js application that uses user defined module to find area 
of rectangle and display details on console. 
// rectangle.js 
module.exports = { 
calculateArea: function(length, width) { 
return length * width; 
} 
}; 
// app.js 
const rectangle = require('./rectangle'); 
const length = 5; 
const width = 10; 
const area = rectangle.calculateArea(length, width); 
console.log('Rectangle Details:'); 
console.log(' ----------------- '); 
console.log(`Length: ${length}`); 
console.log(`Width: ${width}`); 
console.log(`Area: ${area}`);