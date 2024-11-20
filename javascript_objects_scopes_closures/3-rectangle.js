#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    string = '';
    for (let row in h) {
      for (let column in w) {
        string += 'X'
      }
      console.log(string);
    }
  }
}
module.exports = Rectangle;
