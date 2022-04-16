# time: O(n*c)? # but we don't fill out the whole table... but it feels like 2**n
# space: O(n*c)?
def knapsackProblem(items, capacity):
    i = len(items) - 1
    j = capacity

    idxs_not_skipped_yet = [i for i in range(len(items))]

    # idxs going in are carried all the way to the bottom before they start getting eliminated on the output
    value, idx_used, _ = val(i, j, idxs_not_skipped_yet, items)

    return [value, idx_used]


def val(i, j, idxs_not_skipped_yet, items):
    print()
    print("get the val of item i w/ capacity j:", i, j)
    print("item", i, items[i])
    print("idx in play", idxs_not_skipped_yet)

    if i == 0:
        if items[0][1] > j:
            print("return a base case value of 0 (and one less item)")
            return 0, idxs_not_skipped_yet[1:], items
        else:
            print("return a base case value of", items[0][0], "and don't eliminate the item")
            return items[0][0], idxs_not_skipped_yet, items

    # compare two cell values
    # 1) value of looking at the (imaginary grid) cell directly above where you don't use current item i
    no_item_val, items_idx, _ = val(i - 1, j, idxs_not_skipped_yet, items)

    # don't want to subtract off an item weight if it leaves us a negative residual capacity
    if 0 <= j - items[i][1]:
        # 2) value of adding the value of current item i to the max value of the cell less the current item's weight
        add_item_val, items_idx2, _ = val(i - 1, j - items[i][1], idxs_not_skipped_yet, items)
        # compare the two cells and take the max (also return the leftover items still in play)
        if no_item_val < add_item_val + items[i][0]:
            return (add_item_val + items[i][0]), items_idx2, items

    # other cell is the winner of the Max if you don't Return anything by this point
    # the winning cell is the one with the same value (i.e. you don't use item i)
    # ...so the second value returned omits this index from the items still in play
    idx = items_idx.index(i)
    new_idx = items_idx[:idx] + items_idx[idx + 1:]
    return no_item_val, new_idx, items

# maybe we should have memoized it to avoid any 2**n issues??
# although memoized version took longer to run... hmmm
# was the memoized cache that we needed to pass around getting too big??
# or is it the fact that certain calls aren't using the most up-to-date memoization???... perhaps we needed a class object w/ shared memo
def knapsackProblem2(items, capacity):
    i = len(items) - 1
    j = capacity

    idxs_not_skipped_yet = [i for i in range(len(items))]

    # memoization
    val_cache = {}

    # idxs going in are carried all the way to the bottom before they start getting eliminated on the output
    value, idx_used, _ = val2(i, j, idxs_not_skipped_yet, items, val_cache)

    return [value, idx_used]


def val2(i, j, idxs_not_skipped_yet, items, val_cache):
    keys = i, j, *idxs_not_skipped_yet
    print(val_cache)
    if keys in val_cache:
        print("already cached")
        return val_cache[keys]
    else:
        print()
        print("get the val of item i w/ capacity j:", i, j)
        print("item", i, items[i])
        print("idx in play", idxs_not_skipped_yet)
        if i == 0:
            if items[0][1] > j:
                print("return a base case value of 0 (and one less item)")
                val_cache[keys] = 0, idxs_not_skipped_yet[1:], items
                return val_cache[keys]
            else:
                print("return a base case value of", items[0][0], "and don't eliminate the item")
                val_cache[keys] = items[0][0], idxs_not_skipped_yet, items
                return val_cache[keys]

        # compare two cell values
        # 1) value of looking at the (imaginary grid) cell directly above where you don't use current item i
        no_item_val, items_idx, _ = val2(i - 1, j, idxs_not_skipped_yet, items, val_cache)

        # don't want to subtract off an item weight if it leaves us a negative residual capacity
        if 0 <= j - items[i][1]:
            # 2) value of adding the value of current item i to the max value of the cell less the current item's weight
            add_item_val, items_idx2, _ = val2(i - 1, j - items[i][1], idxs_not_skipped_yet, items, val_cache)
            # compare the two cells and take the max (also return the leftover items still in play)
            if no_item_val < add_item_val + items[i][0]:
                val_cache[keys] = (add_item_val + items[i][0]), items_idx2, items
                return val_cache[keys]

        # other cell is the winner of the Max if you don't Return anything by this point
        # the winning cell is the one with the same value (i.e. you don't use item i)
        # ...so the second value returned omits this index from the items still in play
        idx = items_idx.index(i)
        new_idx = items_idx[:idx] + items_idx[idx + 1:]
        val_cache[keys] = no_item_val, new_idx, items
        return val_cache[keys]


