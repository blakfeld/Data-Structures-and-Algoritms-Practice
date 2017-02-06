package ds.circularlinkedlist;

/**
 * Created by blakfeld on 2/5/17.
 */
public class CircularLinkedList<T> {
    private Node<T> first;
    private Node<T> last;

    public void insertFirst(T data) {
        Node<T> newNode = new Node<>(data);

        if(isEmpty()) {
            last = newNode;
        }
        newNode.next = first;
        first = newNode;
    }

    public void insertLast(T data) {
        Node<T> newNode = new Node<>(data);

        if (isEmpty()) {
            first = newNode;
        } else {
            last.next = newNode;
            last = newNode;
        }
    }

    public T deleteFirst() {
        T temp = first.data;
        if (first.next == null) {
            last = null;
        }
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

    private boolean isEmpty() {
        return (first == null);
    }

}
