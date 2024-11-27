#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];
request(url, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  } else if (response.statusCode === 200) {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.log('fail');
      }
    });
  } else {
    console.log('Not found');
  }
});
