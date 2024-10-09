def arrange_paintings_unimodal(n, W, heights, widths):
    rows = []  # num items on each row
    i = 0  # index
    cur_row_width = 0  # current row's width
    curr_row = 0  # number of items in the current row
    total_height = 0  # total height (cost)
    prev_height = heights[0]  # previous painting's height
    minimum_found = False

    while i < n:
        if cur_row_width + widths[i] <= W:
            if cur_row_width == 0:
                total_height += heights[i]
            if not minimum_found:
                if heights[i] <= prev_height or (i < n - 1 and heights[i] == heights[i + 1]):
                    curr_row += 1
                    cur_row_width += widths[i]
                    prev_height = heights[i]
                else:
                    minimum_found = True
                    rows.append(curr_row)
                    cur_row_width = widths[i]
                    curr_row = 1
                    prev_height = heights[i]
                    total_height += heights[i]
            else:
                if heights[i] >= prev_height or (i < n - 1 and heights[i] == heights[i + 1]):
                    curr_row += 1
                    prev_height = heights[i]
                    cur_row_width += widths[i]
            i += 1
        else:
            rows.append(curr_row)
            curr_row = 0
            cur_row_width = 0
    if curr_row > 0:
        rows.append(curr_row)
    return len(rows), total_height, rows



if __name__ == '__main__':
    n = 6
    W = 10
    heights = [10, 8, 5, 6, 7, 9]
    widths = [3, 2, 1, 2, 1, 1]
    result = arrange_paintings_unimodal(n, W, heights, widths)
    print(result)
