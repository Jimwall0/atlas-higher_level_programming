#!/usr/bin/node
const tmp = process.argv[2];
if (Number.isInteger(Number(tmp))) {
  console.log('My number: ' + tmp);
} else {
  console.log('Not a number');
}
