# A Huffman Tree Node
class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

        # tree parent
        self.parent = ''


""" A helper function to calculate the probabilities of symbols in given data"""


def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


""" A helper function to print the codes of symbols by traveling Huffman Tree"""
codes = dict()


def Calculate_Codes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)

    if(node.left):
        Calculate_Codes(node.left, newVal)
    if(node.right):
        Calculate_Codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal

    return codes


""" A helper function to obtain the encoded output"""


def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
      #  print(coding[c], end = '')
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string


""" A helper function to calculate the space difference between compressed and non compressed data"""


def Total_Gain(data, coding):
    # total bit space to stor the data before compression
    before_compression = len(data) * 8
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        # calculate how many bit is required for that symbol in total
        after_compression += count * len(coding[symbol])
    print("Space usage before compression (in bits):", before_compression)
    print("Space usage after compression (in bits):",  after_compression)


def Huffman_Encoding(data):
    symbol_with_probs = Calculate_Probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols: ", symbols)
    print("probabilities: ", probabilities)

    nodes = []

    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)
        # for node in nodes:

        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1
        left.parent = left.symbol+right.symbol
        right.parent = left.symbol+right.symbol

        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol +
                       right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = Calculate_Codes(nodes[0])
    print("symbols with codes", huffman_encoding)
    Total_Gain(data, huffman_encoding)
    encoded_output = Output_Encoded(data, huffman_encoding)
    return encoded_output, nodes[0]


def Huffman_Decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        # print(x)
        if x == '1':
            # print('before',huffman_tree.symbol)
            huffman_tree = huffman_tree.right
            # print('after',huffman_tree.symbol)
        elif x == '0':
            # print('before',huffman_tree.symbol)
            huffman_tree = huffman_tree.left
            # print('after',huffman_tree.symbol)
        try:
            # print('left.symbol',huffman_tree.left.symbol)
            # print('right.symbol',huffman_tree.right.symbol)
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            # print(decoded_output)
            huffman_tree = tree_head
    string = ''.join([str(item) for item in decoded_output])
    return string


""" Function to visualize huffman tree """
# It does reverse inorder traversal


def print_tree_util(root, space, markers):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += markers[0]

    # Process right child first
    print_tree_util(root.right, space, markers)

    # Print current node after space
    print(''.rjust((space), ' '), end="")

    if 1 in {root.code}:  # if node is on the right
        print(f'┌-----[{root.code}] ["{root.symbol}"] [{len(root.symbol)}]')
    elif 0 in {root.code}:  # if node is on the left
        print(f'└-----[{root.code}] ["{root.symbol}"] [{len(root.symbol)}]')
    else:  # if node is root
        print(f'------["{root.symbol}"] [{len(root.symbol)}]')

    # Process left child
    print_tree_util(root.left, space, markers)

# Wrapper over print_tree_util()


def print_huffman_tree(root, spaces=None):
    if not spaces:
        # sets the distances between levels by the length of the root
        markers = [(len(f'[ ] ["{root.symbol}"] [{len(root.symbol)}]'))]
        space = 0 - markers[0]
    else:
        # users sets the space
        markers = [spaces]
        space = 0 - spaces
    print_tree_util(root, space, markers)

# DRIVERCODE

print('''
      INI ADALAH HASIL KOMPRESI HUFFMAN CODE DAN HUFFMAN TREE
      ''')

data = "YUDI HADIANTO"
encoding, huffman_trees = Huffman_Encoding(data)
print("Encoded output / Huffman code :", encoding)
print("Decoded Output / Original Text:",
      Huffman_Decoding(encoding, huffman_trees))
print_huffman_tree(huffman_trees, 20)

# ENCODING

def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        print(element)
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
        print(symbols)
    return symbols


print('''
      #### INI ADALAH HASIL CALCULATION PROBABILITY ####
      ''')


data = "YUDI HADIANTO"
print(data)
symbol_with_probs = Calculate_Probability(data)


# CALCULATE PROBABILITY

def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        # print(element)
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
        # print(symbols)
    return symbols


print('''
      #### INI ADALAH HASIL CALCULATION PROBABILITY ####
      ''')


data = "YUDI HADIANTO"
print(data)
symbol_with_probs = Calculate_Probability(data)
print('symbol_with_probs :', symbol_with_probs)
symbols = symbol_with_probs.keys()
probabilities = symbol_with_probs.values()
print("symbols: ", symbols)
print("probabilities: ", probabilities)


class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

        # tree parent
        self.parent = ''


# converts into object
nodes = []
for symbol in symbols:
    nodes.append(Node(symbol_with_probs.get(symbol), symbol))

# print the entire object
for i in nodes:
    print(i.__dict__)


def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        # print(element)
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
        # print(symbols)
    return symbols


data = "YUDI HADIANTO"
print(data)
symbol_with_probs = Calculate_Probability(data)
print('symbol_with_probs :', symbol_with_probs)
symbols = symbol_with_probs.keys()
probabilities = symbol_with_probs.values()
print("symbols: ", symbols)
print("probabilities: ", probabilities)


class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

        # tree parent
        self.parent = ''


# converts into object
nodes = []
for symbol in symbols:
     nodes.append(Node(symbol_with_probs.get(symbol), symbol))

# print the entire object
# for i in nodes:
    # print(i.__dict__)

# looping to create huffman tree
i = 1
while len(nodes) > 1:

    # sort all the nodes in ascending order based on their probability

    nodes = sorted(nodes, key=lambda x: x.prob)

    print('\niteration number : ', i)

    # to visualize the making of huffman tree
    for node in nodes:
        print(node.symbol, node.prob)
        try:
                print('left', node.left.__dict__)
                print('right', node.right.__dict__)
        except:
            pass

    # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        left.parent = left.symbol+right.symbol
        right.parent = left.symbol+right.symbol

        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol +
                       right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
        i += 1
# loop ended
print('\ncreated huffman tree : ')
print(nodes[0].__dict__)
