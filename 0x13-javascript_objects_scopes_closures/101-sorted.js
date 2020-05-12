#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const { dict } = require('./101-data');

console.log(Object.entries(dict).reduce((currVal, currIndex) => {
  !currVal[currIndex[1]]
    ? currVal[currIndex[1]] = [currIndex[0]]
    : currVal[currIndex[1]].push(currIndex[0]);
  return currVal;
}, {}));
