#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
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
