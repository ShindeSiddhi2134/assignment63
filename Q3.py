import pandas as pd

#find missing values
def main():

    Data = pd.read_csv("Loan_Default.csv")

    print("Missing Values:")
    print(Data.isnull().sum())

if __name__ == "__main__":
    main()