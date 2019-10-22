"""
File: node.py
定义一个单链表节点类
"""
class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
"""
File: testnode.py
测试节点类。
"""

head = None

#创建一个单链表结构
for count in range(1,6):
    head = Node(count,head)
    print(head.data,head.next)

#输出节点内容，输出完后，单链表结构也销毁了
while head != None:
    print(head.next)  #输出：5, 4, 3, 2, 1
    head = head.next
