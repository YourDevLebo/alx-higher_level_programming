#include "lists.h"
#include <stdio.h>

/**
 * add_nodeint - prints new node at the beginning
 * @head: header
 * @n: number of nodes
 * Return: null if failed else address of new element
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}
