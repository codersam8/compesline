nclude <iostream>
#include<cstdlib>
using namespace std;

int compare(const void *a,const void *b){
     return (*(int *)a - *(int *)b);
}

int main()
{
     int t,i;
     cin>>t;//t for test cases

     for(i=0;i<t;i++){
	  int n,j;//number of values
	  cin>>n;

	  long long int a[n+1];//why one more than the size
	  a[n]=-1;
	  for(j=0;j<n;j++){
	       cin>>a[j];
	  }
	  qsort(a,n,sizeof(long long int),compare);

	  int count=0,tempcount=1,max=-1;

	  for(j=1;j<=n;j++){
	       if(a[j]==a[j-1])
		    tempcount++;
	       else{
		    if(tempcount>max)
			 max = tempcount;

		    tempcount=1;
	       }
	  }
	  cout<<max<<endl;
     }
     return 0;
}
