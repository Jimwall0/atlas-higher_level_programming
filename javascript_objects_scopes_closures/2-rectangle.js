#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w < 1) {
      this.width = {};
    } else {
      this.width = w;
    }
    if (h < 1) {
      this.height = {};
    } eles {
      this.height = h;
    }
  }
}
module.exports = Rectangle;
