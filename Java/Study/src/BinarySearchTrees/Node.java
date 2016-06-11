package BinarySearchTrees;

/**
 * Created by blakfeld on 2/17/16.
 */
public class Node<T extends Comparable<T>> {

    private T data;
    private Node<T> leftChild;
    private Node<T> rightChild;

    public Node(T data) {
        this.data = data;
    }

    public void insert(T newData) {
        if (newData.compareTo(data) < 0) {
            if (this.leftChild != null) {
                this.leftChild.insert(newData);
            } else {
                this.leftChild = new Node<T>(newData);
            }
        } else {
            if (this.rightChild != null) {
                this.rightChild.insert(newData);
            } else {
                this.rightChild = new Node<T>(newData);
            }
        }
    }

    public void traverseInOrder() {
        if (this.leftChild != null) {
            this.leftChild.traverseInOrder();
        }

        System.out.print(this + "-");

        if (this.rightChild != null) {
            this.rightChild.traverseInOrder();
        }
    }

    public Node<T> remove(T data, Node<T> root) {

        // Base Case
        if (root == null) return root;

        // Search to left: Data we're searching for is smaller
        if (data.compareTo(root.getData()) < 0) {
            Node<T> tempNode = remove(data, root.getLeftChild());
            root.setLeftChild(tempNode);

        // Search to the right: Data we're searching for is larger.
        } else if (data.compareTo(root.getData()) > 0) {
            Node<T> tempNode = remove(data, root.getRightChild());
            root.setRightChild(tempNode);

        // We've found the node we're searching for
        } else {

            // Node with one child or no children at all
            if (root.getLeftChild() == null) {
                Node<T> tempNode = root.getRightChild();
                root = null;
                return tempNode;
            } else  if (root.getRightChild() == null) {
                Node<T> tempNode = root.getLeftChild();
                root = null;
                return tempNode;
            }

            // Node has two children. We must get a successor -- the node with the smallest value in the right subtree
            Node<T> tempNode = this.getMinValue(root.getRightChild());
            root.setData(tempNode.getData());

            // We have to remove the in order successor
            root.setRightChild(remove(tempNode.getData(), root.getRightChild()));
        }

        return root;
    }

    public Node<T> getMinValue(Node<T> node) {
        Node<T> currentNode = node;

        while(currentNode.getLeftChild() != null) {
            currentNode = currentNode.getLeftChild();
        }

        return currentNode;
    }

    public Node<T> getMaxValue(Node<T> node) {
        Node<T> currentNode = node;

        while(currentNode.getRightChild() != null) {
            currentNode = currentNode.getRightChild();
        }

        return currentNode;
    }

    @Override
    public String toString() {
        return "" + this.data;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Node<T> getLeftChild() {
        return leftChild;
    }

    public void setLeftChild(Node<T> leftChild) {
        this.leftChild = leftChild;
    }

    public Node<T> getRightChild() {
        return rightChild;
    }

    public void setRightChild(Node<T> rightChild) {
        this.rightChild = rightChild;
    }
}
