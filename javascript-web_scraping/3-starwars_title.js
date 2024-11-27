#!/usr/bin/node
const request = ('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, (err, request, body => {
  if (err) {
    console.log('Error:', err);
  } else if (request.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log('Movie not found or id invalid');
  }
}));
