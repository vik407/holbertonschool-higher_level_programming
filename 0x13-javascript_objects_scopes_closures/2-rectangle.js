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
}

module.exports = Rectangle;
