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
    
    // Create a list of all possible return options over i, for 0 <= i < n. 
    // Python could do this with a list comprehension but recursion limits are a dumb and stupid (safe, smart, responsible) idea. Let me write exponential algorithms!!!!!!
    vector<tuple<int, int, vector<int>>> options(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        // Get the value of C for the current i and n values. 
        int c_val = C[n - 1][i];

        // Use the remaining heights and widths. 
        vector<int> tmpHeights(i);
        vector<int> tmpWidths(i);
        for (int j = 0; j < i; ++j) {
            tmpHeights[j] = heights[j];
            tmpWidths[j] = widths[j];
        }

        // Get the return value.
        auto ret = program3(i - 1, tmpHeights, tmpWidths, C);

        // Create a temporary vector to be used in the tuple at the front, and add the length of its row. We add to the front because we construct our solution "backwards".
        vector<int> retvec = get<2>(ret);
        retvec.insert(retvec.begin(), n - i);

        // Add the tuple to the list. 
        options[i] = make_tuple(1 + get<0>(ret), c_val + get<1>(ret), retvec);
    }

    // Construct final return value. 
    // Ugly lambda comparator because I just need something to work; gets the smallest tuple based on the cost (value at index 1). 
    auto result = *min_element(options.begin(), options.end(), 
        [](const auto& a, const auto& b) {
            return get<1>(a) < get<1>(b);
        });
    return result;
}

// tuple<int, int, vector<int>> program3(int n, vector<int> heights, vector<int> widths, const vector<vector<int>> C){
//     // Check for invalid input. 
//     if (n < 1) {
//         return make_tuple(0, 0, heights);
//     }

//     // Base case.
//     else if (n == 1) {
//         return make_tuple(1, heights[0], vector<int>({1}));
//     }
    
//     // Get the minimum value of C_ij.
//     auto it = min_element(C[n - 1].begin(), C[n - 1].end());
//     int max_C = *it;

//     // Calculate the index of the best value of i, and get the preceding index (subtract 1). 
//     int next_n = distance(C[n - 1].begin(), it) - 1;

//     vector<int> tmpHeights(next_n);
//     vector<int> tmpWidths(next_n);
//     for (int i = 0; i < next_n; ++i) {
//         tmpHeights[i] = heights[i];
//         tmpWidths[i] = widths[i];
//     }

//     // Construct return value. 
//     auto val = program3(next_n, tmpHeights, tmpWidths, C);
//     return make_tuple(1 + get<0>(val), max_C + get<1>(val), vector<int>{0});
// }


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

    // Create a new vector using the max integer size (in place of infinity).
    vector<vector<int>> c(n, vector<int>(n, numeric_limits<int>::max()));

    /*
    * WORKING:
    * Iterate over all c_ij values to determine the height of the tallest painting in all possible rows of width W. 
    * This list accessed with the n'th sculpture used as the first index, and the i value used as the second. 
    */
    for (int j = n; j > 0; --j) {
        for (int i = 0; i < j - 1; ++i) {
            vector<int> tmpWidths(widths.begin() + i, widths.begin() + j);
            int sum = accumulate(tmpWidths.begin(), tmpWidths.end(), 0);
            
            if (sum <= W) {
                c[j - 1][i] = *max_element(heights.begin() + i, heights.begin() + j); 
            }
        }
    }

    // // Create a vector of results. I am going to vomit. This is so ugly and terrible. 
    // vector<tuple<int, int, vector<int>>> results;
    // for (int i = 0; i < n - 1; ++i) {
    //     results.push_back(program3(i, heights, widths, c));
    // }

    // // Ugly lambda comparator because I just need something to work. 
    // // Gets the smallest tuple based on the cost (value at index 1). 
    // auto result = *min_element(results.begin(), results.end(), 
    //     [](const auto& a, const auto& b) {
    //         return get<1>(a) < get<1>(b);
    //     });

    auto result = program3(n, heights, widths, c);

    // Print the smelly results. 
    cout << get<0>(result) << endl;
    cout << get<1>(result) << endl;
    for(int i = 0; i < get<0>(result); i++){
        cout << get<2>(result)[i] << endl;
    }
    return 0; 
}