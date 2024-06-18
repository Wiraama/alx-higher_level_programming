#!/usr/bin/node
/* print 2 argument passed with is */

const args = process.argv.slice(2);

console.log(args[0] + ' is ' + args[1]);
