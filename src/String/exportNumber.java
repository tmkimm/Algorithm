package String;

import java.util.Scanner;

public class exportNumber {
    public static void main(String[] args){
        Scanner in=new Scanner(System.in); // 입력받기
        String str = in.next(); // 입력받은 문자열
        char[] arr = str.toCharArray();
        int answer = 0;
        for (char x: arr
             ) {
            if(x >= 48 && x <= 57) {
                answer = answer * 10 + (x - 48);
            }
        }
        System.out.println(answer);
    }
}