#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, request) => {
  if (err) {
    console.log("Error:", err);
  } else {
    console.log("code:", request.statusCode);
  }
});
