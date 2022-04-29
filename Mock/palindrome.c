#include "list.h"
/**
 * check_palind - function that check if the list is a palindrome
 * @head: the list to check
 */
int check_palind(list *head)
{
  int i = 0, j = 0, k;
  list *tmp = head, *tmp2 = head;

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
      printf("La liste précédente n'est pas un palyndrome\n");
      return (0);
    }
    tmp2 = tmp2->next;
  }
  printf("La liste précédente est un palyndrome\n");
  return (0);
}
