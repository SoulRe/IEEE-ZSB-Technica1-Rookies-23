"""taking in the input as number of cities and space stations, then taking
    in the input for indicies of cities with space stations"""
def get_input():
    city = cities = []
    city = input("cities  stations:\n").split(" ")
    stations = input("cities which have stations: \n").split(" ")
    #making a nested list of cities with none of them having space stations
    for i in range(int(city[0])):
        cities.append([i, 0])
    #adding space stations to their specified cities
    for i in range(int(city[1])):
        cities[int(stations[i])][1] = 1
    return cities
        

def get_distance(cities):
        distance = []
        dist1 = dist2 = 0
        #looping through each city
        for i in range(len(cities)):
            #calculating distance from city the end of list
            for j in range(i, len(cities)):
                if cities[j][1] == 1:
                    dist1 = abs(j - i)
                    break
            #calculating the distance from city to the beginning of list
            for k in reversed(range(i)):
                if cities[k][1] == 1:
                    dist2 = abs(k - i)
                    break
            #adding the least distance to a list called distance
            distance.append(min(dist1, dist2))
        #returning the maximum distance
        return max(distance)
        

def main():
    cities = get_input()
    farthestdistance = get_distance(cities)
    print(f"Farthest distance = {farthestdistance}")
    
main()
    
    