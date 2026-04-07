import java.util.Scanner;
public class elementArrays {
    
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        
        int arr[][] = new int[3][3];
        
        System.out.println("Enter elements for the array");
        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                System.out.print("Element [" + a + "][" + b + "]: ");
                arr[a][b] = s.nextInt();
            }
        }
    
        System.out.println("\n---- Inputted Array ----");
        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                System.out.print(arr[a][b] + "\t");
            }
            System.out.println();
        }
        
        int sum = 0;
        int diagonalSum = 0;
        int antiDiagonalSum = 0;
        
        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                sum += arr[a][b];
                if (a == b) {
                    diagonalSum += arr[a][b];
                }
                if (a + b == 2) {
                    antiDiagonalSum += arr[a][b];
                }
            }
        }
        
        System.out.println("\n------ Results ------");
        System.out.println("Sum of all elements  : " + sum);
        System.out.println("Sum of main diagonal : " + diagonalSum);
        System.out.println("Sum of anti-diagonal : " + antiDiagonalSum);
    }
}