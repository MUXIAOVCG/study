
class Solution:
    def pushpoint(self,heap,value):
            heap.append(value)
            index = len(heap) - 1
            while index != -1 :
                cur_c = heap[index]
                cur_p = heap[(index - 1) // 2]
                cur1 = cur_c[0] ** 2 + cur_c[1] ** 2
                cur2 = cur_p[0] ** 2 + cur_p[1] ** 2
                if cur1 < cur2:
                    heap[index], heap[(index - 1) // 2] = cur_p, cur_c
                    index = (index - 1) // 2
                else:
                    return
    def kClosest(self, points, K) :
        heap = []
        for value in points:
            self.pushpoint(heap,value)
        return heap[0]



obj = Solution()
print(obj.kClosest([[3,3],[5,-1],[-2,4]],2))






