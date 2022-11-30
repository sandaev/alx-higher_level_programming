#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: double pointer to sorted linked list
 * @number: value of node to be added
 * Return: address of new node on success, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *next_node, *new_node;

	temp = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
	}
	else if (temp->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}
	else
	{
		while (temp != NULL)
		{
			next_node = temp->next;
			if (next_node->n >= number)
			{
				temp->next = new_node;
				new_node->next = next_node;
				break;
			}
			else if (next_node->next == NULL)
			{
				temp->next->next = new_node;
				break;
			}
			temp = temp->next;
		}
	}
	new_node = *head;

	return (new_node);
}
