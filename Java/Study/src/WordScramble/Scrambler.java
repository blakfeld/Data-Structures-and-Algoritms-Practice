package WordScramble;

import java.util.Random;

/**
 * Created by blakfeld on 2/17/16.
 */
public class Scrambler {
    private Random rand;

    public Scrambler() {
        rand = new Random();
    }

    public String scambleWord(String word) {
        String[] tokenizedWord = word.split("");
        String result;

        do {
            for (int i = 0; i < tokenizedWord.length; i++) {
                int randIndexOne = rand.nextInt(tokenizedWord.length);
                int randIndexTwo = rand.nextInt(tokenizedWord.length);

                String temp = tokenizedWord[randIndexOne];
                tokenizedWord[randIndexOne] = tokenizedWord[randIndexTwo];
                tokenizedWord[randIndexTwo] = temp;
            }

            result = String.join("", tokenizedWord);

        } while(result.equals(word));

        return result;
    }
}
