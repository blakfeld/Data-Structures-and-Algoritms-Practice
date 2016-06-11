package WordScramble;

/**
 * Created by blakfeld on 2/17/16.
 */
public class App {
    public static void main(String[] args) {
        Scrambler scrambler = new Scrambler();

        String scrambled = scrambler.scambleWord("reallylongword");

        System.out.println(scrambled);
    }
}
