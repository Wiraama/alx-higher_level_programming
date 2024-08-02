#!/usr/bin/node
/*
 * Write a script that prints all characters of a Star Wars movie:
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

if (process.argv.length < 3) {
	process.exit(1);
}

request(url + process.argv[2], (error, response, body) => {
	const film = JSON.parse (body);
	const characters = film.characters;

	if (response.statusCode ===200) {
		for (const character of characters) {
			request(character, (error, response, body1) => {
				if (response.statusCode === 200) {
					const dataOfCharacter = JSON.parse(body1);
					console.log(dataOfCharacter.name);
				}
			});
		}
	}
});
