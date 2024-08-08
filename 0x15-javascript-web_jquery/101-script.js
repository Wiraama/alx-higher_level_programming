/*
* Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:
*
* The new element must be: <li>Item</li>
* The new element must be added to UL.my_list
* When the user clicks on DIV#add_item: a new element is added to the list
* When the user clicks on DIV#remove_item: the last element is removed from the list
* When the user clicks on DIV#clear_list: all elements of the list are removed
* You can’t use document.querySelector to select the HTML tag
* You must use the JQuery API
* You script must work when it imported from the HEAD tag
*/
$(document).ready(function() {
	/*Add a new <li> element when the user clicks on DIV#add_item*/
	$('#add_item').click(function() {
		var $list = $('.my_list');
		var newItem = $('<li>').text('Item');
		$list.append(newItem);
	});

	/*Remove the last <li> element when the user clicks on DIV#remove_item*/
	$('#remove_item').click(function() {
		var $list = $('.my_list');
		$list.children('li').last().remove();
	});

	/*Clear all <li> elements when the user clicks on DIV#clear_list*/
	$('#clear_list').click(function() {
		var $list = $('.my_list');
		$list.empty();
	});
});
