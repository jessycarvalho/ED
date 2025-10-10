import java.util.*;
import javax.swing.*;

public class Main {
    public static void main(String[] args) {
     String senha;
     Scanner sc = new Scanner(System.in);
     System.out.println("Digite sua senha: ");
     senha = sc.nextLine();
     if (senha.equals("1234")){
        System.out.println("Bem-vindo!");
     }
     else {
       System.out.println("Senha incorreta! Tente novamente!");
     }
     
  }
}