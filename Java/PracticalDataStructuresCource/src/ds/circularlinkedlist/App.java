package ds.circularlinkedlist;

/**
 * Created by blakfeld on 2/5/17.
 */
public class App {

    public static void main(String[] args) {
        CircularLinkedList<Integer> myList = new CircularLinkedList<>();
        myList.insertFirst(100);
        myList.insertFirst(50);
        myList.insertFirst(99);
        myList.insertFirst(88);
        myList.insertLast(1000);

        myList.displayList();
    }
}
