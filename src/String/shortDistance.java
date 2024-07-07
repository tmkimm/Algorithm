package String;

import java.util.Scanner;

public class shortDistance {
    public static void main(String[] args){
        Scanner in=new Scanner(System.in); // 입력받기
        String str = in.next(); // 입력받은 문자열
        String s = in.next();
        char[] arr = str.toCharArray();
        int[] answer = new int[arr.length];
        int p = 1000;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == s.charAt(0)) {
                p = 0;
            } else {
                p++;
            }
            answer[i] = p;
        }
        for (int i = arr.length - 1; i >= 0; i--) {
            if(arr[i] == s.charAt(0)) {
                p = 0;
            } else {
                p++;
            }
            if(answer[i] > p)
            answer[i] = p;
        }

        for (int i: answer
             ) {
            System.out.print(i + " ");
        }
    }
}