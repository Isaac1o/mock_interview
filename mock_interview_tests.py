# A BST node
class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Recursive function to insert an key into BST
def insert(root, x):
    if root == None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    elif x > root.data:
        root.right = insert(root.right, x)
    return root


def test_kth_smallest(kthSmallest):
    keys = [
        [20, 8, 22, 4, 12, 10, 14],
        [5, 5, 5, 3, 4, 7, 1, 100, 3, 1030],
        [2, 10],
        [num for num in range(1, 1000, 7)]
    ]
    for key in keys:
        root = None
        for x in key:
            root = insert(root, x)
        for k in [1, len(key)//2]:
            user_answer = kthSmallest(root, k)
            true_answer = kthSmallest_true(root, k)
            assert user_answer == true_answer, f"Your answer did not match the correct answer. {user_answer}!={true_answer}"
            print(f'Test Passed: {user_answer} == {true_answer}')


def kthSmallest_true(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.data
        root = root.right


# Anagram Question
def anagram_group(str_list):
    cfd_str_list = {}
    for s in str_list:
        cfd = {}  # Character frequency table
        for char in s:
            if char in cfd.keys():
                cfd[char] += 1
            else:
                cfd[char] = 1

        # Sort the dictionary by key
        cfd = dict(sorted(cfd.items()))

        # Flatten cfd into a single string
        cfd_str = ''.join([f'{key}{value}' for key, value in cfd.items()])

        # Anagrams will produce identical cfd_str
        if cfd_str not in cfd_str_list:
            cfd_str_list[cfd_str] = [s]
        else:
            cfd_str_list[cfd_str].append(s)

    answer = []
    for anagrams in cfd_str_list.values():
        answer.append(anagrams)

    return answer


def anagram_group_test(anagram_user):
    input1 = ['abc', 'abd', 'cab', 'bad', 'bca', 'acd']
    output1 = [['abc', 'cab', 'bca'], ['abd', 'bad'], ['acd']]
    input2 = ['car', 'far', 'arc', 'rac', 'pool', 'olop', 'hiking']
    output2 = [['car', 'arc', 'rac'], ['far'], ['pool', 'olop'], ['hiking']]
    input3 = ['msds']
    output3 = [['msds']]

    assert anagram_user(input1) == output1, f'{anagram_user(input1)}!={output1}'
    print('Test 1 passed')
    assert anagram_user(input2) == output2, f'{anagram_user(input2)}!={output2}'
    print('Test 2 passed')
    assert anagram_user(input3) == output3, f'{anagram_user(input3)}!={output3}'
    print('Test 3 passed')