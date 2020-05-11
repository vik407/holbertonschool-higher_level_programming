#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
class Rectangle {
  // class methods
  constructor (_width, _heigh) {
    // constructor get width and height
    if (isNaN(_width) || isNaN(_heigh) ||
        _width <= 0 || _heigh <= 0) {
      return;
    }
    this.width = _width;
    this.height = _heigh;
  }

  // Create an instance method called print() that prints the rectangle using the character X
  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
}

module.exports = Rectangle;
