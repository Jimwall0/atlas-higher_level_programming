#!/usr/bin/node
const tmp = Number(process.argv[2]);
if (Number.isInteger(tmp)) {
  for (let x = 0; x < tmp; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
