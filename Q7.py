import pandas as pd

from sklearn.model_selection import train_test_split

def main():

    Data = pd.read_csv("Loan_Default.csv")

    Data["PreviousDefault"] = Data["PreviousDefault"].map({
        "No": 0,
        "Yes": 1
    })

    Data = pd.get_dummies(Data,columns=["HomeOwnership"],dtype=int)

    X = Data.drop("Default", axis=1)
    y = Data["Default"]

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,)

    print("Training Data:", X_train.shape)
    print("Testing Data:", X_test.shape)

if __name__ == "__main__":
    main()