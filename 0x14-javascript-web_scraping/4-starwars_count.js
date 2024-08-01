#!/usr/bin/node
/*
 * Write a script that prints the number of movies where the character “Wedge Antilles” is present.
 */

const request = require('request');

if (process.argv.length < 3)
{
	console.log("check on your Usage");
	process.exit(1);
}

const wedge_id = 18;

request(process.argv[2], (error, response, body) => {
	if (error)
	{
		console.log(`Error code ${error} occured`);
		process.exit(1);
	}

	if (response.statusCode === 200) {
		const films = JSON.parse(body).results;
		let count = 0;

		films.forEach(film => {
			film.characters.forEach(character => {
				if (character.includes(`/${wedge_id}/`)) {
					count++;
				}
			});
		});
		console.log(count);
	} else {
		console.log(`Error: ${response.statusCode}`);
	}
	
});
