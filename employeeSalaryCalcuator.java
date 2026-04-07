import java.util.Scanner;
public class employeeSalaryCalcuator {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        displayCompanyInfo();

        System.out.print("\nEmployee's Name: ");
        String employeeName = s.nextLine();
        System.out.print("Current Salary: ");
        double oldSalary = s.nextDouble();
        System.out.print("Salary Increment Percentage: ");
        double increment = s.nextDouble();

        double newSalary = calculateSalary(oldSalary, increment);
        displaySalary(employeeName, oldSalary, newSalary);
    }

    public static void displayCompanyInfo() {
		System.out.println("********* SIGMA COMPANY *********");
		System.out.println("Address: Alang-alang Mandaue City Cebu");
	}

    public static double calculateSalary(double oldSalary, double increment) {
		double newSalary = (oldSalary * increment) / 100;
		return oldSalary + newSalary;
	}

    public static void displaySalary(String employeeName, double oldSalary, double newSalary){
        System.out.println("\n-------- SALARY DETAILS --------");
        System.out.println("Employee: " + employeeName);
        System.out.println("Previous Salary: $" + oldSalary);
        System.out.println("Updated Salary: $" + newSalary);
    }
}