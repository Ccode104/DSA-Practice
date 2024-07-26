#include<iostream>
#include<cstddef>

using namespace std;


class Node
{
    public:
        Node *left,*right;
        int data;

        Node(int d)
        {
            left=right=NULL;
            data=d;
        }
};

int height(Node *root)
{
    if(root==NULL)
    {
        return 0;
    }
    else
    {
        int l=height(root->left);
        int r=height(root->right);

        if(l>r)
        {
            return l+1;
        }
        else{
            return r+1;
        }
    }
}