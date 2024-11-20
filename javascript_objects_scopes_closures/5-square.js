#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super();
    if (size > 0) {
      this.size = size;
    } else {
      this.size = this.width;
    }
  }
}
module.exports = Square;
