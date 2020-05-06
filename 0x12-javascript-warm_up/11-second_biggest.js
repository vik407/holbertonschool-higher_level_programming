#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.

const a = process.argv.length;

if (a <= 3) {
  console.log(0);
} else {
  const nums = process.argv.slice(2);
  nums.sort((a, b) => a - b);
  console.log(Number(nums[nums.length - 2]));
}
