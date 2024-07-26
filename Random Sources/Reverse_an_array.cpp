#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> array;
    int N=0;

    //Input 
    cout<<"Enter the number of elements in the array\n";
    cin>>N;

    cout<<"Enter the elements now\n";

    int e;
    for(int i=0;i<N;i++)
    {
        cin>>e;
        array.push_back(e);
    }
    return 0;
}