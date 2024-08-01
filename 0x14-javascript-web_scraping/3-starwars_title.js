#!/usr/bin/node
const request = require('request');
if (process.argv < 3)
{
	console.log("error: Usage: <path> movie id");
	process.exit(1);
}

const movie_id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request(url, (error, response, body) => {
	if (error) {
		console.log("Error: ", error);
		process.exit(1);
	}

	if (response.statusCode === 200) {
		const film = JSON.parse(body);
		console.log(film.title);
	} else {
		console.log(`Error ${process.statusCode}`);
	}
});
