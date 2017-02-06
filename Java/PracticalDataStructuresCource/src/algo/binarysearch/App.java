package algo.binarysearch;

/**
 * Created by blakfeld on 2/5/17.
 */
public class App {
    public static void main(String[] args) {
        int[] arrayToSearch = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        System.out.println(binarySearch(arrayToSearch, 7));

    }

    public static int binarySearch(int[] A, int x) {
        int p = 0;
        int r = A.length - 1;
        while (p <= r) {
            int q = (p + r) / 2;
            if (A[q] < x) p = q + 1;
            else if (A[q] > x) r = q - 1;
            else return q;
        }

        return -1;
    }
}
