import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class studentRecordsSystem {

    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        
        File myfile = new File("C:\\Users\\Shainiee\\OneDrive\\Documents\\Netbeans\\JavaCollege\\worksheet9\\students.txt");
        
       // creating file
        try {
            if (myfile.createNewFile()) {
            System.out.println("File " + myfile.getName() + " is successfully created.");
            } else {
            System.out.println("File already exists.");
            }
            
        } catch (IOException e) {
            System.out.println("An error occurred.");
        }
    }
}