/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
//https://www.hackerrank.com/challenges/service-lane
package compete;

import java.util.Scanner;

/**
 *
 * @author sampath
 */
public class ServiceLane {
    
    public static void main(String[] a)
    {
        ServiceLane sl = new ServiceLane();
        sl.begin();
    }
    
    void begin()
    {
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        int tc = sc.nextInt();
        int[] width = new int[len];
        for (int i = 0; i < len; i++) 
        {
            width[i]= sc.nextInt();
        }
        int si,ei,lgst;
        for(int i = 0;i<tc;i++)
        {
            lgst=3;
            si = sc.nextInt();
            ei=sc.nextInt();
           // System.out.println("si "+si+" ei "+ei);
            for(;si<=ei;si++)
            {
               // System.out.print(width[si]+" ");
                if(width[si]<lgst)
                    lgst=width[si];
            }
            System.out.println(lgst);
        }
    }
    
}
