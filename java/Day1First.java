import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day1First {
    public static void main(String[] args) throws FileNotFoundException {
        File input = new File("../input/day1.txt");
        Scanner calories = new Scanner(input);
        int cal_max = 0;
        int cal_total = 0;
        
        while (calories.hasNextLine()) {
            String data = calories.nextLine();
            if (data.isEmpty()) {
                cal_max = Math.max(cal_max, cal_total);
                cal_total = 0;
                }
            else cal_total += Integer.valueOf(data);
            }
            
        calories.close();
        System.out.println(cal_max);
        }
    }