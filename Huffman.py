import heapq
import copy

class Node : 
    # 노드 클래스 
    # value = 빈도수, string = 문자, lit = 허프만코드가 입력됨
    def __init__ (self, string, value) :
        self.string = string
        self.value = value
        self.left = None
        self.right = None
        self.lit = []

    def __lt__ (self, other) :
        return self.value < other.value

class PriorityQueue() :
    def __init__(self) :
        self.queue = []
        self.count = 0

    def put(self, priority, v) : # 우선순위 큐를 실제로 구현 / 삽입연산
        self.count += 1
        heapq.heappush(self.queue, v)

    def get(self) : # 우선순위 큐의 pop연산
        self.count -= 1
        return heapq.heappop(self.queue)

    def display(self) : # 큐의 출력
        for i in range(self.count) :
            print('(', self.queue[i].string, ',', self.queue[i].value, ')')
        return None

l_freq = {'a' : 543, 'b' : 70, 'c' : 212, 'd' : 217, 'e' : 666, 'f' : 118, 'g' : 110, 
          'h' : 189, 'i' : 550, 'j' : 10, 'k' : 81, 'l' : 233, 'm' : 145 , 'n' : 437,
          'o' : 398, 'p' : 134, 'q' : 10, 'r' : 386, 's' : 410, 't' : 474, 'u' : 179,
          'v' : 77, 'w' : 85, 'x' : 8, 'y' : 89, 'z' : 4}
l_alpa = [Node(i, l_freq[i]) for i in l_freq.keys()]
# 각 알파벳에 맞춘 Node 생성 / Node에 빈도수 값과 문자값 저장
# <출처> http://lg-sl.net/product/infosearch/curiosityres/readCuriosityRes.mvc?curiosityResId=HODA2009020072
code_map = {'a' : '0000', 'i' : '0001', 'm' : '001000', 'v' : '0010010', 'k' : '0010011', 
            'w' : '0010100', 'y' : '0010101', 'u' : '001011', 'e' : '0011', 'r' : '01000', 
            'o' : '01001', 'h' : '010100', 'c' : '010101' , 's' : '01011', 'z' : '0110000000', 
            'x' : '0110000001', 'j' : '0110000010', 'q' : '0110000011', 'b' : '01100001', 
            'g' : '0110001', 'd' : '011001', 'n' : '01101', 't' : '01110', 'l' : '011110', 
            'f' : '0111110', 'p' : '0111111'}

class Huffman :
    def __init__ (self) :
        que_max = 26
        self.que = PriorityQueue()
        for i in range(que_max) :
            self.que.put(l_alpa[i].value, l_alpa[i])
        self.root = None

    def make_tree(self) :
        while (self.que.count != 1) :
            # 큐에 1개, 즉 루트노드만 남을때까지 부모만들기 반복
            Left = self.que.get()
            Right = self.que.get()
            parent = Node('', Left.value + Right.value)
            parent.left = Left
            parent.right = Right
            self.que.put(parent.value, parent) # 부모 만들고 계속 반복
        self.root = self.que.get()
        # 마지막남은 한 노드는 루트노드임
    # 허프만 코드의 트리 생성

    def Tableout(self) : 
        print("허프만 코드 표")
        self.Preorder(self.root, '0', [])
        # 각 노드의 테이블 생성

    def Preorder(self, node, n, li) :
        node.lit = copy.deepcopy(li)
        node.lit.append(n)
        if node.left == None and node.right == None :
            print(node.string,':', ''.join(node.lit))
            return
        if node.left != None :
            self.Preorder(node.left, '0', node.lit)
        if node.right != None :
            self.Preorder(node.right, '1', node.lit)
    # 각 노드에 허프만 코드값 생성
    # 각 노드에서의 허프만 코드값이 어떻게 되었는지 확인

    def Finding(self, li, node) :
        del li[0]
        if li == [] :
            return node.string
        elif li[0] == '0' :
            return self.Finding(li, node.left)
        elif li[0] == '1' :
            return self.Finding(li, node.right)

    def Find_char(self, li) :
        return self.Finding(li, self.root)
    # 변형하고자 하는 문자의 허프만코드를 리스트로 받음
    # 해당 문자를 찾아가는 형태

    def Find_string(self, li) :
        result = []
        for i in li :
            huf_code = list(i) # i문자열을 list로 변형
            result.append(self.Find_char(huf_code))
        return result
    # 허프만 코드를 알파벳으로 변경하여 단어 반환

if __name__ == '__main__' :
    out = Huffman() # 허프만코드 객체 생성
    out.make_tree() # 코드의 트리 생성
    out.Tableout()  # 코드의 테이블 확인

    inp = list(input("영어 단어 입력 (소문자입력)>> "))
    inp_huf = []
    for i in inp :
        inp_huf.append(code_map[i])

    print('당신이 입력한 문자의 허프만 코드 : ', inp_huf)
    print('허프만 코드의 알파벳 : ', ''.join(out.Find_string(inp_huf)))

