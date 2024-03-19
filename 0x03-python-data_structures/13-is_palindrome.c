#include "lists.h"
#include <stdlib>

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;
	listint_t *f_node = NULL;
	listint_t *c_node = *head;
	listint_t *l_node = NULL;

	/**reversing nodes**/
	while (c_node != NULL)
	{
		l_node = c_node->next;
		c_node->next = f_node;
		f_node = c_node;
		c_node = l_node;
	}

	*head = f_node;

	/** checking and returning palidrome **/
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup  slow->next->next;
			break;
		}
		slow = slow->next;
	}
	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
		{
			return (0);
		}
	}
	if(!dup)
		return (1);
	return (0);
}
