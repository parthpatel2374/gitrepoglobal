import java.util.*;
class checkoddeven{
    public static void main(String a[]){
        System.out.println("Enter some number:");
        Scanner input=new Scanner(System.in);
        int num=input.nextInt();
        if(num%2==0)
            System.out.println("The number is even."); 
        if(num%2!=0)
            System.out.println("The number is odd.");
        input.close();
    }
}