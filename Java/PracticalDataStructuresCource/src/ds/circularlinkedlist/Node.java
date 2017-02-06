package ds.circularlinkedlist;

/**
 * Created by blakfeld on 2/5/17.
 */
public class Node<T> {
    public T data;
    public Node next;

    public Node(T data) {
        this.data = data;
    }

    public void displayNode() {
        System.out.println("{ " + data + " }");
    }
}
