#!/usr/bin/node
// a script that computes and prints a factorial

const a = Number(process.argv[2]);

if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorialize(a));
}

function factorialize (num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * factorialize(num - 1);
  }
}
