#!/usr/bin/node
// a script that computes and prints a factorial

const a = Number(process.argv[2]);

if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorialize(a));
}

function factorialize (num) {
  var result = num;
  if (num === 0 || num === 1) {
    return 1;
  }
  while (num > 1) {
    num--;
    result *= num;
  }
  return result;
}
