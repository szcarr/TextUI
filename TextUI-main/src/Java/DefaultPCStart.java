import java.lang.Process;
import java.lang.ProcessBuilder;
import java.io.IOException;
import java.io.File;
import java.io.InputStream;

public class DefaultPCStart {

    private Files file; //Imported files class so i dynamically can find the filepath

    public DefaultPCStart(Files file) {

        this.file = file;

    }

    public void start() {

        Runtime rt = Runtime.getRuntime();

        try {

            String pathToWorkingDir = file.stringOfMyPath();
            String[] pathArray = pathToWorkingDir.split("");

            System.out.println(pathArray[5]);

            rt.exec(new String[] {"D:\\Documents\\Viktig\\Programmering\\Java\\Prosjekt\\TextUI\\TextUI-main\\TextUI-main\\src\\BAT\\default.bat"});
            //rt.exec(new String[]{"cmd.exe","/c","start","testetst"}); !EXPERIMENTAL
            //rt.exec(new String[]{"cmd.exe /c default.bat"}); !EXPERIMENTAL
            //rt.exec(new String[]{"cmd.exe", "/c", "start"}); !! THIS WORKS

        } catch (IOException e) {

            e.printStackTrace();

        }

    }

}