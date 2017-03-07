def find_digits(digits1, digits2, digit_quantity_to_find):

    print('Inputs:')
    print('\tdigits1 = %s' % (digits1))
    print('\tdigits2 = %s' % (digits2))
    print('\tdigit_quantity_to_find = %d' % (digit_quantity_to_find))

    digit_count_by_input = [len(digits1), len(digits2)]
    positions_by_digit_input = [[[], []] for _ in range(10)]
    for i in range(digit_count_by_input[0]):
        positions_by_digit_input[digits1[i]][0].append(digit_count_by_input[0] - i - 1)
    for i in range(digit_count_by_input[1]):
        positions_by_digit_input[digits2[i]][1].append(digit_count_by_input[1] - i - 1)

    digits_found = []

    digit_quantity_left_to_find = digit_quantity_to_find
    digit_quantity_remaining_by_input = list(digit_count_by_input)

    # Search for the greatest available digit, given the constraint that a
    # digit can't be chosen if its selection would result in too few digits
    # remaining to construct a number of the specified length.  If multiple
    # candidates are found for the greatest digit, choose the one that is
    # furthest to the left in the input list, since its selection maximizes
    # the number of remaining digits for consideration in subsequent
    # positions.  If no candidates are found for the search digit, try again
    # using the next greatest digit.  If a digit is found, for the next
    # position, start a new search using the greatest digit again.

    search_digit = 9
    while digit_quantity_left_to_find > 0:

        print('digits_found = %s, digit_quantity_left_to_find = %d, search_digit = %d' % (digits_found, digit_quantity_left_to_find, search_digit))
        print('digit_quantity_remaining_by_input = %s' % (digit_quantity_remaining_by_input))

        final_candidates = [-1, -1]
        winner_index = -1
        for i in range(2):
            positions = positions_by_digit_input[search_digit][i]

            print('Step 0: positions_by_digit_input[%d][%d] = %s' % (search_digit, i, positions))

            # Remove digits whose positions have already been passed.  These
            # cannot be used now or in subsequent positions, so permanently
            # eliminate them from consideration.

            while len(positions) > 0 and positions[0] >= digit_quantity_remaining_by_input[i]:
                del positions[0]

            print('Step 1: positions_by_digit_input[%d][%d] = %s' % (search_digit, i, positions))

            # Filter out digits that, if chosen, would not leave enough
            # remaining digits to construct a number of the specified length.
            # These digits may be needed in subsequent positions, so just
            # eliminate them from consideration for now.

            candidates = list(positions)
            min_remaining_digits_in_list = digit_quantity_left_to_find - digit_quantity_remaining_by_input[(i + 1) % 2]
            candidates = [positions[j] for j in range(len(positions)) if positions[j] + 1 >= min_remaining_digits_in_list]

            print('Step 2: positions = %s' % (positions))

            # Given how the position list was initially built, elements that
            # are further to the left after filtering correspond to digits
            # that are further to the left in the input list.  Hence, choose
            # the first element of the list, if any, as this will maximize the
            # number of remaining digits for consideration in subsequent
            # positions.

            if len(candidates) > 0:
                final_candidates[i] = candidates[0]
                winner_index = i

        print('Step 3: final_candidates = %s, winner_index = %d' % (final_candidates, winner_index))

        # If a candidate was chosen from both lists, one must now be chosen as
        # the winner.  The best candidate is the one belonging to a list whose
        # remaining digits include a digit greater than the candidate digit.
        # If this is is the situation for both candidates, then the candidate
        # with the nearest greater digit is best.

        if final_candidates[0] != -1 and final_candidates[1] != -1:
            shortest_distances = [0, 0]
            for i in range(2):
                for j in range(digit_count_by_input[i] - final_candidates[i], digit_count_by_input[i]):
                    print(i, digit_count_by_input[i], digit_quantity_remaining_by_input[i], j)
                    if (digits1, digits2)[i][j] > search_digit:
                        shortest_distances[i] = final_candidates[i] - j
                        break

            winner_index = (0, 1)[shortest_distances[0] < shortest_distances[1]]

        print('Step 4: final_candidates = %s, winner_index = %d' % (final_candidates, winner_index))

        if winner_index != -1:
            digit_quantity_left_to_find -= 1
            digit_quantity_remaining_by_input[winner_index] = final_candidates[winner_index]
            digits_found.append(search_digit)
            search_digit = 9
        else:
            search_digit -= 1

    print('Output:\t%s' % (digits_found))

    return digits_found

if __name__ == '__main__':
    print(find_digits([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
    print(find_digits([6, 7], [6, 0, 4], 5))
    print(find_digits([3, 9], [8, 9], 3))
    print(find_digits([1,1,1,9,1], [1,1,9,1,1], 6))
    print(find_digits([1,1,1,9,1,0,0], [1,1,9,1,1,0,0], 10))
    print(find_digits([1,1,1,9,1,9,1], [1,1,9,1,1,9,1], 10))
    print(find_digits([6, 7], [6, 0, 8], 5))
    print(find_digits([6, 7], [6, 7, 8], 5))
