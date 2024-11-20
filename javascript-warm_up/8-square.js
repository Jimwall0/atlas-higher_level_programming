#!/usr/bin/node
const square = Number(process.argv[2]);
if (Number.isInteger(square)) {
  for (let h = 0; h < square; h++) {
    let box = '';
    for (let w = 0; w < square; w++) {
      box += 'X';
    }
    console.log(box);
  }
} else {
    console.log('Missing size')
}
