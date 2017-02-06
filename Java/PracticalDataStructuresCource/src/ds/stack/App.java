package ds.stack;

/**
 * Created by blakfeld on 2/4/17.
 */
public class App {
    public static void main(String [] args) {
        App app = new App();
        System.out.println(app.reverseString("Hello World"));

    }

    public String reverseString(String str) {
        Stack stringStack = new Stack(100);

        for (int i = 0; i < str.length(); i++) {
            stringStack.push(str.charAt(i));
        }

        String result = "";
        while (!stringStack.isEmpty()) {
            result += stringStack.pop();
        }

        return result;
    }
}
