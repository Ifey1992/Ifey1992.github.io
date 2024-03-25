import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String operation;
        double number1, number2, result;

        while (true) {
            System.out.println("Enter your operation (+, -, *, /) or type 'quit' to exit: ");
            operation = scanner.next();

            if (operation.equalsIgnoreCase("quit")) {
                break;
            }

            System.out.println("Enter the first number: ");
            number1 = scanner.nextDouble();

            System.out.println("Enter the second number: ");
            number2 = scanner.nextDouble();

            switch (operation) {
                case "+":
                    result = add(number1, number2);
                    break;
                case "-":
                    result = subtract(number1, number2);
                    break;
                case "*":
                    result = multiply(number1, number2);
                    break;
                case "/":
                    if (number2 == 0) {
                        System.out.println("Error: Cannot divide by zero.");
                        continue;
                    }
                    result = divide(number1, number2);
                    break;
                default:
                    System.out.println("Invalid operation. Please try again.");
                    continue;
            }

            System.out.printf("Result: %.2f\n", result);
        }

        scanner.close();
        System.out.println("Calculator closed.");
    }

    public static double add(double a, double b) {
        return a + b;
    }

    public static double subtract(double a, double b) {
        return a - b;
    }

    public static double multiply(double a, double b) {
        return a * b;
    }

    public static double divide(double a, double b) {
        return a / b;
    }
}