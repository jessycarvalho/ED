import java.util.*;

public class Main {
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      
      String codigo = sc.nextLine();
      System.out.println("\nDigite o código de acesso:");
     
      
      if (codigo.equals("Admin123")) {
        System.out.println("\nBem vindo, administrador!");
      }
      else if(codigo.equals("User123")){
          System.out.println("\nBem-vindo, usuário!");
        }
      else{
        System.out.println("\nCódigo incorreto!");
      }
      
  }
}