#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const sortedArgs = args.map(Number).sort((a, b) => a - b);
  const secondLargest = sortedArgs[sortedArgs.length - 2];
  console.log(secondLargest);
}
