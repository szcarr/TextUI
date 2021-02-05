import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class MainTest {
    
    public static void main(String[] args) {
        
        Path path = Paths.get("c:\\data\\test.txt");

        Path currentDir = Paths.get(".");
        System.out.println(currentDir.toAbsolutePath());

        try {

            System.out.println(path.toRealPath());

        } catch (Exception e) {

            System.out.println("failed");

        }
        
    }

}