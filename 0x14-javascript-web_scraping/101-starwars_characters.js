#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie
const request = require('request');

const req = (arr, i) => {
  if (i === arr.length) { return; }
  request(arr[i], (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      req(arr, i + 1);
    }
  });
};

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(body).characters;
    req(chars, 0);
  }
});
