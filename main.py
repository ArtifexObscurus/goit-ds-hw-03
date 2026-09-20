from os import getenv

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError


load_dotenv()

mongo_uri = getenv("MONGO_URI")

client = MongoClient(mongo_uri)

db = client["cats"]
collection = db["cats"]


def create_cat(name: str, age: int, features: list[str]) -> None:
    """Add a new cat to the collection."""
    cat = {
        "name": name,
        "age": age,
        "features": features,
    }

    collection.insert_one(cat)


def get_all_cats() -> None:
    """Display all cats from the collection."""
    cats = collection.find()

    for cat in cats:
        print(cat)


def find_cat(name: str) -> None:
    """Find and display a cat by name."""
    cat = collection.find_one({"name": name})

    if cat:
        print(cat)
    else:
        print(f"Cat '{name}' not found.")


def update_cat_age(name: str, age: int) -> None:
    """Update a cat's age by name."""
    result = collection.update_one(
        {"name": name},
        {"$set": {"age": age}},
    )

    if result.matched_count:
        print(f"Age of '{name}' updated.")
    else:
        print(f"Cat '{name}' not found.")


def add_cat_feature(name: str, feature: str) -> None:
    """Add a new feature to a cat by name."""
    result = collection.update_one(
        {"name": name},
        {"$push": {"features": feature}},
    )

    if result.matched_count:
        print(f"Feature added to '{name}'.")
    else:
        print(f"Cat '{name}' not found.")


def delete_cat(name: str) -> None:
    """Delete one cat by name."""
    result = collection.delete_one({"name": name})

    if result.deleted_count:
        print(f"Cat '{name}' deleted.")
    else:
        print(f"Cat '{name}' not found.")


def delete_all_cats() -> None:
    """Delete all cats from the collection."""
    result = collection.delete_many({})

    print(f"Deleted {result.deleted_count} cats.")


def show_menu() -> None:
    """Display available commands."""
    menu = {
        "1": ("add", "Add cat"),
        "2": ("all", "Show all cats"),
        "3": ("find", "Find cat"),
        "4": ("age", "Update age"),
        "5": ("feature", "Add feature"),
        "6": ("delete", "Delete cat"),
        "7": ("delete-all", "Delete all cats"),
        "0": ("exit", "Exit"),
    }

    print("\n".join(
        f"{number}: {command:<10} - {description}"
        for number, (command, description) in menu.items()
    ))


def main() -> None:
    """Run the MongoDB CRUD application."""
    try:
        client.admin.command("ping")
    except PyMongoError as error:
        print(f"MongoDB connection error: {error}")
        return

    print("MongoDB connection successful!")
    print("Welcome to the Cat Management System!")
    show_menu()

    try:
        while True:
            choice = input(
                "\nChoose an operation or enter '?' for help: "
            )

            try:
                match choice:
                    case "?":
                        show_menu()

                    case "0":
                        print("Goodbye!")
                        break

                    case "1":
                        name = input("Enter cat name: ")
                        age = int(input("Enter cat age: "))
                        features = input(
                            "Enter cat features: "
                        ).split(", ")
                        create_cat(name, age, features)

                    case "2":
                        get_all_cats()

                    case "3":
                        name = input("Enter cat name: ")
                        find_cat(name)

                    case "4":
                        name = input("Enter cat name: ")
                        age = int(input("Enter new age: "))
                        update_cat_age(name, age)

                    case "5":
                        name = input("Enter cat name: ")
                        feature = input("Enter new feature: ")
                        add_cat_feature(name, feature)

                    case "6":
                        name = input("Enter cat name: ")
                        delete_cat(name)

                    case "7":
                        confirmation = input(
                            "Delete all cats? Enter 'yes' to confirm: "
                        )

                        if confirmation.lower() == "yes":
                            delete_all_cats()
                        else:
                            print("Operation cancelled.")

                    case _:
                        print("Unknown operation. Enter '?' for help.")

            except ValueError:
                print("Age must be a number.")

            except PyMongoError as error:
                print(f"MongoDB error: {error}")

    finally:
        client.close()


if __name__ == "__main__":
    main()