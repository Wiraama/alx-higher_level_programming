/*
 * Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
 *
 * The translation of “hello” must be displayed in the HTML tag DIV#hello
 * You can’t use document.querySelector to select the HTML tag
 * You must use the JQuery API
 * Your script must work when it is imported from the <head> tag
 */

// Wait for the DOM to be fully loaded
$(document).ready(function() {
	$.ajax({
		url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
		method: 'GET',
		success: function(data) {
			var helloTranslation = data.hello;
			// Display the translation in the <div> with id 'hello'
			$('#hello').text(helloTranslation);
		},
		error: function() {
			$('#hello').text('Failed to retrieve translation.');
		}
	});
});
