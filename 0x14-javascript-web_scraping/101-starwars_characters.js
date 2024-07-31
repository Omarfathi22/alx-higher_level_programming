#!/usr/bin/node

const request = require('request');

// Get movie ID from command-line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch movie details
request(apiUrl, async (error, response, body) => {
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
  for (const url of characterUrls) {
    try {
      const characterName = await new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err) {
            reject(err);
            return;
          }
          const character = JSON.parse(body);
          resolve(character.name);
        });
      });
      console.log(characterName);
    } catch (err) {
      console.error(err);
    }
  }
});
