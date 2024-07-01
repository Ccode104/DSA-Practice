#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> array;

    ifstream in("input.txt", ios::in);

    /*
            As long as we haven't reached the end of the file, keep reading entries.
    */

    int number; // Variable to hold each number as it is read

    while (in >> number)
    {
        // Add the number to the end of the array
        array.push_back(number);
    }

    // Close the file stream
    in.close();

    vector<int>::iterator ptr;
    int max_sum = 0;
    int max_till_now = 0;

    for (ptr = array.begin(); ptr < array.end(); ptr++)
    {
        if (max_till_now + (*ptr) > max_sum)
        {
            // Update max sum
            max_sum = max_till_now + (*ptr);
        }
        if (max_till_now + (*ptr) > max_till_now)
        {
            //Update max_till_now
            max_till_now += (*ptr);
        }
        else if (max_till_now + (*ptr) < 0)
        {
            //Update max_till_now to 0 if -ve
            max_till_now = 0;
        }
    }

    cout << max_sum;

    return 0;
}