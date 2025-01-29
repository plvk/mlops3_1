import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(file_path: str = "Credit_Default.csv") -> pd.DataFrame:
    """
    Load the credit default dataset and perform initial preprocessing.

    Args:
        file_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded and preprocessed dataset
    """

    df = pd.read_csv(file_path)
    return df


def missing_values_analysis(df: pd.DataFrame):
    """
    Missing Values Analysis in the dataset.

    Args:
        df (pd.DataFrame): Input dataset

    """

    # Calculating missing values
    missing_values = df.isnull().sum()

    # Check for missing values
    if missing_values[missing_values > 0].empty:
        print("Нет пропущенных значений в датафрейме.")
    else:
        # Building a bar chart to visualize missing values
        plt.figure(figsize=(10, 6))
        missing_values[missing_values > 0].plot(kind="bar")
        plt.title("Missing values ​​by columns")
        plt.xlabel("Columns")
        plt.ylabel("Number of missing values")
        plt.show()


def plotting_pairwise_diagrams(df: pd.DataFrame):
    """
    Plotting pairwise distribution diagrams for numerical features.

    Args:
        df (pd.DataFrame): Input dataset
    """

    # Plotting pairwise distribution diagrams
    sns.pairplot(df, vars=["Income", "Age", "Loan", "Default"], hue="Default")
    plt.show()


def сorrelation_analysis(df: pd.DataFrame):
    """
    Correlation analysis between numerical features.

    Args:
        df (pd.DataFrame): Input dataset
    """

    # Calculation of the correlation matrix
    correlation_matrix = df.corr()

    # Visualizing the correlation matrix using heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation matrix")
    plt.show()


def class_balance_analysis(df: pd.DataFrame):
    """
    Class balance analysis of default/non-default.

    Args:
        df (pd.DataFrame): Input dataset
    """

    # Class balance analysis
    class_distribution = df["Default"].value_counts()

    # Visualization of class distribution
    plt.figure(figsize=(8, 5))
    class_distribution.plot(kind="bar")
    plt.title("Class Distribution (Default/Not Default)")
    plt.xlabel("Class")
    plt.ylabel("Quantity")
    plt.xticks(ticks=[0, 1], labels=["Not Default", "Default"], rotation=0)
    plt.show()


def perform_eda():

    # Load data
    df = load_data()

    # Data set
    print("\nData:")
    print(df.head())

    # Missing values analysis
    print("\nMissing Values Analysis:")
    missing_values_analysis(df)

    # Plotting pairwise distribution diagrams
    print("\nPlotting pairwise distribution diagrams:")
    plotting_pairwise_diagrams(df)

    # Correlation analysis
    print("\nCorrelation analysis:")
    сorrelation_analysis(df)

    # Class balance analysis
    print("\nClass balance analysis:")
    class_balance_analysis(df)
