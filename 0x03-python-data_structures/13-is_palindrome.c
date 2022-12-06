#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * copy_list - copies a singly linked list
 * @head: double pointer to list
 *
 * Return: pointer to copy of list
 */
listint_t *copy_list(listint_t *head)
{
	listint_t *temp, *tmp;
	listint_t *list_copy, *node;

	temp = head;
	list_copy = malloc(sizeof(listint_t));
	if (list_copy == NULL)
	{
		return (NULL);
	}
	list_copy->n = temp->n;
	list_copy->next = NULL;
	temp = temp->next;
	while (temp != NULL)
	{
		node = malloc(sizeof(listint_t));
		if (node == NULL)
		{
			return (NULL);
		}
		node->n = temp->n;
		node->next = NULL;
		tmp = list_copy;
		if (tmp->next == NULL)
		{
			tmp->next = node;
		}
		else
		{
			for (; tmp->next != NULL; )
			{
				tmp = tmp->next;
			}
			tmp->next = node;
		}
		node = tmp;
		temp = temp->next;
	}
	tmp = list_copy;
	return (list_copy);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to linked list
 *
 * Return: 1 if head is apalindrome; 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *prev;
	listint_t *next;
	listint_t *list_copy;
	listint_t *temp;

	current = *head;
	temp = *head;
	list_copy = copy_list(temp);
	prev = NULL;
	next = NULL;
	/* reverse list */
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	/* treverse and compare */
	for (; prev != NULL; )
	{
		if (prev->n != list_copy->n)
		{
			return (0);
		}
		prev = prev->next;
		list_copy = list_copy->next;
	}
	return (1);
}
