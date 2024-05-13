"""Feature 1 - Which color of shirt is the mean color? """
# Provided data
data = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN,BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

# Function to count occurrences of each color
def count_colors(data):
    color_counts = {}
    for day, colors in data.items():
        for color in colors.split(','):
            color = color.strip()
            color_counts[color] = color_counts.get(color, 0) + 1
    return color_counts

# Find the mean color (most common color)
color_counts = count_colors(data)
mean_color = max(color_counts, key=color_counts.get)

print("Mean color of shirts:", mean_color)

"""End of this code"""

""" Features 2 - Which color is mostly worn throughout the week? """

# Count occurrences of each color
color_counts = {}
for day in data.values():
    for color in day.split(','):
        color = color.strip()
        color_counts[color] = color_counts.get(color, 0) + 1

# Find the color mostly worn throughout the week
most_worn_color = max(color_counts, key=color_counts.get)

print("Color mostly worn throughout the week:", most_worn_color)

"""End of this code"""

""" Features 3 - Which color is the median? """

# Count occurrences of each color
color_counts = {}
for day in data.values():
    for color in day.split(','):
        color = color.strip()
        color_counts[color] = color_counts.get(color, 0) + 1

# Sort colors based on their frequencies
sorted_colors = sorted(color_counts.items(), key=lambda x: x[1])

# Determine the median color
num_colors = len(sorted_colors)
if num_colors % 2 == 1:
    median_color = sorted_colors[num_colors // 2][0]
else:
    median_color = (sorted_colors[num_colors // 2 - 1][0], sorted_colors[num_colors // 2][0])

print("Median color(s):", median_color)

"""End of this code"""

""" Features 4 - Bonus: Get the variance of the colors
"""
# Count occurrences of each color
color_counts = {}
for day in data.values():
    for color in day.split(','):
        color = color.strip()
        color_counts[color] = color_counts.get(color, 0) + 1

# Calculate the mean frequency of colors
mean_frequency = sum(color_counts.values()) / float(len(color_counts))

# Calculate the variance
variance = sum((count - mean_frequency) ** 2 for count in color_counts.values()) / len(color_counts)

print("Variance of colors:", variance)

"""End of code"""

""" Features 5 - if a colour is chosen at random, what is the probability that the color is red? """

# Count occurrences of each color
color_counts = {}
for day in data.values():
    for color in day.split(','):
        color = color.strip()
        color_counts[color] = color_counts.get(color, 0) + 1

# Calculate total number of occurrences of all colors

total_occurrences = sum(color_counts.values())

# Calculate the probability of choosing the color red
probability_red = color_counts.get('RED', 0) / float(total_occurrences)

print("Probability of choosing the color red:", probability_red)

"""End of code"""

""" Features 6 - Save the colours and their frequencies in postgresql database
"""

import psycopg2

# Count occurrences of each color
color_counts = {}
for day in data.values():
    for color in day.split(','):
        color = color.strip()
        color_counts[color] = color_counts.get(color, 0) + 1

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

# Create table to store colors and

frequencies if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(50) PRIMARY KEY,
        frequency INTEGER
    )
""")

# Insert colors and frequencies into the table
for color, frequency in color_counts.items():
    cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))

# Commit changes and close connection
conn.commit()
conn.close()

print("Colors and frequencies saved to

PostgreSQL
database.
") \ \


"""End of code"""
