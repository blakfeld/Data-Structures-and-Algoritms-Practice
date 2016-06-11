package BinarySearchTrees;

import DijkstrasIntrepreter.Interpreter;

/**
 * Created by blakfeld on 2/17/16.
 */
public class App {
    public static void main(String[] args) {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();

        bst.insert(3);
        bst.insert(100);
        bst.insert(0);
        bst.insert(-23);
        bst.insert(12);
        bst.insert(389);

        bst.traverseGraph();
        bst.remove(3);
        bst.traverseGraph();
    }
}
