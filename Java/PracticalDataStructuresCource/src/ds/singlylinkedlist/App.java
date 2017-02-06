package ds.singlylinkedlist;

/**
 * Created by blakfeld on 2/5/17.
 */
public class App {
    public static void main(String[] args) {
        SinglyLinkedList<Integer> myList = new SinglyLinkedList<>();
        myList.insertFirst(100);
        myList.insertFirst(50);
        myList.insertFirst(99);
        myList.insertFirst(88);
        myList.insertLast(1000);

        myList.displayList();
    }
}
