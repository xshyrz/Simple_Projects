import javax.swing.JOptionPane;
public class CineMax {
    public static void main(String[] args) {
        
        String age, name, tickets;
        int yourAge, yourTicket, totalTicket;
        final int fixedPrice = 12;
        
        name = JOptionPane.showInputDialog(null, "Please enter your name: ", "Name", JOptionPane.QUESTION_MESSAGE);
        age = JOptionPane.showInputDialog(null, "Enter your age: ", "Age", JOptionPane.INFORMATION_MESSAGE);
        yourAge = Integer.parseInt(age);
        
        tickets = JOptionPane.showInputDialog(null, "How many ticket you want to purchased: ", "Tickets Purchased", JOptionPane.QUESTION_MESSAGE);
        yourTicket = Integer.parseInt(tickets);
        totalTicket = yourTicket * fixedPrice;
        
        JOptionPane.showMessageDialog(null, "****************************** \nCineMax Theaters Receipt \n****************************** \nCustomer Name: " + name 
                                    + "\nTickets Purchased: " + yourTicket 
                                    + "\nPrice per ticket: $" + fixedPrice 
                                    + "\nTotal cost: $" + totalTicket);
    }
}