#!/usr/bin/node
// Write a script that reads and prints the content of a file.
const fs = require('fs');

fs.readFile(`${process.argv[2]}`, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString('utf8'));
  }
});
