import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;

public class TextUI {

    private Scanner scanner;
    private ArrayList <String> commandList;

    private boolean fromSomeWhereElse; // This should be changed to true before another class is initialized.
    
    public TextUI(Scanner scanner) {

        this.scanner = scanner;
        this.commandList = new ArrayList<>();

    }

    public void printHelp() { //Prints this when class is entered

        System.out.println("\n############## - TextUI class initialized - ##############");
        System.out.println("\nFor help type 'help'. All commands should be given in lowercase.\n");

    }

    // temp holder input.equals("")

    public void start() {
        Files files = new Files(scanner);
        DefaultPCStart defaultPC = new DefaultPCStart(files);

        boolean firstRunTime = true;

        while (true) {

            if (firstRunTime) {

                printHelp();
                firstRunTime = false;

            } else if (fromSomeWhereElse) {

                printHelp();
                this.fromSomeWhereElse = false;     

            }

            System.out.print("> ");
            String input = scanner.nextLine();

            // Checks for commands
            if (input.equals("help")) {

                System.out.println("1. 'stop' closes the UI program");
                System.out.println("2. 'files' reads the specified file");
                System.out.println("3. 'dstart' opens the websites i usually look at");

            } else if (input.equals("stop")) {

                System.out.println("");
                System.out.println("############## - Closing Program - ##############");
                System.out.println("");
                break;

            } else if (input.equals("files")) {

                this.fromSomeWhereElse = true;
                files.initialize();

            } else if (input.equals("dstart")) {

                this.fromSomeWhereElse = true;
                defaultPC.start();
            
            } else {

                System.out.println("Unknown command");

            }

        }

    }
    
}