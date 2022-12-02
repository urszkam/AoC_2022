import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day2First {
    public static void main(String[] args) throws FileNotFoundException {
        File game = new File("../input/day2.txt");
        Scanner rounds = new Scanner(game);
        int total = 0;

        while (rounds.hasNextLine()) {
            String round = rounds.nextLine();
            switch (round) {
                case "A X": total += 4; break;
                case "A Y": total += 8; break;
                case "A Z": total += 3; break;
                case "B X": total += 1; break;
                case "B Y": total += 5; break;
                case "B Z": total += 9; break;
                case "C X": total += 7; break;
                case "C Y": total += 2; break;
                case "C Z": total += 6; break;
                default: break;
            }
        }
        rounds.close();
        System.out.println(total);
    }
}
