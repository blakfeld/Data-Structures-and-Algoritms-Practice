package ds.singlylinkedlist;

/**
 * Created by blakfeld on 2/5/17.
 */
public class SinglyLinkedList<T> {
    private Node<T> first;

    public boolean isEmpty() {
        return (first == null);
    }

    // Insert at beginning of list.
    public void insertFirst(T data) {
        Node<T> newNode = new Node<>(data);
        newNode.next = first;
        first = newNode;
    }

    public Node<T> deleteFirst() {
        Node<T> temp = first;
        first = first.next;

        return temp;
    }

    public void displayList() {
        System.out.println("List (first --> last) ");
        Node<T> current = first;
        while(current != null) {
            current.displayNode();
            current = current.next;
        }
        System.out.println();
    }

    public void insertLast(T data) {
        Node<T> current = first;
        while(current.next != null) {
            current = current.next;
        }
        Node<T> newNode = new Node<>(data);
        current.next = newNode;
    }
}
