import java.util.Scanner;

class Butter
{
     Scanner scn = new Scanner(System.in);

     public static void main(String[] args)
     {
     }

     void begin()
     {
	  int testC = scn.nextInt();
	  
	  for(int i=0;i<testC;i++)
	  {
	       int numBoxes = scn.nextInt();
	       int value[] = new int[numBoxes];
	       
	       for(int j =0;j<numBoxes;j++)
	       {
		    value[j] = scn.nextInt();	    
	       }
	  }

     }

     void qSort(int[] value,int arrLen,int end,int begin)
     {
	  
	  

}
