import pandas as pd
#Encode categorical variables.
def main():

    Data = pd.read_csv("Loan_Default.csv")

    Data["PreviousDefault"] = Data["PreviousDefault"].map({"No": 0,"Yes": 1})

    Data = pd.get_dummies(Data,columns=["HomeOwnership"],dtype=int)

    print(Data.head())

if __name__ == "__main__":
    main()