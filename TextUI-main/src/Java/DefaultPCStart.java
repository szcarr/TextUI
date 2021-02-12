import java.lang.Process;
import java.lang.ProcessBuilder;
import java.io.IOException;
import java.io.File;
import java.io.InputStream;


public class DefaultPCStart {

    public void start() {

        Runtime rt = Runtime.getRuntime();

        try {

            rt.exec(new String[]{"cmd.exe", "/c", "start"});
            //rt.exec(new String[]{"cmd.exe","/c","start","testetst"});

    
        } catch (IOException e) {

            e.printStackTrace();

        }

    }

}