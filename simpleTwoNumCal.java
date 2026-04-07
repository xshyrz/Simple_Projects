import java.util.Scanner;
public class simpleTwoNumCal {
   public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
       
        int num1, num2, sum, dif, mul;
        float div;
        
        System.out.print("Enter first number : ");
        num1 = scan.nextInt();
        System.out.print("Enter second number: ");
        num2 = scan.nextInt();
        
        sum = num1 + num2;
        dif = num1 - num2;
        mul = num1 * num2;
        div = num1 / num2;
        
        System.out.println("\n--- Results ---" );
        System.out.println("Sum         : " + sum);
        System.out.println("Difference  : " + dif);
        System.out.println("Multiply    : " + mul);
        System.out.println("Divide      : " + div);
    }
}