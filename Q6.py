import pandas as pd
#Separate X and y.
def main():

    Data = pd.read_csv("Loan_Default.csv")

    Data["PreviousDefault"] = Data["PreviousDefault"].map({"No": 0,"Yes": 1})

    Data = pd.get_dummies(Data,columns=["HomeOwnership"],dtype=int)

    X = Data.drop("Default", axis=1)

    y = Data["Default"]

    print("X:")
    print(X.head())

    print("\ny:")
    print(y.head())

if __name__ == "__main__":
    main()