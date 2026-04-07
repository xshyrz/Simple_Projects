public class circle {
    public static void main(String args[]){
        
        consCircle newcircle = new consCircle();  
        System.out.println("The area of the circle with radius of " + newcircle.radius + " is " + newcircle.getArea());
        
        consCircle circle2 = new consCircle(10);  
        System.out.println("The area of the circle with radius of " + circle2.radius + " is " + circle2.getArea());       
        
    }
}

class consCircle {  
    double radius; 
    
    consCircle(){  
        radius = 1;
    }
    consCircle (double newRadius){ 
        radius = newRadius;
    }
    double getArea(){  
        return radius * radius * Math.PI;
    }
}

