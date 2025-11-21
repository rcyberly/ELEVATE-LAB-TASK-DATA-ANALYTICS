import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data, plot_sales_by_product, plot_sales_by_region, plot_monthly_trend
import os

# Create plots directory if it doesn't exist
os.makedirs("../plots", exist_ok=True)

def main():
    # Load dataset
    df = load_data("../data/sales_data.csv")

    # Group by Product
    sales_by_product = df.groupby("Product")["Sales"].sum()
    print("Sales by Product:\n", sales_by_product)

    # Plot Product Sales
    plot_sales_by_product(sales_by_product)

    # Group by Region
    sales_by_region = df.groupby("Region")["Sales"].sum()
    print("Sales by Region:\n", sales_by_region)

    # Plot Region Sales
    plot_sales_by_region(sales_by_region)

    # Monthly Trend
    df["Date"] = pd.to_datetime(df["Date"])
    monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()
    print("Monthly Sales Trend:\n", monthly_sales)

    # Plot Monthly Trend
    plot_monthly_trend(monthly_sales)

if __name__ == "__main__":
    main()
