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
    } else {
      this.height = h;
    }
  }
}
module.exports = Rectangle;
