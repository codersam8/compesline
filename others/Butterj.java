import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet;
class Test {

     public static void main(String a[]) throws IOException {

	  TreeMap<BigInteger, BigInteger> map =  new TreeMap<BigInteger, BigInteger>();
	  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	  int test = Integer.valueOf(br.readLine());
	  while(test!=0) {
	       int N = Integer.valueOf(br.readLine());  

	       int arr[] =  new int[N];

	       for( int i=0 ; i<N ; ++i)
		    arr[i] = Integer.valueOf(br.readLine());

	       int count = 1;
	       Arrays.sort(arr);


	       boolean flag = true;
	       int i = 0 ,  j =1;
	       for(  ; i<N && j<N; ++i){
		    flag =false;
		    for(; j<N ;++j){
			 if(arr[j] > arr[i] ){
			      ++j;
			      flag =true;
			      break;
			 }
		    }



	       }

	       if(flag)
		    System.out.println(j-i);
	       else
		    System.out.println(j-i+1);
	       --test;
	  }



     }
} 
