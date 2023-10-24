#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    function getCharacterName(url) {
      return new Promise((resolve, reject) => {
        request.get(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          } else {
            reject(`Error: ${response.statusCode}`);
          }
        });
      });
    }

    const promises = characterUrls.map(url => getCharacterName(url));

    Promise.all(promises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(error => console.error(error));
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
