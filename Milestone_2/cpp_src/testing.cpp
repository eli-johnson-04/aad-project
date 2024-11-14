#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <chrono>
#include <algorithm>
#include <numeric>
#include <limits>

using namespace std;

#define WIDTH_EXCEEDED numeric_limits<int>::max()

struct program3_resetter {
    static int& get_count() {
        static int count = 0;
        return count;
    }
};

void reset_program3_counter() {
    program3_resetter::get_count() = 0;
}

tuple<int, int, vector<int>> program3(int n, vector<int> heights, vector<int> widths, const vector<vector<int>>& C){
    static int& count = program3_resetter::get_count();
    ++count;
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
    const vector<int>& c_n = C[n - 1];
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
        tuple<int, int, vector<int>> ret = program3(i, tmpHeights, tmpWidths, C);

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
        options.push_back(make_tuple(count, cost, row_lengths));
    }

    // Construct final return value. 
    // Ugly lambda comparator because I just need something to work; gets the smallest tuple based on the cost (value at index 1). 
    tuple<int, int, vector<int>> result = *min_element(options.begin(), options.end(), 
        [](const auto& a, const auto& b) {
            return get<1>(a) < get<1>(b);
        });
    return result;
}

const int NUM_TEST_AVERAGES = 5;
const int SIZE_MULTIPLES = 5;
const int SIZE_FACTOR = 15;

int main() {
    string outFile = "../test3.csv";
    ofstream out(outFile, ios::out | ios::trunc);
    if (!out.is_open()) {
        cerr << "Failed to open output file: " << outFile << endl;
        return 1;
    }

    out << "Input Size,Execution Time" << endl;

    vector<vector<int>> sizes;
    int W = 10;

    for (int i = 1; i <= SIZE_MULTIPLES; ++i) {
        sizes.push_back(vector<int>(i * SIZE_FACTOR));
        for (int j = i * SIZE_FACTOR; j > 0; --j) {
            sizes[i - 1][j - 1] = rand() % (SIZE_FACTOR * SIZE_MULTIPLES) + 1;
        }
    }

    cout << "Number of paintings to be used for test run: ";
    for (const auto& size : sizes) {
        cout << size.size() << " ";
    }
    cout << endl;

    for (const auto set : sizes) {
        cout << "Testing " << set.size() << " paintings..." << endl;
        vector<int> widths(set.size());
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(1, 10);

        for (auto& width : widths) {
            width = dis(gen);
        }

        vector<vector<int>> C(set.size(), vector<int>(set.size(), 0));
        for (int j = set.size(); j > 0; --j) {
            for (int i = 0; i < j; ++i) {
                int ij_width = 0;
                for (int k = i; k < j; ++k) {
                    ij_width += widths[k];
                }
                if (ij_width <= W) {
                    C[j - 1][i] = *max_element(set.begin() + i, set.begin() + j);
                } else {
                    C[j - 1][i] = WIDTH_EXCEEDED;
                }
            }
        }

        vector<double> times(NUM_TEST_AVERAGES, 0.0);
        for (int i = 0; i < NUM_TEST_AVERAGES; ++i) {
            cout << "Running test " << i + 1 << "...";
            reset_program3_counter();
            auto start = chrono::high_resolution_clock::now();
            tuple<int, int, vector<int>> result = program3(set.size(), set, widths, C);
            auto end = chrono::high_resolution_clock::now();
            times[i] = chrono::duration<double>(end - start).count();
            cout << "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\bRun " << i + 1 << " of " << NUM_TEST_AVERAGES << " complete with " << get<0>(result) << " recursive calls." << endl;
        }

        double avg = accumulate(times.begin(), times.end(), 0.0) / NUM_TEST_AVERAGES;
        out << set.size() << "," << avg << endl;
    }

    cout << "Program test complete. Check for " << outFile << " in parent directory." << endl;
    return 0;
}