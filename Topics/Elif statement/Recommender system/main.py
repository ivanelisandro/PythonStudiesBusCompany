age = int(input())
movie = ""

if age <= 16:
    movie = "Lion King"
elif 17 <= age <= 25:
    movie = "Trainspotting"
elif 26 <= age <= 40:
    movie = "Matrix"
elif 41 <= age <= 60:
    movie = "Pulp Fiction"
elif age > 60:
    movie = "Breakfast at Tiffany's"

print(movie)
