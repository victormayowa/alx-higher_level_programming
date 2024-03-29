#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf-8', (err, dataA) => {
  if (err) throw err;

  fs.readFile(fileB, 'utf-8', (err, dataB) => {
    if (err) throw err;

    const concatenatedData = dataA + dataB;

    fs.writeFile(fileC, concatenatedData, (err) => {
      if (err) throw err;
      console.log('The files have been concatenated!');
    });
  });
});
