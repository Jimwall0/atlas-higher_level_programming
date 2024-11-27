#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  } else if (response.statusCode === 200) {
    const main = JSON.parse(body);
    const results = {};
    for (const temp of main) {
      if (temp.completed === true) {
        if (!results[temp.userId]) {
          results[temp.userId] = 0;
        }
        results[temp.userId] += 1;
      }
    }
    console.log(results);
  } else {
    console.log('fail');
  }
});
