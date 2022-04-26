#include "lists.h"
/**
 * insert_node - function that insert new nodd to a list
 * @head: the list
 * @number: number of the newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t));
	listint_t *tmp = *head;
	
	if (newnode == NULL)
		return (NULL);
	
	newnode->n = number;

	if (*head == NULL || number < (*head)->n)
	{
		*head = newnode;
		newnode->next = tmp;
	}
	else
	{
		while (tmp && number > tmp->next->n)
			tmp = tmp->next;

		newnode->next = tmp->next;
		tmp->next = newnode;
	}
	return (newnode);
}
