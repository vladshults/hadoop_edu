import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/**
 * Created by Демьян Бельский on 19.01.2017.
 */
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while((line = br.readLine()) != null){
            String[] words = line.split("\\W+");
            System.out.println(line);
            for(int i = 2; i < words.length; i++){
                    System.out.println(words[i] + "\t" + (words[1].equals("INF")?"INF":Integer.parseInt(words[1])+1) + "\t{}");
                }
        }
    }
}
