#!/usr/bin/node
/* script to print
 * My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 */

const number = process.argv.slice(2);
const num = parseInt(number[0]);

if (isNaN) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
