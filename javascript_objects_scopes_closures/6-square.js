#!/usr/bin/node

const Square = require('./5-square');

class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let row = 0; row < this.size; row++) {
      let string = '';
      for (let column = 0; column < this.size; column++) {
        if (c) {
          string += c;
        } else {
          string += 'X';
        }
      }
      console.log(string);
    }
  }
}
module.exports = Square;
