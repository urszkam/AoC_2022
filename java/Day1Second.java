import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day1Second {
    public static void main(String[] args) throws FileNotFoundException {
        File input = new File("../input/day1.txt");
        Scanner calories = new Scanner(input);
        int cal_max, cal_total, cal_second, cal_third;
        cal_max = cal_total = cal_second = cal_third = 0;
        
        while (calories.hasNextLine()) {
            String data = calories.nextLine();
            if (data.isEmpty()) {
                if (cal_total >= cal_max) {
                    cal_third = cal_second;
                    cal_second = cal_max;
                    cal_max = cal_total;
                }
                else if (cal_total >= cal_second) {
                    cal_third = cal_second;
                    cal_second = cal_total;
                }
                else if (cal_total > cal_third) {
                    cal_third = cal_total;
                }
                cal_total = 0;
                }
            else cal_total += Integer.valueOf(data);
            }

        calories.close();
        int sum = cal_max + cal_second + cal_third;
        System.out.println(sum);
        }
    }
