package String;

import java.util.Scanner;

public class findText {
    public int solution(String str, char t) {
        int answer = 0;
        str=str.toLowerCase();
        t = Character.toLowerCase(t);
        // for each
        for (char x: str.toCharArray()
             ) {
            if(x == t) answer++;
        }

        // for i
//        for (int i = 0; i < str.length(); i++) {
//            if(str.charAt(i) == t) {
//                answer++;
//            }
//        }
        return answer;
    }
    public static void findText(String[] args){
        findText T = new findText();
        Scanner in=new Scanner(System.in); // 입력받기
        String str = in.next(); // 입력받은 문자열 읽기
        //char c=in.next().charAt(0);
        System.out.println(T.solution(str, 'n'));
    }
}