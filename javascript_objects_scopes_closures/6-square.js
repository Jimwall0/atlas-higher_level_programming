#!/usr/bin/node
const Square = require('./5-square');

class Square2 extends Square {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;
    for (let row = 0; row < this.size; row++) {
      let string = '';
      for (let column = 0; column < this.size; column++) {
        string += char;
      }
      console.log(string);
    }
  }
}
module.exports = Square2;