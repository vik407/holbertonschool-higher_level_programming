#!/usr/bin/node
// Write a function that returns the reversed version of a list:
exports.esrever = function (list) {
  return list.reduce((accumulator, currentValue) => {
    accumulator.unshift(currentValue);
    return accumulator;
  }, []);
};
