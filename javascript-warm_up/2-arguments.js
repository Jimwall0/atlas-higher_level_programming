#!/usr/bin/node
const { argv } = require('node:processs');
if (argv < 1) {
  console.log('No Arguement');
} else if (argv === 1) {
  console.log('Argumenet found');
} else {
  console.log('Arguements found');
}
