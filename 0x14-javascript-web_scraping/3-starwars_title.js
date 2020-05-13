#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');

const url = `http://swapi.co/api/films/${process.argv[2]}`;
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
