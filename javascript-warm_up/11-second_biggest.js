#!/usr/bin/node
const args = [];
for (let i = 2; i < process.argv.length; i++) {
  args.push(parseInt(process.argv[i], 10));
}

if (args.length <= 1) {
  console.log(0);
} else {
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const num of args) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }

  console.log(secondLargest === -Infinity ? 0 : secondLargest);
}
