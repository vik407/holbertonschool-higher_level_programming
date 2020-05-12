#!/usr/bin/node
// Write a class Square that defines a square and inherits from Square of 5-square.js:
const importSq = require('./5-square');

class Square extends importSq {
  // Create an instance method called charPrint(c) that prints the rectangle using the character c
  charPrint (c) {
    // If c is undefined, use the character X
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;