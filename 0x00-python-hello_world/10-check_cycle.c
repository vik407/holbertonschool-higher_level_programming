#include "lists.h"
/**
 *check_cycle - Write a function in C that checks if a singly linked list has a
 * cycle in it.
 * @list: linked list to be checked
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	/* Need two variables (pointers) to compare */
	listint_t *list_a = NULL, *list_b = NULL;

	/* A list to check is coming? */
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	list_b = list;
	list_a = list_b->next;
	/* Do a loop to check for a cycle */
	while (list_a != NULL && list_a->next != NULL && list_a->next->next != NULL)
	{
		/* is a cycle */
		if (list_a == list_b)
		{
			return (1);
		}
		/* And move the list */
		list_b = list_b->next;
		list_a = list_a->next->next;
	}
	return (0);
}
