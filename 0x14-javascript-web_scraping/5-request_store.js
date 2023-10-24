#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];
request.get(url, (error, response, body) => {
  if (error) console.log(error);
  fs.open(file, 'w', (error, fd) => {
    if (error) console.log(error);
    fs.write(fd, body, 'utf8', (error) => {
      if (error) console.log(error);
    });

    fs.close(fd, (error) => {
      if (error) console.log(error);
    });
  });
});
