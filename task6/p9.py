"""I can't understand how i could even begin to take input nor how to implement
    although i have an idea of how it might be implemented but i have taken this
    answer from one of the leetcode submissions after trying to understand what
    i could understand from it"""
    
    
class DetectSquares:
    def __init__(self):
        self.d = Counter()
        self.x_coord = defaultdict(Counter)

    def add(self, point):
        x, y = point
        self.d[x, y] += 1
        self.x_coord[x][y] += 1

    def count(self, point):
        x, y = point
        ans = 0
        for y2 in self.x_coord[x]:
            if y == y2: continue
            ans += self.d[x, y2] * self.d[x + y2 - y, y] * self.d[x + y2 - y, y2]
            ans += self.d[x, y2] * self.d[x + y - y2, y] * self.d[x + y - y2, y2]
        return ans