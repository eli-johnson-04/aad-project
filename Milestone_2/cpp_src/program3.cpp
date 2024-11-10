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
tuple<int, int, vector<int>> program3(int n, vector<int> heights, vector<int> widths, const vector<vector<int>> C){
    // Check for invalid input. 
    if (n < 1) {
        return make_tuple(0, 0, heights);
    }

    // Base case.
    else if (n == 1) {
        return make_tuple(1, heights[0], vector<int>({1}));
    }
    
    // Get the minimum value of C_ij.
    auto it = min_element(C[n - 1].begin(), C[n - 1].end());
    int min_C = *it;

    // Calculate the index of the best value of i. 
    int next_n = distance(C[n - 1].begin(), it);

    vector<int> tmpHeights(next_n);
    vector<int> tmpWidths(next_n);
    for (int i = 0; i < next_n; ++i) {
        tmpHeights[i] = heights[i];
        tmpWidths[i] = widths[i];
    }

    // Construct return value. 
    auto ret = make_tuple(min_C + get<0>(program3(next_n, tmpHeights, tmpWidths, C)), 0, vector<int>{0});
    return ret;
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
    for (int j = n; j > 0; --j) {
        for (int i = 0; i < j ; ++i) {
            vector<int> tmpWidths(widths.begin() + i, widths.begin() + j);
            int sum = accumulate(tmpWidths.begin(), tmpWidths.end(), 0);
            
            if (sum <= W) {
                c[j - 1][i] = *max_element(heights.begin() + i, heights.begin() + j); 
            }
        }
    }

    auto result = program3(n, heights, widths, c);

    cout << get<0>(result) << endl;
    cout << get<1>(result) << endl;
    for(int i = 0; i < get<0>(result); i++){
        cout << get<2>(result)[i] << endl;
    }
    return 0; 
}