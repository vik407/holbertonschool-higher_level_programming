#!/usr/bin/node
// Write a script that imports an array and computes a new array.
const { list } = require('./100-data.js');

console.log(list);
// 1*0 / 2*1 / 3*2 / 4*3 / 5*4
console.log(list.map((currVal, index) => currVal * index));
