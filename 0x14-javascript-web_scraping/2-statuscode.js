#!/usr/bin/node
const request = require('request');
if (process.argv.length < 3) {
	console.log("error on your input");
	process.exit(1);
}
request(process.argv[2], (error, response, body) => {
	if (error)
	{
		console.log("error:", error);
		process.exit(1);
	}
	console.log(`code: ${response.statusCode}`);
});
