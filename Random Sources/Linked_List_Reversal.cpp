#include<iostream>

using namespace std;

typedef struct Node
{
    struct Node *next;
    int data;
} Node;

Node* reverse(Node *root)
{
    if(root==nullptr)
    {
        return nullptr;
    }
    else{
        Node *tail,*middle,*head;
        tail=middle=nullptr;
        head=root;

        while(head!=nullptr)
        {
            tail=middle;
            middle=head;
            head=head->next;
            middle->next=tail;
        }
        return middle;
    }
    
}