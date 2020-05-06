#!/usr/bin/node
// A function that executes x times a function.
exports.callMeMoby = (num, func) => {
  for (let i = 0; i < num; i++) {
    func();
  }
};
