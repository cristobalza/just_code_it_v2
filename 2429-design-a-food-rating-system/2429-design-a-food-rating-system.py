from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_foods = collections.defaultdict(SortedSet) # cuisine : (ratings, food)
        self.ratings = collections.defaultdict(int) # food: ratings
        self.cuisines = collections.defaultdict(str) # food : cuisine

        for i in range(len(foods)):
            self.cuisine_foods[cuisines[i]].add((-ratings[i], foods[i]))
            self.ratings[foods[i]] = ratings[i]
            self.cuisines[foods[i]] = cuisines[i]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.cuisines[food]
        rating = self.ratings[food]
        self.cuisine_foods[cuisine].remove((-rating, food))
        self.cuisine_foods[cuisine].add((-newRating, food))

        self.ratings[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_foods[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)