#!/usr/bin/node
const fs = require('fs');

const filename = 'cisfun';

fs.readFile(filename, 'utf-8', (err, data) => {
	if (err)
	{
		console.log("nothing found");
	}
	else
		console.log(data);
});
