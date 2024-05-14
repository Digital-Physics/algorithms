class Node:
    def __init__(self, parent: int, left: "Node", right: "Node") -> None:
        self.parent = parent
        self.left = left
        self.right = right

def lowestCommonAncestor(a: Node, b: Node) -> Node:
    """Time: Avg: O(h) Worst: O(n)
    Space: Avg: O(h) Worst: O(n)"""
    visited = set()
    
    # go all the way to the root with one node
    while a is not None:
        visited.add(a)
        a = a.parent
    
    # as soon as the other node intersects, it will be
    while b is not None:
        if b in visited:
            return b
        else:
            b = b.parent

def lowestCommonAncestor2(a: Node, b: Node) -> Node:
    """assume a starts x depth levels above b. once it reaches the root first
    and resets to b (not a), it will take x steps to get back to level a. It won't
    necessarily be at a, because it could be on another branch, but it will be at 
    the same level. That's also the same point that PointerB will get reset to a.
    So they pointers will either be the same when pointerB resets, or they'll be the
    same within the next d steps, where d is their current depth. 
    
    e.g. 
    assume a is on the right branch at depth 2.
    assume b is on the left branch at depth 5.
    in 2 steps pointerA will be at depth 0
    in 2 steps pointerB will be at depth 3.
    in 1 more step pointerA will be at depth 5
    in 1 more step pointerB will be at depth 2
    in 3 more steps pointerA will be at depth 2
    in 3 more steps pointerB will be at depth 2 (reset in 2 steps to height 3)

    now pointer A == pointerB now or will match sometime in the next 2 steps.

    a_depth + x = b_depth
    b_depth + a_depth = a_depth + b_depth (total travel to get to root twice for each pointer)
    b_depth + a_depth -1  = a_depth + b_depth -1 (could meet before the root if they were on the same side)
    b_depth + a_depth -2  = a_depth + b_depth -2 (and maybe they could have met when pointerB was reset)

    space: O(1)
    time: avg: O(h), worst: O(n)
    """
    pointerA, pointerB = a, b
        
    while pointerA != pointerB:
        pointerA = pointerA.parent if pointerA.parent else b
        pointerB = pointerB.parent if pointerB.parent else a
            
    return pointerA


if __name__ == "__main__":
