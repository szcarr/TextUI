import java.lang.Process;
import java.lang.ProcessBuilder;
import java.io.File;

public class DefaultPCStart {

    public void start() {

        try {

            Runtime.getRuntime().exec(new String[]{"cmd.exe", "/c", new File("C:\Users\itwan\Documents\Prgorammering\Java\Prosjekt\TextUI-main\TextUI-main\src\.bat\defaultPCstart.bat")});
            System.out.println("--test");

        } catch (Exception e) {

            System.out.println("Failed starting Processbuilder");

        }

    }

}