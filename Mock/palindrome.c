/**
void rotate(char *s)
{
  int i;
  int size = strlen(s);
  char c;

  if (s == NULL)
    return;

  for(i = 0; i < size - 1; i++)
  {
    c = s[size - 2 - i];
    s[size - 2 - i] = s[size - 1 - i];
    s[size - 1 - i] = c;
  }
  printf("%s\n", s);
}

int main(void)
{
  char str[] = "bonjour";
  rotate(str);
  return (0);
}
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node {
    char c;
    struct node *next;
  } list;

list *add_node_char(list **head, char c)
{
  list *new;

  new = malloc(sizeof(list));

  if (new == NULL)
    return (NULL);

  new->c = c;
  new->next = *head;

  *head = new;

  return (new);
}

int palyin(list *head)
{
  int i = 0, j = 0, k;
  list *tmp = head;
  list *tmp2 = head;

  while (tmp->next->next)
  {
    tmp = tmp->next;
    i++;
  }
  k = i / 2;
  if (i % 2 != 0)
    j--;
  for(; j < k + 1; j++)
  {
    tmp = head;
    for(i = k * 2; i - j != 0; i--)
    {
      tmp = tmp->next;
    }
    
    if (tmp->next->c != tmp2->c)
    {
      printf("La liste n'est pas un palyndrome\n");
      return (0);
    }
    tmp2 = tmp2->next;
  }
  printf("La liste est un palyndrome\n");
  return (0);
}

int main(void)
{
  list *head = NULL;

  add_node_char(&head, 'a');
  add_node_char(&head, 'b');
  add_node_char(&head, 'c');
  add_node_char(&head, 'o');
  add_node_char(&head, 'k');
  add_node_char(&head, 'c');
  add_node_char(&head, 'b');
  add_node_char(&head, 'a');

  printf("Lancement du check palyndrome...\n");
  printf("\n");


  palyin(head);

  return (0);
}
