import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
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

        // asking the user to input record
        try {
            FileWriter myWriter = new FileWriter(myfile, true);
            System.out.print("\nEnter your name: ");
            String name = s.nextLine();
            System.out.print("Enter your ID: ");
            String id = s.nextLine();
            System.out.print("Enter your grade: ");
            String grade = s.nextLine();
            myWriter.write(name + ", " + id + ", " + grade + "\n"); // Write in comma-separated format
            System.out.println("\nData written successfully to the file.");
            myWriter.close();
            
        } catch (IOException e) {
            System.out.println("An error occurred.");
        }

        // viewing all student records into the file
            System.out.println("\nAll student data into the file: ");
        try {
            Scanner readFile = new Scanner(myfile);
            while (readFile.hasNextLine()) {
            String data = readFile.nextLine();
            System.out.println(data);
            }
            readFile.close();
            
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
        }
    }
}