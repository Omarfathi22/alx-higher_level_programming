#!/usr/bin/node
const numArg = parseInt(process.argv[2]);

if (isNaN(numArg) || numArg <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numArg; i++) {
    console.log('C is fun');
  }
}
