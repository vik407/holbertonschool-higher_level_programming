#!/usr/bin/node
// A script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

const arg = process.argv[2];

if (Number.isInteger(Number(arg))) {
  for (let i = 0; i < Number(arg); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
