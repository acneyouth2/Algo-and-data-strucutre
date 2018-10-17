# Represents a Huffman tree for use in encoding/decoding strings.
# A sample usage is as follows:
#
# h = HuffmanTree([('A', 2), ('B', 7), ('C', 1)])
# assert(h.encode('ABC') == '01100')
# assert(h.decode(h.encode('ABC')) == 'ABC')
import heapq
from collections import defaultdict
class TreeNode:

  def __init__(self):
    self.left = None
    self.right = None
    self.symbol = None
    self.weight = 0
    self.min_element = None

  #in order to make TreeNode object comaparable based on their weigth and min_element
  # min_element is for ties such as (A:2)(B:1)(C:1), we can allocate A to the left.
  def __cmp__(self, other):
    return cmp((self.weight,self.min_element),( other.weight,other.min_element))

class HuffmanTree:
  # Helper object for building the Huffman tree.
  # You may modify this constructor but the grading script rlies on the left, right, and symbol fields.


  # The `symbol_list` argument should be a list of tuples `(symbol, weight)`,
  # where `symbol` is a symbol that can be encoded, and `weight` is the
  # the unnormalized probabilitiy of that symbol appearing.




  def __init__(self, symbol_list):
    assert(len(symbol_list) >= 2)
    # YOUR CODE HERE
    self.tree=[]
    self.dic=defaultdict()
    self.symbol_list=symbol_list
    self.buildTree(symbol_list)
    self.root = self.tree[0]# (place TreeNode object here)



  def buildTree(self,symbol_list):
    for i in symbol_list:
      node=TreeNode()
      node.weight=i[1]
      node.symbol=i[0]
      node.min_element=node.symbol
      heapq.heappush(self.tree,node)





    while len(self.tree)>1:

      node1=heapq.heappop(self.tree)
      node2=heapq.heappop(self.tree)

      new_node=TreeNode()
      new_node.min_element=min(node1.min_element,node2.min_element)

      new_node.left=node1
      new_node.right=node2
      new_node.weight=node1.weight+node2.weight
      heapq.heappush(self.tree,new_node)




  # Encodes a string of characters into a string of bits using the
  # symbol/weight list provided.

  def encodeHelper(self,root,char):
      ####


      if not root:
        return

      elif root.symbol:
        self.dic[root.symbol]=char



      self.encodeHelper(root.left,char+"0")
      self.encodeHelper(root.right,char+"1")



  def encode(self, s):
    assert(s is not None)
    # YOUR CODE HERE
    res=""
    self.buildTree(self.symbol_list)
    root=self.root
    self.encodeHelper(root,"")
    for char in s:
      res+=self.dic[char]

    return str(res)



  # Decodes a string of bits into a string of characters using the
  # symbol/weight list provided.
  def decode(self,s):
    assert(s is not None)
    # YOUR CODE HERE
    ans=""

    root=self.root
    if not s:
      return ""

    a = root
    for bit in s:

      if bit=="0":

        root=root.left
      else:
        root=root.right



      if not root.left and not root.right:
        ans+=root.symbol
        root=a

    if s!=self.encode(ans):
      return None

    return ans













