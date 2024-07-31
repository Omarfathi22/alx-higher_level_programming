#!/usr/bin/node

const request = require('request');

// Get movie ID from command-line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch movie details
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

  // Get the list of character URLs
  const characterUrls = movie.characters;

  // Fetch and print each character in the order provided
  characterUrls.forEach((url, index) => {
    request(url, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);

      // Only print "Movie not found" if the list is empty
      if (index === characterUrls.length - 1 && characterUrls.length === 0) {
        console.error('Movie not found');
      }
    });
  });
});
