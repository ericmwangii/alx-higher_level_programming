#include "lists.h"
#include <stdlib.h>

/**
 * listint *insert_node - inserts a number into as sorted linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: number to be iinserted
 * Return: address of the new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current;
listint_t *previous;

current = *head;
previous = NULL;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = number;
new->next = NULL;

if (*head == NULL)
*head = new;
else
{
while (current != NULL && current->n < number)
{
previous = current;
current = current->next;
}
if (previous == NULL)
{
new->next = *head;
*head = new;
}
else
{
previous->next = new;
new->next = current;
}
}
return (new);
}
