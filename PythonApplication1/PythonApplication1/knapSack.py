class Knapsack:
    def __init__ (self, maxweight):
        self.Maxweight = maxweight
       
class Loot:
    def __init__ (self, name, value, weight):
        self.Name = name 
        self.Value = value 
        self.Weight = weight


combinationsArray = []
def getCombinations(array:[]):

    combinationsArray.append(array)
    if (array.length >= 1):
         for i in array:
             combinationsArray.append(i)
             getCombinations()




   







def main():
    k = Knapsack(160)
    

    sword = Loot("sword", 50, 150)
    ring = Loot("ring", 150, 10)
    coin = Loot("coin", 100, 10)
    stone = Loot("stone", 10, 100)

    lootList = []
    lootList.append(ring)
    lootList.append(coin)
    lootList.append(sword)
    lootList.append(stone)

    knapsackList = []

    currentweight = 0
    #for item in lootList:   
      #   if (currentweight + item.Weight <= k.Maxweight):
       #      knapsackList.append(item) 
        #     currentweight = currentweight + item.Weight
         #    print("added ", item.Name, " to knapsack")
          #   print(currentweight)
            
             
         
             










main()