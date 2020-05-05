#!/usr/bin/node
// A script that prints a message depending of the number of arguments passed
const arg = process.argv[2];
if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
