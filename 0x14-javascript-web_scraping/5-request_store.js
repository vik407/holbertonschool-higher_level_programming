#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');

request(`${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const _body = body;
    fs.writeFile(`./${process.argv[3]}`, _body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
