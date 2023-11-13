#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const numArray = process.argv.sort((a, b) => a - b);
  console.log(numArray[numArray.length - 2]);
}
