import java.util.Scanner;

class KnightKnave
{
	Scanner scn = new Scanner(System.in);
	public static void main(String args[]){
		KnightKnave kk = new KnightKnave();
		kk.startWorking();
	}

	void startWorking(){
		int tCases = scn.nextInt();
		for(int i = 0;i<tCases;i++){//loop for each case
			int ppl = scn.nextInt();
			int[][] pplArr = new int[ppl][2];
			for(int j = 0;j<ppl;j++){//for no of ppl
				pplArr[j][0]=scn.nextInt();
				pplArr[j][1]=scn.nextInt();
			}
		forTestCase(pplArr);			
		}
	}
	
	void forTestCase(int[][] pA){
		int does00Exist = 0;
		int distSols = 0;
		int smallest = (int)Math.pow(10,pA.length);
		int op[] = new int[pA.length];
		for(int i = 0;i<pA.length;i++){//for selecting one person to compare against
			if( pA[i][0] == 0 || pA[i][1] == 0){
				does00Exist++;
			}
			int ub = pA[i][1];
			for(int lb = pA[i][0];lb <= ub;lb++){//for number in persons range
				int count=0;
				int sol=0;
				for(int ep = 0;ep < pA.length && !(count > lb);ep++)//for each person in test case
				{	
					sol*=10;
					if((lb >= pA[ep][0] )&&(lb <= pA[ep][1] ))
					{
						sol++;
						count++;
					}
						
					
				 }
				if(lb == count)
				{
					int k = distSols-1;
					for(;k>=0 && op[k]!=sol; k--)
					{
					}
					if(k== -1)
					{	
						op[distSols] = sol;
						if(smallest > op[distSols])
							smallest = op[distSols];
						distSols++;
					}
				}
			}
		}
		display(op);
		if(does00Exist == 0)
		{
			System.out.println((distSols+1) % 1000000007);
			for(int k = 0;k<pA.length;k++)
			{
				System.out.print(0);
			}
		}
		else
		{
			System.out.println(distSols%1000000007);
			int lead0 = (int) Math.pow(10,(pA.length-1));
			for( int k = 0 ;lead0 > smallest * Math.pow(10,k);k++)
			{
				System.out.print(0);
			}
			System.out.print(smallest);
		}
	}
	void display(int[] op){
		for (int i = 0;i<op.length;i++)
		{
			System.out.println(op[i]);
		}
	}
	

}

