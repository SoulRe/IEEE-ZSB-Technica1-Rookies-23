#needless to say this doesn't run on vscode aswell but it does on leet code
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #print(points)
        distances = []
         #k is the distance as specified in the explanation
        for i in range(len(points)):
            distance = sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            #making another nested list with its values having the distance and point at same index for easy sorting
            distances.append([distance, points[i]])
        #sorting the list of points and distances
        distances.sort()
        output = []
        #printing out however many he specified
        for i in range(k):
            #this stupid method is for the output he wants
            #it was easier to do it this way
            output.append(distances[i][1])
        return output