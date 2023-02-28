import random

# Define the percentage of features to randomize (between 0 and 100)
random_percent = 25

# Define a sample wheat seed cell (replace this with your own data)
wheat_seed = {'feature1': 10, 'feature2': 20, 'feature3': 30, 'feature4': 40, 'feature5': 50}

# Select a random subset of features to randomize
random_features = random.sample(list(wheat_seed.keys()), k=int(len(wheat_seed)*random_percent/100))

for feature in random_features:
    wheat_seed[feature] = random.randint(0, 100)
print(wheat_seed)
