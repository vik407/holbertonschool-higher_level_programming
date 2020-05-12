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

  // Create an instance method called rotate() that exchanges the width and the height of the rectangle
  rotate () {
    const __width = this.width;
    this.width = this.height;
    this.height = __width;
  }

  // Create an instance method called double() that multiples the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
