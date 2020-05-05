#!/usr/bin/node
// A script that prints a message depending of the number of arguments passed
const arg = process.argv.length;
if (arg === 2) {
  console.log('No argument');
} else {
  if (arg === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}
