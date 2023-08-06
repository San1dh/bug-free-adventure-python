// random C program in Python programs :)

int n;
int a[n];
printf("input number of numbers: ");
 scanf("%d", &n);
int sum = 0;
printf("input numbers: ");
for(int i=0; i<n; i++)
{
  scanf("%d", &a[i]);
  sum += a[i];
}
mean = sum/n;
for(i=0; i<n; i++)
 for(int j=0; j<(n-1-1); j++)
  if(a[j]>a[j+1])
  {
    int temp = a[j];
    a[j] = a[j+1];
    a[j+1] = temp;
  }

  medpos = n/2;

if(n%2 == 0)
 int med = a[medpos];
else
 int med = (a[medpos]+a[medpos+1])/2
