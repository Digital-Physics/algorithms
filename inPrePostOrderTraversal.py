# for all three traversals the following complexity holds:
# time: O(n) since we visit each node
# space: O(n) because we build up and output an array...
# if we just printed the value, we could do it in O(h)
def inOrderTraverse(tree, array):
	if tree is not None:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array

# preorder means do what ever you want to do (append to list in this case) at start
def preOrderTraverse(tree, array):
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array

# postorder means do whatever you want to do at end
def postOrderTraverse(tree, array):
	if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array
