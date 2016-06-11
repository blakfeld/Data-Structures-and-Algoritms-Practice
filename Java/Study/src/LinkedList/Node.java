package LinkedList;

import java.util.Comparator;

/**
 * Created by blakfeld on 2/16/16.
 */
public class Node <T extends Comparable<T>>  {

    private T data;
    private Node<T> nextNode;

    public Node(T data) {
        this.data = data;
    }

    public void insert(T newData) {
        if (this.nextNode != null) {
            this.nextNode.insert(newData);
        } else {
            this.nextNode = new Node<T>(newData);
        }
    }

    public void remove(T dataToRemove, Node<T> previousNode) {
        if (this.data.compareTo(dataToRemove) == 0) {
            previousNode.setNextNode(this.getNextNode());
            this.data = null;
            this.nextNode = null;
        } else {
            if (this.getNextNode() != null) {
                this.nextNode.remove(dataToRemove, this);
            }
        }
    }

    @Override
    public String toString() {
        return this.data.toString();
    }

     public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Node<T> getNextNode() {
        return nextNode;
    }

    public void setNextNode(Node<T> nextNode) {
        this.nextNode = nextNode;
    }

}
