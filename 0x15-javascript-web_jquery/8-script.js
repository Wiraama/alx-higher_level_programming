/*
 * Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
 *
 * All movie titles must be list in the HTML tag UL#list_movies
 * You can’t use document.querySelector to select the HTML tag
 * You must use the JQuery AP
 */

$(document).ready(function() {
	$ajax({
		url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
		method = 'GET';
		success: function(data) {
			let movies = data.results;
			let films = $('list_movies');
			$films.empty();

			movies.forEach(film) {
				var $li = $('<li'>).text(film.title);
				$films.append($li);
			};
		}
		// you can handle error if you wish
	});
});

