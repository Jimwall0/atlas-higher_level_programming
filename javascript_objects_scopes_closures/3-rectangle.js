#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let string = '';
      for (let column = 0; column < this.width; column++) {
        string += 'X';
      }
      console.log(string);
    }
  }
}
module.exports = Rectangle;
