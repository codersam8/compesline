package compete;

import java.util.Scanner;

public class LoveLetter {
    
    public static void main(String ar[])
    {
        LoveLetter ll = new LoveLetter();
        ll.begin();
    }
    
    void begin()
    {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i = 0; i < tc; i++)
        {
            char[] wordArray = sc.next().toCharArray();
            int wrdLen = wordArray.length-1;
            int diff=0;
            for (int j = 0; j <=( wrdLen)/2; j++) 
            {
                diff=diff+Math.abs(wordArray[j]-wordArray[wrdLen-j]);
            }
            System.out.println(diff);
        }
    }
    
}
