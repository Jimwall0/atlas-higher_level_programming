#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  } else if (response.statusCode === 200) {
    const movieList = JSON.parse(body);
    let total = 0;
    for (const movie of movieList.results) {
      if (movie.characters.some(characterUrl => characterUrl.includes('18'))) {
        total += 1;
      }
    }
    console.log(total);
  } else {
    console.log('Not found');
  }
});
