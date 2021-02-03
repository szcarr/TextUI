import java.util.Scanner;
import java.util.ArrayList;

public class TextUI {

    private Scanner scanner;
    private ArrayList <String> commandList;

    private boolean fromSomeWhereElse; // This should be changed to true before another class is initialized.
    
    public TextUI(Scanner scanner) {

        this.scanner = scanner;
        this.commandList = new ArrayList<>();


    }

    // temp holder input.equals("")

    public void start() {

        boolean firstRunTime = true;

        while (true) {

            if (firstRunTime) {

                System.out.println("\nFor help type 'help'. All commands should be given in lowercase.\n");
                firstRunTime = false;

            } else if (fromSomeWhereElse) {

                System.out.println("\nFor help type 'help'. All commands should be given in lowercase.\n");
                this.fromSomeWhereElse = false;     

            }

            System.out.print("> ");
            String input = scanner.nextLine();

            // Checks for commands
            if (input.equals("help")) {

                System.out.println("1. 'stop' closes the UI program");
                System.out.println("2. 'files' reads the specified file");

            } else if (input.equals("stop")) {

                System.out.println("");
                System.out.println("############## - Closing Program - ##############");
                System.out.println("");
                break;

            } else if (input.equals("files")) {

                Files file = new Files(scanner);
                this.fromSomeWhereElse = true;
                file.initialize();

            } else {

                System.out.println("Unknown command");

            }

        }

    }
    
}