#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18; // Wedge Antilles' character ID

request(apiUrl, (error, response, body) => {
  try {
    if (error) {
      throw new Error(`Request failed: ${error.message}`);
    }

    if (response.statusCode === 200) {
      const filmsData = JSON.parse(body).results;
      const count = filmsData.reduce((acc, film) => {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          return acc + 1;
        }
        return acc;
      }, 0);

      console.log(count);
    } else {
      throw new Error(`Failed to retrieve films data. Status code: ${response.statusCode}`);
    }
  } catch (parseError) {
    console.error(`Error parsing JSON: ${parseError.message}`);
  }
});
