package ds.queue;

/**
 * Created by blakfeld on 2/4/17.
 */
public class App {

    public static void main(String[] args) {
        Queue queue = new Queue(5);

        queue.insert(1);
        queue.insert(4);
        queue.insert(5);

        queue.view();
    }
}
