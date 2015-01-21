import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Cavity
{
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args)
	{
		Cavity c = new Cavity();
		c.begin();
	}
	
	void begin()
	{
		try
		{
			int tc = br.read();
			System.out.println(tc);
			int[][] map = new int[tc][tc];
			for(int i = 0;i<tc;i++)
			{
				for(int j =0;j<tc;j++)
				{
					map[i][j] = br.read();
					System.out.print(map[i][j]);
				}
				System.out.println();
			}
		}
		catch(IOException e)
		{
			System.out.println(e);
		}
	}
}




















