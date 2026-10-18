
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None

    
    def load_data(self):
        file_name = input("Enter CSV file name (or press Enter for sample data): ")

        if file_name == "":
            self.data = pd.DataFrame({
                "SalesID": range(101, 121),
                "Product": [
                    "Laptop", "Mobile", "Tablet", "Mouse", "Keyboard",
                    "Monitor", "Laptop", "Mobile", "Tablet", "Mouse",
                    "Keyboard", "Monitor", "Laptop", "Mobile", "Tablet",
                    "Mouse", "Keyboard", "Monitor", "Laptop", "Mobile"
                ],
                "Region": [
                    "North", "South", "East", "West", "Central",
                    "North", "South", "East", "West", "Central",
                    "North", "South", "East", "West", "Central",
                    "North", "South", "East", "West", "Central"
                ],
                "Sales": [
                    45000, 18000, 12000, 2500, 1200,
                    15000, 52000, 22000, 14000, 1500,
                    2800, 17000, 48000, 20000, 11000,
                    1800, 3200, 16000, 55000, 24000
                ],
                "Year": [
                    2022, 2022, 2022, 2022, 2022,
                    2022, 2023, 2023, 2023, 2023,
                    2023, 2023, 2024, 2024, 2024,
                    2024, 2024, 2024, 2022, 2022
                ]
            })

            print("Sample data loaded successfully!")

        else:
            try:
                self.data = pd.read_csv(file_name)
                print("CSV file loaded successfully!")

            except FileNotFoundError:
                print("File not found. Please check the file name.")
                return

            except Exception as e:
                print("Error loading file:", e)
                return

        print(self.data.head())

    
    def check_data(self):
        if self.data is None:
            print("Please load the data first.")
            return False
        return True

    
    def explore_data(self):
        if not self.check_data():
            return

        print("\n1. First 5 rows")
        print("2. Last 5 rows")
        print("3. Column names")
        print("4. Data types")
        print("5. Dataset information")
        print("6. Full statistics")

        choice = input("Enter choice: ")

        if choice == "1":
            print(self.data.head())

        elif choice == "2":
            print(self.data.tail())

        elif choice == "3":
            print(self.data.columns)

        elif choice == "4":
            print(self.data.dtypes)

        elif choice == "5":
            self.data.info()

        elif choice == "6":
            print(self.data.describe())

        else:
            print("Invalid choice.")

    
    def array_operations(self):
        if not self.check_data():
            return

        if "Sales" not in self.data.columns:
            print("Sales column not found.")
            return

        sales_array = self.data["Sales"].dropna().to_numpy()

        if len(sales_array) == 0:
            print("No sales values available.")
            return

        print("\nSales Array:")
        print(sales_array)

        print("\nFirst 5 sales:")
        print(sales_array[:5])

        print("\nFirst sale:", sales_array[0])

        print("\nSales increased by 10%:")
        print(sales_array * 1.10)

        print("\nTotal sales:", np.sum(sales_array))
        print("Average sales:", np.mean(sales_array))

    
    def data_operations(self):
        if not self.check_data():
            return

        if "Product" not in self.data.columns or "Sales" not in self.data.columns:
            print("Product or Sales column is missing.")
            return

        print("\n1. Search product")
        print("2. Sort sales")
        print("3. Filter sales")
        print("4. Total and average sales")
        print("5. Sales by region")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            result = self.data[
                self.data["Product"].astype(str).str.contains(
                    name, case=False, na=False
                )
            ]
            print(result)

        elif choice == "2":
            result = self.data.sort_values("Sales", ascending=False)
            print(result)

        elif choice == "3":
            try:
                amount = float(input("Enter minimum sales amount: "))
                print(self.data[self.data["Sales"] >= amount])
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Total sales:", self.data["Sales"].sum())
            print("Average sales:", self.data["Sales"].mean())
            print("Number of sales:", self.data["Sales"].count())

        elif choice == "5":
            if "Region" in self.data.columns:
                print(self.data.groupby("Region")["Sales"].sum())
            else:
                print("Region column not found.")

        else:
            print("Invalid choice.")

   
    def missing_data(self):
        if not self.check_data():
            return

        print("\nMissing values:")
        print(self.data.isnull().sum())

        print("\n1. Fill missing values")
        print("2. Remove rows with missing values")

        choice = input("Enter choice: ")

        if choice == "1":
            for column in self.data.columns:
                if self.data[column].isnull().any():
                    if pd.api.types.is_numeric_dtype(self.data[column]):
                        self.data[column] = self.data[column].fillna(
                            self.data[column].mean()
                        )
                    else:
                        self.data[column] = self.data[column].fillna("Unknown")

            print("Missing values filled.")

        elif choice == "2":
            self.data = self.data.dropna()
            print("Rows with missing values removed.")

        else:
            print("Invalid choice.")

    
    def statistics(self):
        if not self.check_data():
            return

        if "Sales" not in self.data.columns:
            print("Sales column not found.")
            return

        sales = self.data["Sales"].dropna()

        if sales.empty:
            print("No sales values available.")
            return

        print("\n1. Mean")
        print("2. Median")
        print("3. Standard deviation")
        print("4. Variance")
        print("5. Percentiles")
        print("6. Full statistics")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Mean:", sales.mean())

        elif choice == "2":
            print("Median:", sales.median())

        elif choice == "3":
            print("Standard deviation:", sales.std())

        elif choice == "4":
            print("Variance:", sales.var())

        elif choice == "5":
            print("25th percentile:", sales.quantile(0.25))
            print("50th percentile:", sales.quantile(0.50))
            print("75th percentile:", sales.quantile(0.75))

        elif choice == "6":
            print(sales.describe())

        else:
            print("Invalid choice.")

   
    def combine_split_data(self):
        if not self.check_data():
            return

        print("\n1. Combine two DataFrames")
        print("2. Merge product details")
        print("3. Split data by region")
        print("4. Create pivot table")

        choice = input("Enter choice: ")

        if choice == "1":
            first_part = self.data.head(5)
            second_part = self.data.tail(5)

            combined = pd.concat(
                [first_part, second_part], ignore_index=True
            )

            print("Combined DataFrame:")
            print(combined)

        elif choice == "2":
            if "Product" not in self.data.columns:
                print("Product column not found.")
                return

            products = self.data["Product"].dropna().unique()

            details = pd.DataFrame({
                "Product": products,
                "Category": ["Electronic"] * len(products)
            })

            result = pd.merge(self.data, details, on="Product", how="left")
            print(result)

        elif choice == "3":
            if "Region" not in self.data.columns:
                print("Region column not found.")
                return

            for region, group in self.data.groupby("Region"):
                print("\nRegion:", region)
                print(group)

        elif choice == "4":
            if "Region" not in self.data.columns or "Year" not in self.data.columns:
                print("Region or Year column not found.")
                return

            table = pd.pivot_table(
                self.data,
                values="Sales",
                index="Region",
                columns="Year",
                aggfunc="sum",
                fill_value=0
            )

            print(table)

        else:
            print("Invalid choice.")

  
    def make_chart(self):
        if not self.check_data():
            return

        if "Sales" not in self.data.columns:
            print("Sales column not found.")
            return

        print("\n1. Bar chart")
        print("2. Line chart")
        print("3. Scatter plot")
        print("4. Histogram")
        print("5. Pie chart")
        print("6. Box plot")
        print("7. Heatmap")
        print("8. Subplots")

        choice = input("Choose chart: ")

        plt.figure(figsize=(9, 5))

        if choice == "1":
            if "Product" not in self.data.columns:
                print("Product column not found.")
                return

            self.data.groupby("Product")["Sales"].sum().plot(kind="bar")
            plt.title("Sales by Product")
            plt.xlabel("Product")
            plt.ylabel("Sales")

        elif choice == "2":
            if "Year" not in self.data.columns:
                print("Year column not found.")
                return

            self.data.groupby("Year")["Sales"].sum().plot(
                kind="line", marker="o", label="Sales"
            )
            plt.title("Sales by Year")
            plt.xlabel("Year")
            plt.ylabel("Sales")
            plt.legend()

        elif choice == "3":
            if "Year" not in self.data.columns:
                print("Year column not found.")
                return

            plt.scatter(self.data["Year"], self.data["Sales"])
            plt.title("Year and Sales")
            plt.xlabel("Year")
            plt.ylabel("Sales")

        elif choice == "4":
            self.data["Sales"].dropna().plot(kind="hist", bins=8)
            plt.title("Sales Histogram")
            plt.xlabel("Sales")
            plt.ylabel("Frequency")

        elif choice == "5":
            if "Region" not in self.data.columns:
                print("Region column not found.")
                return

            self.data.groupby("Region")["Sales"].sum().plot(
                kind="pie", autopct="%1.1f%%"
            )
            plt.title("Sales by Region")
            plt.ylabel("")

        elif choice == "6":
            sns.boxplot(x=self.data["Sales"])
            plt.title("Sales Box Plot")
            plt.xlabel("Sales")

        elif choice == "7":
            numbers = self.data.select_dtypes(include=np.number)

            if numbers.shape[1] < 2:
                print("At least two numeric columns are needed.")
                plt.close()
                return

            sns.heatmap(numbers.corr(), annot=True, cmap="coolwarm")
            plt.title("Sales Data Heatmap")

        elif choice == "8":
            if "Product" not in self.data.columns or "Year" not in self.data.columns:
                print("Product or Year column not found.")
                plt.close()
                return

            fig, axes = plt.subplots(1, 2, figsize=(12, 5))

            self.data.groupby("Product")["Sales"].sum().plot(
                kind="bar", ax=axes[0]
            )
            axes[0].set_title("Sales by Product")
            axes[0].set_xlabel("Product")
            axes[0].set_ylabel("Sales")

            self.data.groupby("Year")["Sales"].sum().plot(
                kind="line", marker="o", ax=axes[1]
            )
            axes[1].set_title("Sales by Year")
            axes[1].set_xlabel("Year")
            axes[1].set_ylabel("Sales")

            plt.tight_layout()

            file_name = input("Save subplot image? (y/n): ")
            if file_name.lower() == "y":
                plt.savefig("sales_subplots.png")
                print("Saved as sales_subplots.png")

            plt.show()
            return

        else:
            print("Invalid choice.")
            plt.close()
            return

        plt.tight_layout()

        save = input("Save this chart? (y/n): ")
        if save.lower() == "y":
            file_name = input("Enter file name (e.g. chart.png): ")

            if file_name.strip() != "":
                if not file_name.lower().endswith(
                    (".png", ".jpg", ".jpeg")
                ):
                    file_name += ".png"

                try:
                    plt.savefig(file_name)
                    print("Chart saved as", file_name)
                except Exception as e:
                    print("Error saving chart:", e)

        plt.show()
        plt.close()

   
    def export_data(self):
        if not self.check_data():
            return

        file_name = input("Enter output file name (e.g. result.csv): ")

        if file_name.strip() == "":
            print("File name cannot be empty.")
            return

        if not file_name.lower().endswith(".csv"):
            file_name += ".csv"

        try:
            self.data.to_csv(file_name, index=False)
            print("Data exported successfully:", file_name)

        except Exception as e:
            print("Error exporting data:", e)


    def menu(self):
        while True:
            print("\n===== PANDAS SALES ANALYZER =====")
            print("1. Load data")
            print("2. Explore data")
            print("3. NumPy array operations")
            print("4. Data operations")
            print("5. Handle missing data")
            print("6. Statistics")
            print("7. Combine and split data")
            print("8. Create chart")
            print("9. Export data")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.load_data()

            elif choice == "2":
                self.explore_data()

            elif choice == "3":
                self.array_operations()

            elif choice == "4":
                self.data_operations()

            elif choice == "5":
                self.missing_data()

            elif choice == "6":
                self.statistics()

            elif choice == "7":
                self.combine_split_data()

            elif choice == "8":
                self.make_chart()

            elif choice == "9":
                self.export_data()

            elif choice == "10":
                print("Thank you for using Pandas Sales Analyzer!")
                break

            else:
                print("Please choose a number from 1 to 10.")


app = SalesDataAnalyzer()
app.menu()
