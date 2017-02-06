package ds.doublylinkedlist;

/**
 * Created by blakfeld on 2/5/17.
 */
public class Node<T> {
    public T data;
    public Node<T> next;
    public Node<T> previous;

    public Node(T data) {
        this.data = data;
    }

    public void displayNode() {
        System.out.print("{ " + data + " } ");
    }
}
