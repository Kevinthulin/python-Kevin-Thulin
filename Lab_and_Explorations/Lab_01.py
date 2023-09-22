# Promt the user with widght and height.
# Return the corrdiantes as a tuples of floats
def input_from_user():
    while True:
        try:
            height = float(input("Enter height: "))
            weight = float(input("Enter weight: "))
            if height <= 0 or weight <= 0:
                print("Enter a positive number for both height and wight")
                continue
            return height, weight
        except ValueError:
            print("Enter a number!")
        
    
# Read in the datapoints from a txt file and skip the header
def read_datapoints(datapoint):
    with open(datapoint, "r") as f:
        data = f.readlines()[1:]
    return [process_data_points(point) for point in data ]

#  Split the in three and convret them in to floats or int
def process_data_points(point):   
    x, y, label = point.split(",")
    return float(x), float(y), int(label)

# Read in the testpoints from a txt file and skip header
def read_testpoints(testpoints):
    with open(testpoints, "r") as f:
        data = f.readlines()[1:]
    return [process_test_point(point) for point in data]

# split testoints into two and start with ( and ends with )
def process_test_point(point):
    x_str, y_str = point.split(",")
    x = float(x_str.split("(")[1])
    y = float(y_str.split(")")[0])
    return x, y

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

testpoints = read_testpoints("testpoints.txt")
datapoints = read_datapoints("datapoints.txt")
user_points = input_from_user()
result = classify(user_points)
# Classify the testpoints from the file
results = [classify(testpoint) for testpoint in testpoints]

# Generate the output for each test point
output_strings = []
for testpoint, result in zip(testpoints, results):
    classification = "Pikachu" if result == 1 else "Pichu"
    output_strings.append(f"Sample with (width, height): {testpoint} classified as {classification}")


print("\n".join(output_strings))

classification = "Pikachu" if result == 1 else "Pichu"
print(f"Sample with (width, height): {user_points} and classified as {classification}")
