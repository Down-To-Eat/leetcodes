
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        long long rev = 0;
        int n = x;

        while (n > 0) {
            int digit = n % 10;
            rev = rev * 10 + digit;
            n /= 10;
        }

        if (x < 0) {
            return false;
        }
        else if (x == rev) {
            return true;
        }
        else {
            return false;
        }
    }
};

int main() {
    int x = 121;

    Solution obj;

    cout << boolalpha << obj.isPalindrome(x);

    return 0;
}
