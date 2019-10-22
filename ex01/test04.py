class Solution:
    def totalFruit(self, tree):
        i, j, p =0, 0, 0
        basket = [tree[0]]
        n = len(tree)
        max_fruit = 0
        while i < n-1:
            if tree[i+1] in basket:
                if tree[i] != tree[i+1]:
                    p = i+1
                i += 1
            elif len(basket) == 1:
                basket.append(tree[i+1])
                i += 1
                p = i
            elif len(basket) == 2:
                max_fruit = max(max_fruit, i - j + 1)
                j = p
                basket.remove(tree[p-1])
            max_fruit = max(max_fruit, i - j + 1)
        return max_fruit

obj = Solution()
print(obj.totalFruit([1,2,3,2,2]))
