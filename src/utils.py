import pandas as pd
import matplotlib.pyplot as plt
import os

# Create plots directory if it doesn't exist
os.makedirs("../plots", exist_ok=True)


def load_data(filepath: str) -> pd.DataFrame:
    """Load CSV data into a Pandas DataFrame."""
    return pd.read_csv(filepath)

def plot_sales_by_product(sales_by_product: pd.Series):
    """Plot total sales by product as a bar chart."""
    sales_by_product.plot(kind="bar", title="Total Sales by Product")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("../plots/sales_by_product.png")
    plt.show()

def plot_sales_by_region(sales_by_region: pd.Series):
    """Plot total sales by region as a pie chart."""
    sales_by_region.plot(kind="pie", autopct="%1.1f%%", title="Sales by Region")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("../plots/sales_by_region.png")
    plt.show()

def plot_monthly_trend(monthly_sales: pd.Series):
    """Plot monthly sales trend as a line chart."""
    monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("../plots/monthly_sales_trend.png")
    plt.show()
