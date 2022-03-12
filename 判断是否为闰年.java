import java.util.Scanner;
public class HelloWorld {
    public static void main(String[] args) {
        int a;
        Scanner scan = new Scanner(System.in);
        a = scan.nextInt();
        if (a % 4 == 0 && a % 100 != 0 ||a % 400 == 0) {
            System.out.println("Y");
        }else{
            System.out.println("N");
        }

    }
}
