import java.util.Scanner;

class Butter
{
     Scanner scn = new Scanner(System.in);

     public static void main(String[] args)
     {
	  Butter b1 = new Butter();
	  b1.begin();
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
	       qSort(value,0,value.length-1);
	       int c,n,lb=1,ub=1;

	       for(int k = 0;k<(value.length-1);k++)
	       {
		    c = value[k];
		    n = value[k+1];
		    
		    if(c==n)
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
	       System.out.println(ub);
	  }

     }

     void qSort(int[] value,int begin,int end)
     {

	  if(begin!=end)
	  {
	       int pivInd = partition(value,begin,end);
	       qSort(value,begin,pivInd-1);
	       qSort(value,pivInd+1,end);
	  }
     }

     int partition(int[] value,int begin,int end)
     {
	  int piv = value[end-1];
	  int lessEle = begin-1;
	  int temp;
	  
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

