package adt;

/**
 * Created by blakfeld on 2/4/17.
 */
public class App {
    public static void main(String[] args) {
        Counter counter = new Counter("App");
        counter.increment();
        counter.increment();
        counter.increment();
        System.out.println(counter.getCurrentValue());
    }
}
