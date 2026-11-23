
#include <iostream>
#include <climits>
#include <cstdlib>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long rev = 0;
        long long n = abs((long long)x);
        while (n > 0) {
            int digit = n % 10;
            rev = rev * 10 + digit;
            n /= 10;
        }
        if (x < 0) {
            rev = -rev;
        }
        if (rev < INT_MIN || rev > INT_MAX) {
            return 0;
        }
        return (int)rev;
    }
};

int main() {
    int x = -123;

    Solution obj;

    cout << obj.reverse(x);

    return 0;
}