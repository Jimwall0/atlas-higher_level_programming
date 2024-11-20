#!/usr/bin/node
function second (array) {
  let largest = 1;
  let second = 1;
  for (const x of array) {
    if (x > largest) {
      second = largest;
      largest = x;
    } else if (x > second && x !== largest) {
      second = x;
    }
  }
  return second;
}
const argv = process.argv.slice(2).map(Number);
const len = argv.len;
if (len < 2) {
  console.log(1);
} else {
  console.log(second(argv));
}
