import pandas as pd

def main():
#load the dataset
    Data = pd.read_csv("Loan_Default.csv")

    print("First 5 Records:")
    print(Data.head())

    print("Last 5 Records:")
    print(Data.tail())

    print("Shape:")
    print(Data.shape)

    print("Columns:")
    print(Data.columns)

    print("Data Types:")
    print(Data.dtypes)

    print("Dataset Information:")
    Data.info()

if __name__ == "__main__":
    main()