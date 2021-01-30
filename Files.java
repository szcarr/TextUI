import java.nio.file.Paths;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class Files {

    private Scanner scanner;
    private ArrayList<String> list;
    
    public Files(Scanner scanner) {

        this.scanner = scanner;
        this.list = new ArrayList<>();

    }

    public void initialize() {

        while (true) {

            System.out.println("");
            System.out.println("############## - Files class initialized - ##############");
            System.out.println("");
            System.out.print("Give file name: ");
            String file = scanner.nextLine();

            System.out.println("");
            System.out.println("Press the numerical value according to what you want to do.");
            System.out.println("1. Read file in its entirety ");
            System.out.println("2. Search for keyword in given file.");

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

                readFile(file);

            } else if (mode == 2) {

                keyword(file);

            }

        }

    }

    public void readFile(String file) {

        try (Scanner filescanner = new Scanner(Paths.get(file))) {

            while (filescanner.hasNextLine()) {

                String row = filescanner.nextLine();

                this.list.add(row);

            }

        } catch (Exception e) {

            System.out.println("Failed at reading " + e.getMessage());

        } finally {

            for (int i = 0; i < this.list.size(); i++) {

                System.out.println(this.list.get(i));

            }

        }
       
    }

    public void keyword(String file) {



    }

}
