# note: this is not an algo expert problem
print("general approach:")
print("take one less than your stack height, and move those n-1 disks legally so they end up properly stacked on the auxiliary pole")
print("then move your bottom, biggest disk to the destination pole")
print("then move your your stack of n-1 disks from the orig_aux_pole, to the original end pole, using the orig_from_pole as auxiliary ")
print()
print("recursion is sort of like mathematical induction. make sure the base case is true. and then show you can climb ladder from n to n+1")
print("here we should think about base cases of 0, 1, 2, or even 3 disks, in our opinion...")
print("rationalizing what makes sense with a base case of 0s, empty sets, infinity, seems difficult.")
print("so just make sure our approach holds for 1 disk, or even 1 and 2, even if we don't/shouldn't code it in.")
print("so here, we convinced ourselves that by starting with a stack of 2, we could get the top disk to the aux pole legally...")
print("then move the bottom disk to the end pole, and then cover it with disk from the aux pole...")
print("note, this still possible with 3 disks, the first situation of where we need to designate different poles as aux at some point")
print()
print("the approach we are taking:")
print("1) get the entire stack of whatever is above the bottom disk to the pole currently designated as the aux pole")
print("2) then move the bottom disk to the destination")
print("3) then get the stack on the aux pole to the destination")
print()
print("Note: when we ignore the bottom disk, we're playing the same game but with one less disk...")
print("but if we know we really have this other disk to handle, then we'll play the game of moving the n-1 stack to the aux pole instead.")

def hanoi(num_of_disks, orig_from_pole_a, orig_aux_pole_b, orig_to_pole_c):
    print("num of disks:", num_of_disks)
    if num_of_disks == 0:
        return
    else:
        hanoi(num_of_disks-1, orig_from_pole_a, orig_to_pole_c, orig_aux_pole_b)
        move(orig_from_pole_a, orig_to_pole_c)
        hanoi(num_of_disks-1, orig_aux_pole_b, orig_from_pole_a, orig_to_pole_c)

def move(from_pole, to_pole):
    print(f"Move disk from {from_pole} to {to_pole}")

hanoi(2,"pole a", "pole b", "pole c")


