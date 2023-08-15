#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the list
 * Return: 1 if not palindrome, 0 if palindrome
 */
int is_palindrome(listint_t **head)
{
    int number_of_nodes;
    int left;
    int right;
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

    left = 0;
    right = number_of_nodes - 1;

    while (right >= number_of_nodes / 2)
    {
        int current_left = 0;
        int current_right = 0;
        int current_left_counter = 0;
        int current_right_counter = 0;
        listint_t *node = *head;

        while (node != NULL)
        {
            if (current_left_counter == left)
            {
                current_left = node -> n;
            }
            if (current_right_counter == right)
            {
                current_right = node -> n;
            }
            current_left_counter++;
            current_right_counter++;
            node = node -> next;
        }

        if (current_left != current_right)
        {
            return 0;
        }

        left++;
        right--;
    }

    return 1;
}
