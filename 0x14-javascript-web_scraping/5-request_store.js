#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  try {
    if (error) {
      throw new Error(`Request failed: ${error.message}`);
    }

    if (response.statusCode === 200) {
      fs.writeFileSync(filePath, body, 'utf-8');
      console.log(`Body content successfully written to ${filePath}`);
    } else {
      throw new Error(`Failed to retrieve webpage data. Status code: ${response.statusCode}`);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
});
