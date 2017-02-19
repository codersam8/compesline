import java.util.Scanner;

class kktries{
	
	public static void main(String args[]){
	Scanner scn = new Scanner(System.in);
		int tCases = scn.nextInt();
		for(int s = 0;s<tCases;s++){//loop for each case
			int[][] pplArr = new int[scn.nextInt()][2];
			for(int j = 0;j<pplArr.length;j++){//for no of ppl
				pplArr[j][0]=scn.nextInt();
				pplArr[j][1]=scn.nextInt();
			}
					
		
		int does00Exist = 0;
		int distSols = pplArr.length;
		int smallest = 2*(int)Math.pow(10,pplArr.length);
		for(int i = 0;i<pplArr.length;i++){//for selecting which //person to compare against
			if( pplArr[i][0] == 0 && pplArr[i][1] == 0){
				does00Exist++;
			}
			int op[] = new int[pplArr.length];
			int lb = pplArr[i][0];
			int ub = pplArr[i][1];
			for(int j = 0;j<pplArr.length;j++){//comparing //against each person in the test case
				op[i] *= 10;
				if(!(ub < pplArr[j][0])){
					if(!(lb > pplArr[j][1])){
						op[i]++;
						
					}
				}
			}
			int k = i-1;
			for(;k>=0 && op[k]!=op[i]; k--)
			{
			}
			if(k!= -1)
				distSols--;
			if(smallest > op[i])
				smallest = op[i];
			
		}
		if(does00Exist == 0)
		{
			System.out.println((distSols+1) % 1000000007);
			for(int k = 0;k<pplArr.length;k++)
			{
				System.out.print(0);
			}
		}
		else
		{
			System.out.println(distSols%1000000007);
			int lead0 = (int) Math.pow(10,(pplArr.length-1));
			for( int k = 0 ;lead0 > smallest * Math.pow(10,k);k++)
			{
				System.out.print(0);
			}
			System.out.print(smallest);
		}
	}
	}
}
