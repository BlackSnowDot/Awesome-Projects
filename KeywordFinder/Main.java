import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Main {
    private static final List<String> founded = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter File Path » ");
        String filePath = scanner.next();
        if (!Path.of(filePath).isAbsolute()) {
            System.out.println("File Not Found");
            System.exit(1);
        }
        System.out.print("Enter Keyword » ");
        String keyWord = scanner.next();


        System.out.print("Enter Output » ");
        String output = scanner.next();
        if (!Path.of(output).isAbsolute()) {
            Files.createFile(Path.of(output));
        }

        Instant start = Instant.now();

        for (String line : Files.readAllLines(Path.of(filePath))) {

            if (line.toLowerCase().contains(keyWord.toLowerCase())) {
                founded.add(line);
                Files.writeString(Path.of(output), String.format("%s\n%s", Files.readString(Path.of(output)), line));
                System.out.println("Founded " + line);
            }
        }
        System.out.println("Done! " + founded.size() + " line match with yor keywords in " + Duration.between(start, Instant.now()).toMillis() + " Millisecond");
    }
}
