#!/usr/bin/node
// a script that prints a square

const arg = process.argv[2];

if (Number.isInteger(Number(arg))) {
  const size = Number(arg);
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
