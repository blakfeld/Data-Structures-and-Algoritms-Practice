/* 
 * Linked List:
 *  Seeing if I remember how to build an application using Linked Lists.
 *
 *  Author: Corwin Brown
 *  Date: 4/24/2016
 */

#include<stdio.h>
#include<stdlib.h>
#include "linkedlist.h"

struct node
{
    int info;
    struct node *link;
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
            break;
        
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
                start = insertBefore(start, data, x);
                displayList(start);
                break;
            case 7:
                printf("\nEnter the data to insert: ");
                scanf("%d", &data);
                printf("Enter the node to After \"%d\" before: ", data);
                scanf("%d", &x);
                insertAfter(start, data, x);
                displayList(start);
                break;
            case 8:
                printf("\nEnter the data to insert: ");
                scanf("%d", &data);
                printf("\nEnter the position to insert at: ");
                scanf("%d", &x);
                start = insertAtPosition(start, data, x);
                displayList(start);
                break;
            case 9:
                printf("\nEnter element to delete (NOTE: if repeated, first one found will be removed): ");
                scanf("%d", &data);
                start = deleteNode(start, data);
                displayList(start);
                printf("\n");
                break;
            case 10:
                start = reverseList(start);
                displayList(start);
                break;
        }
    }

    return 0;
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
            start = createNode(number, NULL);
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


struct node *createNode(int data, struct node *link)
{
    struct node *newNode;

    newNode = (struct node *)malloc(sizeof(struct node));
    if (newNode == NULL)
        return NULL;

    newNode->info = data;
    newNode->link = link;

    return newNode;
}

void insertAtEnd(struct node *start, int data)
{
    struct node *p, *temp;

    temp = createNode(data, NULL);
    if (temp == NULL)
        return;

    // Traverse to end.
    p = start;
    while(p->link != NULL)
    {
        p = p->link;
    }

    p->link = temp;
}

void displayList(struct node *start)
{
    struct node *p;

    printf("\n");

    // Traverse.
    p = start;
    while(1)
    {
        printf("%d -> ", p->info);
        if (p->link == NULL)
            break;
        p = p->link;
    }

    printf("END\n");
}

void countNode(struct node *start)
{
    struct node *p;
    int count = 1;

    // Traverse!
    p = start;
    while(p->link != NULL)
    {
        count++;
        p = p->link;
    }

    printf("\n\nCount: %d\n\n", count);
}

void search(struct node *start, int data)
{
    struct node *p;
    int found = 0;
    int count = 1;

    p = start;
    while(1)
    {
        if (p->info == data)
        {
            found = 1;
            break;
        }

        if(p->link == NULL)
            break;

        count++;
        p = p->link;
    }

    if (found <= 0) {
        printf("Did not find an element with data of: \"%d\"", data);
    }
    else
    {
        printf("Found element \"%d\" at position \"%d\"", data, count);
    }
}

struct node *deleteNode(struct node *start, int data)
{
    struct node *p, *temp;

    if (start == NULL)
    {
        printf("List is empty\n");
        return start;
    }

    // Deletion of first node
    if (start->info == data) {
        temp = start;
        start = start->link;
        free(temp);

        return start;
    }

    p = start;
    while(p->link != NULL)
    {
        if (p->link->info == data) {
            break;
        }
        p = p->link;
    }

    if (p->link == NULL)
    {
        printf("Element \"%d\" is not in list.\n\n", data);
    }
    else
    {
        temp = p->link;
        p->link = temp->link;
        free(temp);
    }

    return start;
}


struct node *insertInBeginning(struct node *start, int data)
{
    struct node *temp;

    if (start == NULL)
    {
        start = createNode(data, NULL);
    }
    else
    {
        temp = createNode(data, start);
        start = temp;
    }
    
    return start;
}

struct node *insertBefore(struct node *start, int data, int x)
{
    struct node *p, *temp;

    if (start->info == x) {
        temp = createNode(data, start);
        start = temp;
        return start;
    }

    p = start;
    while(p->link != NULL)
    {
        if (p->link->info == x)
            break;
        p = p->link;
    }

    if (p->link == NULL) {
        printf("Element \"%d\" is not in list.\n\n", x);
    }
    else
    {
        temp = createNode(data, p->link);
        p->link = temp;
    }

    return start;
}

void insertAfter(struct node *start, int data, int x)
{
    struct node *p, *temp;

    p = start;
    while(p->link != NULL)
    {
        if(p->info == x)
            break;
        p = p->link;
    }

    if (p->link == NULL) {
        printf("Element \"%d\" is not in list.\n\n", x);
    }
    else
    {
        temp = createNode(data, p->link);
        p->link = temp;
    }
}

struct node *insertAtPosition(struct node *start, int data, int x)
{
    struct node *p, *temp;
    int count = 0;

    p = start;
    while(p->link !=NULL) {
        count++;
        if (count == x)
            break;
        p = p->link;
    }

    if(p->link == NULL) {
        printf("Position \"%d\" is out of bounds!", x);
    }
    else
    {
        temp = createNode(data, p->link);
        p->link = temp;
    }

    return start;
}

struct node *reverseList(struct node *start)
{
    struct node *p, *prev, *next;

    if (start->link == NULL)
        return start;
    prev = NULL;
    p = start;
    while(p != NULL)
    {
        next = p->link;
        p->link = prev;
        prev = p;
        p = next;
    }

    start = prev;

    return start;
}
