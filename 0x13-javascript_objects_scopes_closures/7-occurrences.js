#!/usr/bin/node
// Write a function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((accumulator, currentValue) => {
    if (currentValue === searchElement) {
      accumulator++;
    }
    return accumulator;
  }, 0);
};
