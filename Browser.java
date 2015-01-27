import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Browser
{
     BufferedReader br = new BufferedReader(new InputStreamReader(
     System.in));
     public static void main(String[] args)
     {
	  Browser b = new Browser();
	  b.begin();
     }

     void begin()
     {
	  char[] vowe = {'a','e','i','o','u'};
	  try
	  {
	       int tc = Integer.parseInt(br.readLine()); 
	       for(int i =0;i<tc;i++)
	       {
		    char[] addr = br.readLine().toCharArray();
		    int addrLen = addr.length-4;//to skip checking .com
		    int len = 4;//commonly added for all for .com

		    for(int j = 4;j<addrLen;j++)
		    {
			 for(int k = 0;k<5;k++)
			 {
			      if(addr[j] == vowe[k])
			      {
				   len++;
		//		   System.out.println("char "+addr[j]+" len "+len);
				   break;
			      }
			      
			 }
		    }

		    System.out.println((addr.length-len)+"/"+addr.length);
	       }
	  }
	  catch(IOException e)
	  {
	  }

     }
}
