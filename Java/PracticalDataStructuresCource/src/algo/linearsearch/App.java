package algo.linearsearch;

/**
 * Created by blakfeld on 2/5/17.
 */
public class App {
    public static void main(String[] args) {

    }

    public static int linearSearch(int[] a, int x) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] == x) {
                return i;
            }
        }
        return -1;
    }
}
