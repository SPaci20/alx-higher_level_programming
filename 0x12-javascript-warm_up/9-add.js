#!/usr/bin/node
// Prints the addition of 2 integers

function add (a, b) {
  const sum = a + b;
  return sum;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const c = add(a, b);
console.log(c);
