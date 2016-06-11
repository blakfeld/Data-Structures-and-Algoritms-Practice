package LinkedList;

/**
 * Created by blakfeld on 2/16/16.
 */
public class LinkedList <T extends Comparable<T>> {

    private Node<T> root;
    private int count;

    public boolean isEmpty() {
        return this.root == null;
    }

    public int getSize() {
        return this.count;
    }

    public void insert(T newData) {
        this.count++;

        if (this.root == null) {
            this.root = new Node<>(newData);
        } else {
            this.root.insert(newData);
        }

    }

    public void remove(T dataToRemove) {
        this.count--;

        if (this.root != null) {
            if (this.root.getData().equals(dataToRemove)) {
                this.root = this.root.getNextNode();
            } else {
                this.root.remove(dataToRemove, root);
            }
        }
    }

    public void traverseLinkedList() {
        Node<T> tmpNode = this.root;

        while (tmpNode != null) {
            System.out.print(tmpNode + "-");
            tmpNode = tmpNode.getNextNode();
        }
    }

}
