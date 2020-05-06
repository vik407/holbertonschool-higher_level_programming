#!/usr/bin/node
// A script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const arg = process.argv[2];

if (isNaN(Number(arg))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(arg, 10)}`);
}
