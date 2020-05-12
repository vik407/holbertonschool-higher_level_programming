#!/usr/bin/node
// Write a function that prints the number of arguments already printed and the new argument value.
exports.logMe = (function (item) {
  let arg = 0;
  return function (item) {
    // Output format: <number arguments already printed>: <current argument value>
    console.log(`${arg}: ${item}`);
    arg += 1;
  };
}());
