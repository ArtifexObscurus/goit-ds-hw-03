import json

import requests
from bs4 import BeautifulSoup


quotes_data = []
authors_links = set()
authors_data = []

# Start scraping from the main page.
url = "https://quotes.toscrape.com/"

# The loop will continue while the "Next" page exists.
while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quote blocks on the current page.
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        # Extract the quote text, author name, and author page link.
        quote_text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        author_link = quote.find("a")["href"]

        # Store author links in a set to avoid duplicates.
        authors_links.add(author_link)

        # Create a dictionary with the required quote information.
        quote_data = {
            "tags": [
                tag.text for tag in quote.find_all("a", class_="tag")
            ],
            "author": author,
            "quote": quote_text,
        }

        quotes_data.append(quote_data)

    # Find the link to the next page.
    next_page = soup.find("li", class_="next")

    if next_page:
        next_link = next_page.find("a")["href"]
        url = f"https://quotes.toscrape.com{next_link}"
    else:
        # Stop scraping when there is no next page.
        url = None


# Visit each unique author page and collect the required information.
for author_link in authors_links:
    url = f"https://quotes.toscrape.com{author_link}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the author's name, birth date, birth location, and biography.
    fullname = soup.find(
        "h3",
        class_="author-title",
    ).text.strip()

    born_date = soup.find(
        "span",
        class_="author-born-date",
    ).text.strip()

    born_location = soup.find(
        "span",
        class_="author-born-location",
    ).text.strip()

    description = soup.find(
        "div",
        class_="author-description",
    ).text.strip()

    # Create a dictionary with the required author information.
    author_data = {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description,
    }

    authors_data.append(author_data)


# Save quotes and authors data to separate JSON files.
with open("part_2/qoutes.json", "w", encoding="utf-8") as file:
    json.dump(
        quotes_data,
        file,
        ensure_ascii=False,
        indent=4,
    )

with open("part_2/authors.json", "w", encoding="utf-8") as file:
    json.dump(
        authors_data,
        file,
        ensure_ascii=False,
        indent=4,
    )

print(f"Found {len(quotes_data)} quotes.")
print(f"Found {len(authors_data)} authors.")