#!/usr/bin/node
// Write a function that converts a number from base 10 to another base passed as argument
exports.converter = function (base) {
  return function (num) {
    // radix - base to use for representing a numeric value. Must be an integer between 2 and 36.
    return num.toString(base);
  };
};
