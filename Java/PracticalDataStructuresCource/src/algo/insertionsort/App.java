package algo.insertionsort;

/**
 * Created by blakfeld on 2/5/17.
 */
public class App {
    public static void main(String[] args) {
        int[] sortedArray = insertionSort(new int[] {9, 8, 3, 13, 87, 12, 99});
        for (int i = 0; i < sortedArray.length; i++) {
            System.out.println(sortedArray[i]);
        }
    }

    public static int[] insertionSort(int[] a) {
        for (int i = 1; i < a.length; i++) {
            int element = a[i];
            int j = i - 1;
            while(j >= 0 && a[j] > element) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = element;
        }

        return a;
    }
}
