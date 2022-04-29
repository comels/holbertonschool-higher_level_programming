#ifndef __list_h__
#define __list_h__

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct node {
    char c;
    struct node *next;
  } list;

list *add_node_char(list **head, char c);
int check_palind(list *head);

#endif
