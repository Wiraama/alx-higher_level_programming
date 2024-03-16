#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - main entry point
 * @number: ...
 * @head: ...
 *
 * Return: ...
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
	{
		return (NULL);
	}
	newnode->n = number;
	newnode->next = NULL;

	/** if the list is null its insserted int the begggining **/
	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		(*head) = newnode;
	}
	else
	{
		while (current && current->next && current->next->n < number)
		{
			current = current->next;
		}
		/** insert the new node **/
		newnode->next = current->next;
		current->next = newnode;
	}
	return (newnode);
}
