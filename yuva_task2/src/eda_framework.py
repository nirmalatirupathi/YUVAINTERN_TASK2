"""Reusable EDA framework for the hypothetical customer churn project.

This script is intentionally dataset-agnostic. It demonstrates the analysis structure
without fabricating results from a dataset that was not supplied for the internship task.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file supplied by the project owner."""
    return pd.read_csv(path)


def profile_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a compact structural profile."""
    return pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing_count": df.isna().sum(),
        "missing_percent": (df.isna().mean() * 100).round(2),
        "unique_count": df.nunique(dropna=True),
    })


def plot_numeric_distribution(df: pd.DataFrame, column: str, output: str) -> None:
    """Create a histogram for one numeric variable."""
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x=column, kde=True)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output, dpi=150)
    plt.close()


def plot_churn_by_category(df: pd.DataFrame, category: str, target: str, output: str) -> None:
    """Plot mean binary churn by category."""
    rates = df.groupby(category, dropna=False)[target].mean().sort_values(ascending=False)
    plt.figure(figsize=(9, 5))
    rates.plot(kind="bar")
    plt.title(f"Churn Rate by {category}")
    plt.xlabel(category)
    plt.ylabel("Churn rate")
    plt.tight_layout()
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output, dpi=150)
    plt.close()


def correlation_matrix(df: pd.DataFrame, output: str) -> None:
    """Create a correlation heatmap for numeric columns."""
    numeric = df.select_dtypes(include="number")
    plt.figure(figsize=(10, 7))
    sns.heatmap(numeric.corr(), annot=True, fmt=".2f", cmap="coolwarm", center=0)
    plt.title("Numeric Feature Correlation Matrix")
    plt.tight_layout()
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output, dpi=150)
    plt.close()


if __name__ == "__main__":
    print("EDA framework ready. Supply an approved dataset path before execution.")
