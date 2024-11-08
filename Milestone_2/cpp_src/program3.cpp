#include <iostream>
#include <vector>
#include <tuple>
#include <limits>
#include <numeric>
#include <algorithm>
using namespace std;
/* Solution to program 3
* @param n the number of paintings
* @param W the maximum width of the platform
* @param heights the heights of the paintings
* @param widths the widths of the paintings
* @return a tuple containing the number of platforms used, the optimal total height, and the number of paintings on each platform
*/
tuple<int, int, vector<int>> program3(int n, int W, vector<int> heights, vector<int> widths){
    /************************
    * ADD YOUR CODE HERE *
    ***********************/
//    return make_tuple(0, 0, vector<int>()); // replace with your own result.
    return make_tuple(n, 0, heights);
}
int main(){
    int n, W;
    cin >> n >> W;
    vector<int> heights(n);
    vector<int> widths(n);
    for(int i = 0; i < n; i++){
        cin >> heights[i];
    }
    for(int i = 0; i < n; i++){
        cin >> widths[i];
    }

    // Create a new vector using the max integer size (in place of infinity).
    vector<vector<int>> c(n, vector<int>(n, numeric_limits<int>::max()));

    /*
    * Iterate over all c_ij values to determine the height of the tallest painting in all possible rows of width W. 
    * This list accessed with the n'th sculpture used as the first index, and the i value used as the second. 
    */
    for (int j = n - 1; j > 0; --j) {
        for (int i = 0; i < j; ++i) {
            vector<int> tmpWidths(widths.begin() + i, widths.begin() + j + 1);
            int sum = accumulate(tmpWidths.begin(), tmpWidths.end(), 0);
            
            if (sum <= W) {
                c[j][i] = *max_element(heights.begin() + i, heights.begin() + j + 1); 
            }
        }
    }



    auto result = program3(n, W, heights, widths);

    cout << get<0>(result) << endl;
    cout << get<1>(result) << endl;
    for(int i = 0; i < get<0>(result); i++){
        cout << get<2>(result)[i] << endl;
    }
    return 0; 
}