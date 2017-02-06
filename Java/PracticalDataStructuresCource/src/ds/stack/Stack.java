package ds.stack;

/**
 * Created by blakfeld on 2/4/17.
 */
public class Stack<T> {
    private int maxSize;
    private char[] stackArray;
    private int top;

    public Stack(int maxSize) {
        this.maxSize = maxSize;
        this.stackArray = new char[maxSize];
        this.top = -1;
    }

    public void push(char c) {
        if (isFull()) {
            System.out.println("Stack is full!!!");
        } else {
            top++;
            stackArray[top] = c;
        }
    }

    public char pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty!!!");
            return '0';
        } else {
            int oldTop = top;
            top--;

            return stackArray[oldTop];
        }
    }

    public char peak() {
        return stackArray[top];
    }

    public boolean isEmpty() {
        return (top == -1);
    }

    public boolean isFull() {
        return (maxSize - 1 == top);
    }
}
