package LinkedList;

/**
 * Created by blakfeld on 2/16/16.
 */
public class App {

    public static void main(String[] args) {
        LinkedList<Integer> linkedList = new LinkedList<Integer>();

        linkedList.insert(2);
        linkedList.insert(4);
        linkedList.insert(122);
        linkedList.insert(9389);
        linkedList.insert(522);

        System.out.println(linkedList.getSize());

        linkedList.traverseLinkedList();
    }
}
