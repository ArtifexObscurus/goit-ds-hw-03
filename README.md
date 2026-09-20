## Task 1 — MongoDB CRUD

A Python script was developed to work with MongoDB using the **PyMongo** library.

The following CRUD operations are implemented for animal records:

- add a new record;
- display all records;
- find a record by name;
- update the animal's age;
- add a new feature;
- delete a record by name;
- delete all records;
- handle MongoDB errors.

The MongoDB connection string is stored in the `MONGO_URI` environment variable.

Main file:

```text
main.py
```

## Task 2 — Web Scraping

The project includes web scraping of [quotes.toscrape.com](https://quotes.toscrape.com/).

The scraper collects data from all available pages:

- **100 quotes**
- **50 authors**

Two JSON files are generated:

```text
part_2/
├── authors.json
└── qoutes.json
```

### `authors.json`

Contains the following information about authors:

- `fullname`
- `born_date`
- `born_location`
- `description`

### `qoutes.json`

Contains the following information about quotes:

- `tags`
- `author`
- `quote`

The collected data was also uploaded to **MongoDB Atlas** into a separate `quotes` database:

```text
quotes
├── authors
└── qoutes
```

## Project Structure

```text
goit-ds-hw-03/
│
├── main.py
├── pyproject.toml
├── poetry.lock
├── poetry.toml
├── .gitignore
│
└── part_2/
    ├── quotes_scraper.py
    ├── check_json.py
    ├── upload_to_mongodb.py
    ├── authors.json
    └── qoutes.json
```

## Technologies

- Python 3.14
- Poetry
- MongoDB Atlas
- PyMongo
- Requests
- BeautifulSoup4
- python-dotenv
- JSON

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd goit-ds-hw-03
```

Install the project dependencies using Poetry:

```bash
poetry install
```

Create a `.env` file in the project root:

```env
MONGO_URI=your_mongodb_connection_string
```

## Running the Project

### Task 1

Run:

```bash
python main.py
```

The program provides a console menu for working with the MongoDB database.

### Task 2

Run the scraper:

```bash
python part_2/quotes_scraper.py
```

The script collects quotes and authors and saves them to JSON files.

To verify the generated JSON files:

```bash
python part_2/check_json.py
```

To upload the collected data to MongoDB Atlas:

```bash
python part_2/upload_to_mongodb.py
```

## Notes

The `.env` file containing the MongoDB connection string is excluded from the repository using `.gitignore`.

The collection name `qoutes` intentionally follows the spelling specified in the assignment.
