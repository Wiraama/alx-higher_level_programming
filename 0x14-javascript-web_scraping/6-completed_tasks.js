#!/usr/bin/node
/*
 * Write a script that computes the number of tasks completed by user id.
 */

const request = require('request');

if (process.argv.length < 3) {
	console.log("Usage: ./script <url>");
	process.exit(1);
}

request(process.argv[2], (error, response, body) => {
	if (error) {
		console.log(`Error: ${error}  occured`);
		process.exit(1);
	}

	if (response.statusCode === 200) {
		const todos = JSON.parse(body);
		const count = {};

		todos.forEach(todo => {
			if (todo.completed) {
				if (!count[todo.userId]) {
					count[todo.userId] = 0;
				}
				count[todo.userId] += 1;
			}
		});
		Object.keys(count).forEach(userId => {
			console.log(`'${userId}': ${count[userId]}`);
		});
	}
});
