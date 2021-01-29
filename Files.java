import java.nio.file.Paths;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Files {

    private Scanner scanner;
    
    public Files(Scanner scanner) {

        this.scanner = scanner;

    }

    public void initialize() {

        while (true) {

            System.out.println("");
            System.out.println("############## - Files class initialized - ##############");
            System.out.println("");
            System.out.println("Give file name: ");
            String fileToInteractWith = scanner.nextLine();

            System.out.println("Press the numerical value according to what you want to do.");
            System.out.println("1. Read file in its entirety " + "/n" + "2. Search for keyword in given file.");


        }

    }

}
