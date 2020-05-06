#!/usr/bin/node
// A function that increments and calls a function.
exports.addMeMaybe = (num, func) => {
  func(num + 1);
};
