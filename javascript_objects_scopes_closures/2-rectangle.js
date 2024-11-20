#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w < 1) {
      this.width = undefined;
    } else {
      this.width = w;
    }
    if (h < 1) {
      this.height = undefined;
    } else {
      this.height = h;
    }
  }
}
module.exports = Rectangle;
