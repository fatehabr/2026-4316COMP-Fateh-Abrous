import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("dataset/vgsales.csv")


def show_first_games():
   
    print("\n=== First 5 Games ===")

    # Display first five records
    print(df.head())


def show_top_10_games():
    print("\n=== Top 10 Best Selling Games ===")
    top10 = df.sort_values(by="Global_Sales", ascending=False)
    print(top10[["Name", "Platform", "Genre", "Publisher", "Global_Sales"]].head(10))


def search_game():
    keyword = input("\nEnter game name: ")
    results = df[df["Name"].str.contains(keyword, case=False, na=False)]

    if results.empty:
        print("No game found.")
    else:
        print("\n=== Search Results ===")
        print(results[["Name", "Platform", "Year", "Genre", "Publisher", "Global_Sales"]].head(20))


def filter_by_genre():
    genre = input("\nEnter genre: ")
    results = df[df["Genre"].str.contains(genre, case=False, na=False)]

    if results.empty:
        print("No games found for this genre.")
    else:
        print("\n=== Games by Genre ===")
        print(results[["Name", "Platform", "Genre", "Global_Sales"]].head(20))


def show_statistics():
    print("\n=== Dataset Statistics ===")
    print("Total games:", len(df))
    print("Number of platforms:", df["Platform"].nunique())
    print("Number of genres:", df["Genre"].nunique())
    print("Number of publishers:", df["Publisher"].nunique())
    print("Average global sales:", round(df["Global_Sales"].mean(), 2))
    print("Highest global sales:", df["Global_Sales"].max())
    print("Lowest global sales:", df["Global_Sales"].min())

# Create publisher sales graph
def publisher_graph():
    publisher_sales = (
        df.groupby("Publisher")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    publisher_sales.plot(kind="bar")
    plt.title("Top 10 Publishers by Global Sales")
    plt.xlabel("Publisher")
    plt.ylabel("Global Sales (Millions)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("screenshots/publisher_sales.png")
    print("\nGraph saved in screenshots/publisher_sales.png")
    plt.show()


def genre_graph():
    genre_sales = (
        df.groupby("Genre")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))
    genre_sales.plot(kind="bar")
    plt.title("Global Sales by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Global Sales (Millions)")
    plt.tight_layout()
    plt.savefig("screenshots/genre_sales.png")
    print("\nGraph saved in screenshots/genre_sales.png")
    plt.show()


def main_menu():
    while True:
        print("\n========== Video Game Sales Analysis ==========")
        print("1. Show first 5 games")
        print("2. Show top 10 best-selling games")
        print("3. Search game by name")
        print("4. Filter games by genre")
        print("5. Show statistics")
        print("6. Create publisher graph")
        print("7. Create genre graph")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_first_games()
        elif choice == "2":
            show_top_10_games()
        elif choice == "3":
            search_game()
        elif choice == "4":
            filter_by_genre()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            publisher_graph()
        elif choice == "7":
            genre_graph()
        elif choice == "0":
            print("Program closed.")
            break
        else:
            print("Invalid option. Please try again.")


main_menu()