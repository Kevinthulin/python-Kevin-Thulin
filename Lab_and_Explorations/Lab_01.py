import matplotlib.pyplot as plt

# Import data from txt files
with open("datapoints.txt", "r") as f:
    data = f.readlines()[1:]
    datapoints = [(float(point.split(",")[0]), float(point.split(",")[1]), int(point.split(",")[2])) for point in data]

with open("testpoints.txt", "r") as f:
    data = f.readlines()[1:]
    testpoints = [(float(point.split(",")[0].split("(")[1]), float(point.split(",")[1].split(")")[0])) for point in data]

# Function to calculate distance
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Function to classify a point
def classify(point):
    distances = [(distance(point, datapoint), datapoint[2]) for datapoint in datapoints]
    distances.sort(key=lambda x: x[0])
    nearest_10 = distances[:10]
    pichus = sum(1 for d in nearest_10 if d[1] == 0)
    pikachus = 10 - pichus
    return 0 if pichus > pikachus else 1

# Classify the testpoints from the file
results = [classify(testpoint) for testpoint in testpoints]

# Generate the output for each test point
output_strings = []
for testpoint, result in zip(testpoints, results):
    classification = "Pikachu" if result == 1 else "Pichu"
    output_strings.append(f"Sample with (width, height): {testpoint} classified as {classification}")

output_strings

