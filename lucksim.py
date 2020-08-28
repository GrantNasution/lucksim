from random import randrange

def calcAvgGrad(graduates):
    sum = 0
    for _ in graduates:
        sum += _.luck
    return sum/len(graduates)

def calcAvg(arr):
    sum = 0
    for _ in arr:
        sum += _
    return sum/len(arr)

class Graduate:
    def __init__(self):
        self.skill = randrange(50, 100)
        self.luck = randrange(100)
        self.rating = (self.skill * .95) + (self.luck * .05)

    def __eq__(self, other):
        if not isinstance(other, Graduate):
            return NotImplemented
        return self.rating == other.rating
    
    def __lt__(self, other):
        if not isinstance(other, Graduate):
            return NotImplemented
        return self.rating < other.rating

    def __le__(self, other):
        if not isinstance(other, Graduate):
            return NotImplemented
        return self.rating <= other.rating

    def __ne__(self, other):
        if not isinstance(other, Graduate):
            return NotImplemented
        return self.rating != other.rating

    def __gt__(self, other):
        if not isinstance(other, Graduate):
            return NotImplemented
        return self.rating > other.rating

    def __ge__(self, other):
        if not isinstance(other, Graduate):
            return NotImplemented
        return self.rating >= other.rating

    def __str__(self):
        return "Rating: " + str(self.rating) + " | Skill: " + str(self.skill) + " | Luck: " + str(self.luck) 

with open('Avg_Luck.txt', 'w') as f:
    luckAvgs = []
    for i in range(0, 100):
        graduates = [Graduate() for _ in range(1000)]
        graduates.sort()
        luckAvg = calcAvgGrad(graduates[989:999])
        luckAvgs.append(luckAvg)
        f.write(str(luckAvg) + "\n")
    f.write("\nTotal Avg Luck:" + str(calcAvg(luckAvgs)))
    f.close()



