#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const [, , sourceFileA, sourceFileB, destinationFile] = process.argv;

// Read the contents of the source files
const contentA = fs.readFileSync(sourceFileA, 'utf8');
const contentB = fs.readFileSync(sourceFileB, 'utf8');

// Concatenate the contents
const concatenatedContent = `${contentA}${contentB}`;

fs.writeFileSync(destinationFile, concatenatedContent);

console.log(`Files ${sourceFileA} and ${sourceFileB} were successfully concatenated to ${destinationFile}`);
