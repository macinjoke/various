package Facade.Sample.pagemaker;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class Database {
    private Database() {    // newでインスタンス生成させないためにprivate宣言
    }
    public static Properties getProperties(String dbname) { // データベース名からPropertiesを得る
        String filename = dbname + ".txt";
        final String PATH = "/home/shunji/work/java/IdeaProjects/SoftwareDesign/src/Facade/Sample/";
        Properties prop = new Properties();
        try {
            prop.load(new FileInputStream(PATH+filename));
        } catch (IOException e) {
            System.out.println("Warning: " + PATH+filename + " is not found.");
        }
        return prop;
    }
}
