import java.util.Scanner;
public class voter {
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        
        System.out.print("Enter name: ");
        String name = s.nextLine();
        System.out.print("Enter age : ");
        int age = s.nextInt();
        
        if(age >= 18){
            System.out.println("Hi, " + name + " you can now vote!");
        }else
            System.out.println("Hi, " + name + " you can not vote yet!");
        }
    }