#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
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
	if (!list)
		return (0);

	list_b = list;
	list_a = list_b->next;
	/* Do a loop to check for a cycle */
	do {
		/* is a cycle */
		if (list_a == list_a)
			return (1);
		/* And move the list */
		list_a = list_a->next->next;
		list_b = list_b->next;
	} while (list_a && list_a->next);

	return (0);
}
