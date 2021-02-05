import java.io.File;
import java.util.Scanner;

import java.util.ArrayList;

public class Files {

    private File file;
    private Scanner scanner;
    private ArrayList<String> document;

    private boolean isFileReadible;
    
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

            if (pathName.equals("")) {

                break;

            }

            File fileDecoy = new File(pathName); // Use a decoy to get path of file.

            String actualPathName = fileDecoy.getAbsolutePath(); // Can remove this line and just paste fileDecoy.getAbsolutePath(); straight to file class parameter.

            file = new File(actualPathName); // Gets actual path by using decoys path

            if (file.isAbsolute()) {

                System.out.println("--testtor"); // 

            }

            readFile(file);

            if (this.isFileReadible) {

                System.out.println("\nPress the numerical value according to what you want to do.\n1. Search for keyword in given file.");

                int mode;

                while (true) {

                    System.out.print("> ");
                    mode = Integer.valueOf(scanner.nextLine());

                    if (mode == 1 || mode == 2) {

                        break;

                    } else {

                        System.out.println("Unknown command. Must give a valid command");

                    }

                }

                if (mode == 1) {

                    keyword(file);
                    break;

                }

            }

        }

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

        } finally {

            for (int i = 0; i < this.document.size(); i++) {

                System.out.println(this.document.get(i));

            }

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