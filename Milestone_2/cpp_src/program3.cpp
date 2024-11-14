#include <iostream>
#include <vector>
#include <tuple>
#include <limits>
#include <numeric>
#include <algorithm>
using namespace std;
#define WIDTH_EXCEEDED numeric_limits<int>::max()
/* Solution to program 3
* @param n the number of paintings
* @param heights the heights of the paintings
* @param widths the widths of the paintings
* @param &C a reference to the nested vector containing all C_ij values
* @return a tuple containing the number of platforms used, the optimal total height, and the number of paintings on each platform
*/
// if needed, this could (probably) be modified to include a static variable for C_ij instead of passing in a reference for every call, but that will only be done if we are not allowed to modify the function header. 
tuple<int, int, vector<int>> program3(int n, vector<int> heights, vector<int> widths, const vector<vector<int>>& C){
    // Check for invalid input. 
    bool n_small = n < 1;
    if (n_small) {
        return make_tuple(0, 0, vector<int>({}));
    }

    // Base case.
    else if (n == 1) {
        return make_tuple(1, heights[0], vector<int>({1}));
    }
    
    /*
    * Create a list of all possible return options over i, for 0 <= i <= n - 1. 
    * Python could do this with a list comprehension but recursion limits are a dumb and stupid (safe, smart, responsible) idea. Let me write exponential algorithms!!!!!!
    */
    vector<tuple<int, int, vector<int>>> options;
    auto& c_n = C[n - 1];
    for (int i = 0; i < n; ++i) {
        // Get the value of C for the current i and n values. 
        int c_val = c_n[i];

        // Only include values for which the width is valid.
        if (c_val == WIDTH_EXCEEDED) {
            continue;
        }

        // Use the remaining heights and widths. 
        vector<int> tmpHeights(i);
        vector<int> tmpWidths(i);
        for (int j = 0; j < i; ++j) {
            tmpHeights[j] = heights[j];
            tmpWidths[j] = widths[j];
        }

        // Get the return value.
        auto ret = program3(i, tmpHeights, tmpWidths, C);

        // Only add a row if we are not in the n < 1 case. 
        int rows = !n_small + get<0>(ret);

        // Calculate the cost of the now-constructed row. 
        int cost = c_val + get<1>(ret);

        // Create a temporary vector to be used in the tuple at the front, and add the length of its row. We add to the front because we construct our solution "backwards".
        vector<int> row_lengths = get<2>(ret);

        // Bounds check.
        if (!n_small) {
            // Insert length of row. 
            row_lengths.push_back(n - i);
        }

        // Add the tuple to the list. 
        options.push_back(make_tuple(rows, cost, row_lengths));
    }

    // Construct final return value. 
    // Ugly lambda comparator because I just need something to work; gets the smallest tuple based on the cost (value at index 1). 
    auto result = *min_element(options.begin(), options.end(), 
        [](const auto& a, const auto& b) {
            return get<1>(a) < get<1>(b);
        });
    return result;
}


int main() {
    // Read problem parameters from user input.  
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

    // Create a new vector for all C_ij values.
    vector<vector<int>> c(n);

    /*
    * Iterate over all c_ij values to determine the height of the tallest painting in all possible rows of width W. 
    * This list accessed with the n'th painting used as the first index, and the i value used as the second. 
    */

    for (int j = n; j > 0; --j) {
        c[j - 1].reserve(j);

        int max_height = 0;
        int curr_width = 0;

        for (int i = j; i > 0; --i) {
            curr_width += widths[i - 1];

            if (curr_width > W) {
                max_height = WIDTH_EXCEEDED;
            }
            else if (max_height < heights[i - 1]) {
                max_height = heights[i - 1];
            }

            c[j - 1][i - 1] = max_height;
        }
    }

    // Print the result.
    auto result = program3(n, heights, widths, c);

    cout << get<0>(result) << endl;
    cout << get<1>(result) << endl;
    for(int i = 0; i < get<0>(result); i++){
        cout << get<2>(result)[i] << endl;
    }
    return 0; 
}