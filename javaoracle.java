/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author lenovo
 */
import java.io.*;
import org.graalvm.polygot.*;
import java.util.Scanner;

public class Oracle {
    public static void main(String[]args)
    {
      Scanner input=new Scanner(System.in);
      String Email;
      String Password;
      
      System.out.println("Enter email address:");
      Email=input.nextLine();
      System.out.println("Enter Password:");
      Password=input.nextLine();
        
       if(Email.equals("Emre@gmail.com")&&Password.equals("JavaProgram"))
       {
         System.out.println("Welcome Emre");
       }
       else
       {
         System.out.println("Wrong Email address or Password please try again");
       }    
    }

    
    
}
