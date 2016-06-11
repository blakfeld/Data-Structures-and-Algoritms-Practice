package BinarySearchTrees;

/**
 * Created by blakfeld on 2/17/16.
 */
public class BinarySearchTree<T extends Comparable<T>> {

    private Node<T> root;

    public void insert(T data) {
        if (this.root != null) {
            this.root.insert(data);
        } else {
            this.root = new Node<T> (data);
        }
    }

    public void traverseGraph() {
        if (this.root != null) {
            this.root.traverseInOrder();
        }
    }

    public T getMin() {
        Node<T> minNode = this.root.getMinValue(root);

        return minNode.getData();
    }

    public T getMax() {
        Node<T> maxNode = this.root.getMaxValue(root);

        return maxNode.getData();
    }

    public void remove(T value) {
        this.root = root.remove(value, root);
    }

}
