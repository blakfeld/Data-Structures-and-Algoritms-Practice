package DijkstrasIntrepreter;

/**
 * Created by blakfeld on 2/16/16.
 */
public class App {
    public static void main(String[] args) {
        Interpreter interpreter = new Interpreter();

        String expression = "( 1 + 5 ) * ( 4 + 4 )";
        interpreter.interpretExpression(expression);
        System.out.println(interpreter.result());
    }
}
