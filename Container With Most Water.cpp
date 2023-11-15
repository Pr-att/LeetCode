#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    static int maxArea(const vector<int> &height)
    {
        const int n = height.size();
        int j = n - 1;
        int i = 0;
        int Max = 0;
        int temp = 0;
        while (i < j)
        {
            if (height[j] < height[i])
            {
                temp = (j - i) * (height[j]);
                j--;
            }
            else
            {
                temp = (j - i) * (height[i]);
                i++;
            }
            Max = max(Max, temp);
        }
        return Max;
    }
};

int main(int argc, const char **argv)
{
    const vector<int> nums = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << Solution::maxArea(nums);
}
