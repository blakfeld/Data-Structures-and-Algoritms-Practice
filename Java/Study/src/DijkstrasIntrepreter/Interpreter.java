package DijkstrasIntrepreter;

import java.util.Stack;

/**
 * Created by blakfeld on 2/16/16.
 */
public class Interpreter {
    private Stack<String> operationStack;
    private Stack<Double> valueStack;

    public Interpreter() {
        operationStack = new Stack<>();
        valueStack = new Stack<>();
    }

    public void interpretExpression(String expression) {
        String[] tokenizedExpression = expression.split(" ");

        for (String s : tokenizedExpression) {
            switch(s) {
                case "(":
                    // Ignore.
                    break;
                case "+":
                    this.operationStack.push(s);
                    break;
                case "*":
                    this.operationStack.push(s);
                    break;
                case "-":
                    this.operationStack.push(s);
                    break;
                case "/":
                    this.operationStack.push(s);
                    break;
                case ")":
                    String operation = this.operationStack.pop();
                    this.performOperation(operation);
                    break;
                default:
                    this.valueStack.push(Double.parseDouble(s));
                    break;
                }
        }

        while(!operationStack.empty()) {
            String operation = this.operationStack.pop();
            this.performOperation(operation);

        }
    }

    public void performOperation(String operation) {
        switch(operation) {
            case "+":
                this.valueStack.push(this.valueStack.pop() + this.valueStack.pop());
                break;
            case "-":
                this.valueStack.push(this.valueStack.pop() - this.valueStack.pop());
                break;
            case "*":
                this.valueStack.push(this.valueStack.pop() * this.valueStack.pop());
                break;
            case "/":
                this.valueStack.push(this.valueStack.pop() / this.valueStack.pop());
                break;
        }
    }

    public Double result() {
        return this.valueStack.pop();
    }

}
