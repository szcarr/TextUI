import java.io.File;
import java.util.Scanner;

import java.util.ArrayList;

public class Files {

    //Objects/Packages
    private File file;
    private Scanner scanner;
    private ArrayList<String> document;

    //Standard data types
    //Booleans
    private boolean isFileReadible;
    
    //Strings
    private String filePath;
    
    public Files(Scanner scanner) {

        this.scanner = scanner;
        this.document = new ArrayList<>();

    }

    public void initialize() {

        this.isFileReadible = true;  //A file is readable unless if its proven to not be readable

        while (true) {

            System.out.println("\n ############## - Files class initialized - ############## \n");
            System.out.print("Give file name(leave empty to close): ");
            String pathName = scanner.nextLine();
            this.filePath = pathName;

            if (pathName.equals("")) {

                break;

            }

            File fileDecoy = new File(this.filePath); // Use a decoy to get path of file.

            String actualPathName = fileDecoy.getAbsolutePath(); // Can remove this line and just paste fileDecoy.getAbsolutePath(); straight to file class parameter.

            System.out.println(actualPathName);

            file = new File(actualPathName); // Gets actual path by using decoys path

            readFile(file);

            if (this.isFileReadible) {

                printChooseMode();

                int mode;

                boolean previousInputFailed = false; //If user gave an error to the program it pormpts the user to give a new input

                while (true) {                   

                    if (previousInputFailed) { //If user gave an error to the program it pormpts the user to give a new input

                        printChooseMode();
                        
                    }

                    int[] acceptableArgs = {1, 2, 3}; //Adds list of all acceptable args that can be passed to get to next stage.
                    System.out.print("> ");
                    mode = Integer.valueOf(scanner.nextLine());               

                    try {

                        if (mode == acceptableArgs[mode - 1]) {

                            break;

                        } else {

                            System.out.println("Unknown command. Must give a valid command");

                        }

                    } catch (Exception e) {

                        previousInputFailed = true;

                        System.out.println(""); // Linebreaker for clarity
                        System.out.println(e);
                        System.out.println(""); // Linebreaker for clarity

                    }

                }

                if (mode == 1) {

                    keyword(file);                   

                } else if (mode == 2) {

                    printFile();                 

                } else if (mode == 3) {

                    printMyPath();                

                }

                break;

            }

        }

    }

    public void printChooseMode() {

        System.out.println("\nPress the numerical value according to what you want to do.");
        System.out.println("1. Search for keyword in given file.");
        System.out.println("2. Prints contents of the given file.");
        System.out.println("3. Prints filepath of given file");
                
        System.out.println(""); // Linebreaker for clarity

    }

    public void printMyPath() { //Mostly debugger class

        System.out.println("");

        File fileDecoy = new File(this.filePath); // Use a decoy to get path of file.
        String actualPathName = fileDecoy.getAbsolutePath(); // Can remove this line and just paste fileDecoy.getAbsolutePath(); straight to file class parameter.

        System.out.println(actualPathName);

    }

    public String stringOfMyPath() {

        File about = new File("about.txt");
        return about.getAbsolutePath();

    }

    public void readFile(File file) {

        this.document.clear(); // The list is reset for each time another file is read. (Might make a seperate method for this.)

        try {

            Scanner filescanner = new Scanner(file);

            while (filescanner.hasNextLine()) {

                String row = filescanner.nextLine();

                this.document.add(row);

            }

            filescanner.close();

        } catch (Exception e) {

            System.out.println("Failed at reading " + e.getMessage());     
            this.isFileReadible = false; 

        }
       
    }

    public void printFile() {

        for (int i = 0; i < this.document.size(); i++) {

            System.out.println(this.document.get(i));

        }

    }

    public void keyword(File file) {

        if (file.exists()) {

            System.out.print("Give word to look for in a file: ");
            String keyword = scanner.nextLine();

            boolean keywordWasFound = false;

            for (int i = 0; i < this.document.size(); i++) {

                if (this.document.get(i).contains(keyword)) {

                    keywordWasFound = true;
                    System.out.println(keyword + " was found at row: " + i + 1);

                }

            }

            if (!keywordWasFound) {

                System.out.println("There was no matching words of '" + keyword + "'");

            }

        } else {

            System.out.println("Failed giving keyword, cause there was no file to read.");

        }

    }

}