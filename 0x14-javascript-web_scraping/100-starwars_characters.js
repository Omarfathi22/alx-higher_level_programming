#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  if (movie.detail && movie.detail === 'Not found') {
    console.error('Movie not found');
    return;
  }

  const characterUrls = movie.characters;

  characterUrls.forEach(url => {
    request(url, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
