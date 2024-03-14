#include "list.h"
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	while (current)
	{
		current = current->next;
		if ( current == list)
		{
			return (1);
		}
	}
	return (0);
}
