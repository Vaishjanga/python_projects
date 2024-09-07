import random
friends = ["Alice","Bob","Charlie","David","Emanuel"]


#method1
print(random.choice(friends))

#method2
random_index = random.randint(0 ,4)
print(friends[random_index])