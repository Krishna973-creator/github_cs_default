import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        double num1, num2;
        char operator;

        System.out.println("Enter two numbers:");

        try {
            num1 = reader.nextDouble();
            num2 = reader.nextDouble();
        } catch (java.util.InputMismatchException e) {
            System.out.println("Invalid input. Please enter numbers only.");
            return;
        }

        System.out.println("Enter an operator (+, -, *, /):");
        operator = reader.next().charAt(0);

        double result;

        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("Error! Division by zero is not allowed.");
                    return;
                }
                break;
            default:
                System.out.println("Invalid operator!");
                return;
        }

        System.out.println(num1 + " " + operator + " " + num2 + " = " + result);
        reader.close();
    }
}
