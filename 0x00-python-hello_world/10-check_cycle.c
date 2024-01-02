#include <stdio.h>
#include <stdlib.h>
#include "main.h"

/**
 * check_cycle - checks if a linked list has a cycle or not
 * @list: pointer to the linked list to be checked
 * Return: 1 if cycle exists, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
	{
		return (0);
	}
	fast = list_next;
	slow = list;
	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
		{
			return (0);
		}
		slow = slow->next;
		fast = fast->next->next;

	return (1);
}
