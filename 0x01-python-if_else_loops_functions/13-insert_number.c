#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - Function
* @head: parameter
* @number: parameter
* return: listint_t
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *newObject;

	newObject = (listint_t*)malloc(sizeof(newObject));

	newObject->n = number;
	newObject->next = NULL;

		if (head == NULL)
		{
			head = newObject;
		}
		else
		{
			aux = head;

			while (aux->next != NULL)
			{
				aux = aux->next;
				aux->next = newObject;
			}
		}
		return (head);
}
