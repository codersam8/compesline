import java.io.BufferedReader;
import java.io.InputStreamReader;

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
	       int tc = br.read(); 
	       for(int i =0;i<tc;i++)
	       {
	       }
	  }
	  catch(IOException e)
	  {
	  }

     }
}
