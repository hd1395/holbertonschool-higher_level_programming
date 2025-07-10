#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);

if (isNaN(num1) || isNaN(num2)) {
  console.log('Arguments must be integers');
} else {
  console.log(add(num1, num2));
}
