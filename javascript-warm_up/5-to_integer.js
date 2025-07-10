#!/usr/bin/node
const num = process.argv[2];
const parsed = parseInt(num, 10);

if (isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsed}`);
}
