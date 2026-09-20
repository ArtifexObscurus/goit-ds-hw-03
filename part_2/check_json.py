import json


with open("part_2/qoutes.json", "r", encoding="utf-8") as file:
    quotes = json.load(file)

with open("part_2/authors.json", "r", encoding="utf-8") as file:
    authors = json.load(file)

print(f"Quotes: {len(quotes)}")
print(f"Authors: {len(authors)}")

print("\nFirst quote:")
print(quotes[0])

print("\nFirst author:")
print(authors[0])