#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the head of the list
 * @number: number to be inserted
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	current = *head;
	if (number < current->n)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
