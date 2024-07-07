package String;

import java.util.Scanner;

public class reverseString {
    public static void main(String[] args){
        reverseString T = new reverseString();
        Scanner in=new Scanner(System.in); // 입력받기
        String str = in.next(); // 입력받은 문자열
        char[] arr = str.toCharArray();
        int lt = 0, rt = arr.length -1;
        char tmp;
        while(lt < rt) {
            if(!Character.isAlphabetic(arr[lt])) {
                lt++;
            } else if(!Character.isAlphabetic((arr[rt]))) {
                rt--;
            } else {
                tmp = arr[lt];
                arr[lt] = arr[rt];
                arr[rt] = tmp;
                lt++;
                rt--;
            }
        }
        System.out.println(String.valueOf(arr));

    }
}