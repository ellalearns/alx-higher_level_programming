#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
    int number_of_nodes;
    listint_t *current_node;

    if (*head == NULL)
    {
        return 1;
    }

    number_of_nodes = 0;
    current_node = *head;

    while (current_node != NULL)
    {
        number_of_nodes++;
        current_node = current_node -> next;
    }

    if (number_of_nodes % 2 != 0)
    {
        return 0;
    }
}
