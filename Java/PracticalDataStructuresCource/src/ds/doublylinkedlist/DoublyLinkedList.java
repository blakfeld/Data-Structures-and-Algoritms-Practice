package ds.doublylinkedlist;

/**
 * Created by blakfeld on 2/5/17.
 */
public class DoublyLinkedList<T> {
    private Node<T> first;
    private Node<T> last;

    public boolean isEmpty() {
        return first == null;
    }

    public void insertFirst(T data) {
        Node<T> newNode = new Node<>(data);

        if (isEmpty()) {
            last = newNode;
        } else {
            first.previous = newNode;
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
            newNode.previous = last;
        }
        last = newNode;
    }

    // Assume non-empty list.
    public Node<T> deleteFirst() {
        Node<T> temp = first;
        if (first.next == null) {
            last = null;
        } else {
            first.next.previous = null;
        }
        first = first.next;

        return temp;
    }

    // Assume non-empty list.
    public Node<T> deleteLast() {
        Node<T> temp = last;
        if (first.next == null) {
            first = null;
        } else {
            last.previous.next = null;
        }
        last = last.previous;

        return temp;
    }

    // Assume non-empty list.
    public boolean insertAfter(T key, T data) {
        Node<T> current = first;
        while(current.data != key) {
            current = current.next;
            if (current == null) {
                return false;
            }
        }

        Node<T> newNode = new Node<>(data);
        if (current == last) {
            current.next = null;
            last = newNode;
        } else {
            newNode.next = current.next;
            current.next.previous = newNode;
        }
        newNode.previous = current;
        current.next = newNode;

        return true;
    }

    //Assume non-empty liast.
    public Node<T> deleteKey(T key) {
        Node<T> current = first;
        while(current.data != key) {
            current = current.next;
            if (current == null)
                return null;
        }

        if (current == first) {
            first = current.next;
        } else {
            current.previous.next = current.next;
        }

        if (current == last) {
            last = current.previous;
        } else {
            current.next.previous = current.previous;
        }

        return current;
    }

    public void displayForward() {
        System.out.print("List (first --> last): ");
        Node<T> current = first;
        while(current != null) {
            current.displayNode();
            current = current.next;
        }
        System.out.println();
    }

    public void displayBackwards() {
        System.out.print("List (first --> last): ");
        Node<T> current = last;
        while(current != null) {
            current.displayNode();
            current = current.previous;
        }
        System.out.println();
    }
}
