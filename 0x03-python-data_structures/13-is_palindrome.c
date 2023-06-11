#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head node of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr, *fast_ptr, *prev_slow_ptr;
	listint_t *second_half, *mid_node;
	int is_palindrome = 1;

	slow_ptr = fast_ptr = *head;
	prev_slow_ptr = NULL;
	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		if (fast_ptr != NULL)
		{
			mid_node = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		second_half = slow_ptr;
		prev_slow_ptr->next = NULL;
		reverse_list(&second_half);
		is_palindrome = compare_lists(*head, second_half);
		reverse_list(&second_half);
		if (mid_node != NULL)
		{
			prev_slow_ptr->next = mid_node;
			mid_node->next = second_half;
		}
		else
			prev_slow_ptr->next = second_half;
	}
	return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer of the head node of the linked list
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *prev_node, *current_node, *next_node;

	prev_node = NULL;
	current_node = *head;
	while (current_node != NULL)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}
	*head = prev_node;
}

/**
 * compare_lists - compares two linked lists for equality
 * @head1: pointer to the head node of the first linked list
 * @head2: pointer to the head node of the second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}
