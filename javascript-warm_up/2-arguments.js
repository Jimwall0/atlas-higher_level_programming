#!/usr/bin/node
const len = process.argv.length;
if (len < 3) {
  console.log('No Arguement');
} else if (len === 3) {
  console.log('Argumenet found');
} else {
  console.log('Arguements found');
}
