import pandas as pd
#EDA
def main():

    Data = pd.read_csv("Loan_Default.csv")

    print("Statistical Information:")
    print(Data.describe())

    print("\nDefault Distribution:")
    print(Data["Default"].value_counts())

    print("\nCategorical Values:")
    print("PreviousDefault:", Data["PreviousDefault"].unique())
    print("HomeOwnership:", Data["HomeOwnership"].unique())

if __name__ == "__main__":
    main()