#!/usr/bin/node
function add (a, b) {
  if (Number.isInteger(a)) {
    if (Number.isInteger(b)) {
      const total = a + b;
      console.log(total);
    } else {
      console.log('NaN');
    }
  } else {
    console.log('NaN');
  }
}

add(Number(process.argv[2]), Number(process.argv[3]));
