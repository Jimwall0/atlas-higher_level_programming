#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
if (process.argv[2] === undefined) {
  console.log(1);
} else {
  console.log(factorial(process.argv[2]));
}
