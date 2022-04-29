#include "list.h"
/**
 * main - function principale
 * Return: 0
 */
int main(void)
{
  list *tmp, *head = NULL;
  char *str;

  add_node_char(&head, 'a');
  add_node_char(&head, 'b');
  add_node_char(&head, 'c');
  add_node_char(&head, 'o');
  add_node_char(&head, 'k');
  add_node_char(&head, 'c');
  add_node_char(&head, 'b');
  add_node_char(&head, 'a');

  tmp = head;

  printf("Lancement du check palindrome :\n");
  printf("\nLa liste à checker est :\n\n");
  while(tmp)
  {
	  printf("'%c' ", tmp->c);
	  tmp = tmp->next;
  }
  printf("\n\n...\n\n");
  check_palind(head);

  return (0);
}
