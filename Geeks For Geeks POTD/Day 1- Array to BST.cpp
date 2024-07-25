//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val)
        : data(val)
        , left(nullptr)
        , right(nullptr) {}
};

bool help(Node* root, long long int up, long long int l) {
    if (root->data >= up || root->data <= l)
        return false;
    bool ans = true;
    if (root->left)
        ans = help(root->left, root->data, l);
    if (ans && root->right)
        ans = help(root->right, up, root->data);
    return ans;
}

bool isValidBST(Node* root) {
    return help(root, 3147483648, -3147483649);
}

int Height(Node* root) {

    if (root == NULL)
        return 0;

    int leftHeight = Height(root->left);

    int rightHight = Height(root->right);

    if (leftHeight == -1 || rightHight == -1 || abs(leftHeight - rightHight) > 1)
        return -1;

    return max(leftHeight, rightHight) + 1;
}

bool isBalanced(Node* root) {

    if (root == NULL)
        return true;

    if (Height(root) == -1)
        return false;
    return true;
}

void inorder(Node* root, vector<int>& v) {
    if (root == NULL)
        return;

    inorder(root->left, v);
    v.push_back(root->data);
    inorder(root->right, v);
}


// } Driver Code Ends
/*
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val)
        : data(val)
        , left(nullptr)
        , right(nullptr) {}
};
*/

class Solution {
  public:
    void height_bal(Node** root_ptr,vector<int>& nums,int start,int end)
    {
        Node *root=*root_ptr;
        //cout<<start<<" "<<end<<endl;
        if(start>=end)
        {
            //Nothing
        }
        else if(end-start==1)
        {
            root=new Node(nums[start]);
            //cout<<root->data;
        }
        else
        {
            root=new Node(nums[(int)((start+end)/2)]);
            if((end-start)%2==0)
            {
                height_bal(&(root->left),nums,start,(start+end)/2);
                height_bal(&(root->right),nums,((start+end)/2)+1,end);
            }
            else
            {
                height_bal(&(root->left),nums,start,(start+end)/2);
                height_bal(&(root->right),nums,((start+end)/2)+1,end);
            }
            
        }
        *root_ptr=root;
    }
    void in(Node *root)
    {
        if(root!=nullptr)
        {
            in(root->left);
            cout<<root->data;
            in(root->right);
        }
    }
    Node* sortedArrayToBST(vector<int>& nums) {
        // Code here
        
        Node *root;
        height_bal(&root,nums,0,nums.size());
        //in(root);
        return root;
        
        
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;

        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        Node* a = ob.sortedArrayToBST(arr);
        vector<int> v;
        inorder(a, v);

        if (!isValidBST(a) or v != arr) {
            cout << "false" << endl;
            return 0;
        }
        bool f = isBalanced(a);

        if (f)
            cout << "true";
        else
            cout << "false";
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends