/*
 * Doubly Linked List:
 *  Seeing if I remember how to build an application using Doubly Linked Lists.
 *
 *  Author: Corwin Brown
 *  Date: 5/27/2016
 */

#include<stdio.h>
#include<stdlib.h>
#include "doublyLinkedList.h"

struct node
{
    struct node *prev;
    int info;
    struct node *next;
};

int main ()
{
    struct node *start = NULL;
    int choice, data, x, k;

     start = createList(start);

    while(1)
    {
        printf("\n");
        printf("1.  Display list.\n");
        printf("2.  Count the number of nodes.\n");
        printf("3.  Search for an element.\n");
        printf("4.  Insert in empty list / Insert in beginning of the list.\n");
        printf("5.  Insert a node at the end of the list.\n");
        printf("6.  Insert a node before a specified node.\n");
        printf("7.  Insert a node after a specified node.\n");
        printf("8.  Insert a node at a given position.\n");
        printf("9.  Delete a node.\n");
        printf("10. Reverse the list.\n");
        printf("11. Quit.\n\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 11)
        {
            printf("Goodbye!\n");
            break;
        }
        
        switch(choice)
        {
            case 1:
                displayList(start);
                break;
            case 2:
                countNode(start);
                break;
            case 3:
                printf("\nEnter the number to search for: ");
                scanf("%d", &data);
                search(start, data);
                printf("\n");
                break;
            case 4:
                printf("\nEnter data to insert at beginning: ");
                scanf("%d", &data);
                start = insertInBeginning(start, data);
                displayList(start);
                break;
            case 5:
                printf("\nEnter data to insert at end of list: ");
                scanf("%d", &data);
                insertAtEnd(start, data);
                displayList(start);
                break;
            case 6:
                printf("\nEnter the data to insert: ");
                scanf("%d", &data);
                printf("Enter the node to insert \"%d\" before: ", data);
                scanf("%d", &x);
                //start = insertBefore(start, data, x);
                displayList(start);
                break;
            case 7:
                printf("\nEnter the data to insert: ");
                scanf("%d", &data);
                printf("Enter the node to After \"%d\" before: ", data);
                scanf("%d", &x);
                //insertAfter(start, data, x);
                displayList(start);
                break;
            case 8:
                printf("\nEnter the data to insert: ");
                scanf("%d", &data);
                printf("\nEnter the position to insert at: ");
                scanf("%d", &x);
                //start = insertAtPosition(start, data, x);
                displayList(start);
                break;
            case 9:
                printf("\nEnter element to delete (NOTE: if repeated, first one found will be removed): ");
                scanf("%d", &data);
                //start = deleteNode(start, data);
                displayList(start);
                printf("\n");
                break;
            case 10:
                //start = reverseList(start);
                displayList(start);
                break;
        }
    }

    return 0;
}

void displayList(struct node *start)
{
    struct node *p;
    if (start == NULL)
    {
        printf("List is empty\n");
        return;
    }

    p = start;
    printf("List is:\n");
    while (1)
    {
        printf("%d -> ", p->info);
        p = p->next;
        if (p == NULL)
            break;
    }

    printf("\n");
}


struct node *createList(struct node *start)
{
    int nodeCount, number;

    printf("Enter the number of nodes: ");
    scanf("%d", &nodeCount);

    if (nodeCount < 1)
    {
        return start;
    }

    for(int i = 0; i < nodeCount; i++)
    {
        if (i == 0)
        {
            printf("Enter the first number: ");
            scanf("%d", &number);
            start = createNode(number, NULL, NULL);
            if (start == NULL)
                return NULL;
        }
        else
        {
            printf("Enter the next number: ");
            scanf("%d", &number);
            insertAtEnd(start, number);
        }
    }

    return start;
}

struct node *createNode(int data, struct node *prev, struct node *next)
{
    struct node *newNode;

    newNode = (struct node *)malloc(sizeof(struct node));
    if (newNode == NULL)
        return NULL;

    newNode->prev = prev;
    newNode->info = data;
    newNode->next = next;

    return newNode;
}

void insertAtEnd(struct node *start, int data)
{
    struct node *p, *temp;

    // Create new node.
    temp = createNode(data, NULL, NULL);
    if (temp == NULL)
        return;

    // Traverse the list
    p = start;
    while(p->next != NULL)
    {
        p = p->next;
    }
    temp->prev = p;
    p->next = temp;
}

void countNode(struct node *start)
{
    struct node *p;
    int count = 0;

    p = start;
    while(p != NULL)
    {
        count++;
        p = p->next;
    }
    printf("\n\nCount: %d\n\n", count);
}

void search(struct node *start, int data)
{
    struct node *p;
    int count = 0;

    p = start;
    while(p != NULL)
    {
        count ++;
        if (p->info == data)
            break;
        p = p->next;
    }
    printf("\n\nItem located at index: %d\n\n", count);
}

struct node *insertInBeginning(struct node *start, int data)
{
    struct node *p, *temp;

    if (start == NULL)
    {
        start = createNode(data, NULL, NULL);
    }
    else
    {
        temp = createNode(data, NULL, start);
        start->prev = temp;
        start = temp;
    }
    return start;
}

struct node *insertAtPosition(struct node *start, int data, int x)
{}
