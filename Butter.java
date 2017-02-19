import java.util.Scanner;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Butter
{
     //     Scanner scn = new Scanner(System.in);
     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
     public static void main(String[] args)
     {
	  Butter b1 = new Butter();
	  b1.begin();
     }

     void begin()
     {
	  try
	  {
	       int testC = Integer.valueOf(br.readLine());
	       //	  System.out.println("test cases: "+testC);

	       for(int i=0;i<testC;i++)
	       {
		    int numBoxes = Integer.valueOf(br.readLine());
		    //	       System.out.println("boxes in test case "+(i+1)+" "+numBoxes);
		    int value[] = new int[numBoxes];
		    //	       System.out.println("box values");

		    for(int j =0;j<numBoxes;j++)
		    {
			 value[j] = Integer.valueOf(br.readLine());	    
			 //		    System.out.println(value[j]);
		    }

		    Arrays.sort(value);
		    //qSort(value,0,value.length-1);
		    //	       int c,n;
		    int lb=1,ub=1;

		    for(int k = 0;k<(value.length-1);k++)
		    {
			 //		    c = value[k];
			 //		    n = value[k+1];
			 //		    System.out.println("c and n "+c+" "+n);  
			 if(value[k]==value[k+1])
			 {
			      lb++;
			 }
			 else
			 {
			      if(ub<lb)
			      {
				   ub = lb;
			      }
			      lb=1;
			 }
		    }
		    if(ub<lb)
			 ub=lb;
		    System.out.println(ub);
	       }
	  }
	  catch(IOException e)
	  {
	  }

     }

     void qSort(long[] value,int begin,int end)
     {

	  if(begin<end)
	  {
	       int pivInd = partition(value,begin,end);
	       qSort(value,begin,pivInd-1);
	       qSort(value,pivInd+1,end);
	  }
     }

     int partition(long[] value,int begin,int end)
     {
	  long piv = value[end-1];
	  int lessEle = begin-1;
	  long temp;

	  for(int i = begin;i<=end;i++)
	  {
	       if(value[i]<=piv)
	       {
		    lessEle++;
		    temp = value[i];
		    value[i]= value[lessEle];
		    value[lessEle] = temp;
	       }
	  }
	  return lessEle;
     }
}

