#include "lists.h"
/**
 * insert_node - function that insert new nodd to a list
 * @head: the list
 * @number: number of the newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t));
	listint_t *tmp, *tmp2;
	
	if (newnode == NULL)
		return (NULL);
	
	newnode->n = number;

	tmp = *head;
	while (number > tmp->n)
	{
		tmp2 = tmp;
		tmp = tmp->next;
	}
	tmp2->next = newnode;
	newnode->next = tmp;

	return (newnode);
}
