#ifndef DOUBLYLINKEDLIST_H_
#define DOUBLYLINKEDLIST_H_

struct node *createList(struct node *start);
struct node *createNode(int data, struct node *prev, struct node *next);
struct node *insertInBeginning(struct node *start, int data);
struct node *insertBefore(struct node *start, int data, int x);
struct node *insertAtPosition(struct node *start, int data, int x);
struct node *deleteNode(struct node *start, int data);
struct node *reverseList(struct node *start);

void displayList(struct node *start);
void countNode(struct node *start);
void search(struct node *start, int x);
void insertAtEnd(struct node *start, int data);
void insertAfter(struct node *start, int data, int x);

#endif
