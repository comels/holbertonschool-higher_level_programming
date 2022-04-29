#include "list.h"
/**
 * add_node_char - function that add a node to a list
 * @head: the list
 * @c: the char of the new node
 */

list *add_node_char(list **head, char c)
{
  list *new = malloc(sizeof(list));;

  if (new == NULL)
    return (NULL);

  new->c = c;

  new->next = *head;
  *head = new;

  return (new);
}
