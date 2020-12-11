#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - Function
* @list: parameter
* Return: int
*/

int check_cycle(listint_t *list)
{
	int isOrNot;

	if ((list == NULL) || (list->next == NULL))
	{
		isOrNot = 0;
	}
	else
	{
		isOrNot = 1;  
	}
	return (isOrNot);
}
