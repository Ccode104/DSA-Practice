#include<iostream>
#include <cstddef>
using namespace std;

class Node
{
    public:
        Node *right,*left;
        int data;
    public:
        Node()
        {
            left=right=NULL;
            data=0;
        }
};

bool checkMirror(Node *root1,Node *root2)
{
    if((root1==NULL)&&(root2==NULL))
    {
        return true;
    }
    else if(root1==NULL)
    {
        return false;
    }
    else if(root2==NULL)
    {
        return false;
    }
    else{
        if((root1->data==root2->data))
        {
            return ((checkMirror(root1->left,root2->right))&&(checkMirror(root2->left,root1->right)));
        }
        else
        {
            return false;
        }
    }
}
    