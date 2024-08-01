#!/usr/bin/node
/*
 * Write a script that gets the contents of a webpage and stores it in a file.
 */

const request = require('request');
const fs = require('fs');

if (process.argv < 4) {
	console.log("Usage: command-line <url>");
	process.exit(1);
}

request(process.argv[2], (error, response, body) => {
	if (error) {
		console.log(`Error ${error} occurred`);
		process.exit(1);
	}

	if (response.statusCode === 200) {
		fs.writeFile(process.argv[3], body, 'utf8', (errors) => {
			if (errors) {
				console.log(`Error ${errors} occured while writting`);
				process.exit(1);
			}
		});
	} else {
		console.log(`Error status code: ${response.statusCode}`);
	}
});
