import pandas as pd
#Check whether the target classes are balanced.
def main():

    Data = pd.read_csv("Loan_Default.csv")

    print("Class Count:")
    print(Data["Default"].value_counts())

    print("Class Percentage:")
    print(Data["Default"].value_counts(normalize=True) * 100)

if __name__ == "__main__":
    main()