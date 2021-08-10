import pandas as pd
from typing import List




def openFile(filePath: str = None) -> pd.DataFrame:
    df = None
    if not filePath:
        filePath = input('Enter the file path of the csv file:\n')
    try:
        df = pd.read_csv(filePath)
    except Exception as ex:
        print(str(ex))
        print("Reenter file path before proceeding...\n")
    return df


def groupCols(df: pd.DataFrame, cols: List[str], axi: int = 0) -> pd.DataFrame:
        grouped = None
        try:
            if len(cols) == 1:
                df = df.groupby([cols[0]], axis=axi)
            elif len(cols) == 2:
                df = df.groupby([cols[0], cols[1]], axis=axi)
            elif len(cols) == 3:
                df = df.groupby([cols[0], cols[1], cols[2]], axis=axi)
            else:
                raise Exception("An error occurred, incorrect amount of columns.")
        except Exception as ex:
            print(str(ex))
            print("Check that the columns are correct. If unsure, call option 3.\n")
        return df


def showStats(dafr: pd.DataFrame) -> None:
    print('Mean: %r' % (dafr.mean()))
    print('Variance:%r' % (dafr.var()))
    print('Std Dev: %r' % (dafr.std()))
    return



def main():
    df = None
    
    while True:
        df = openFile()
        if df is None:
            continue
        else:
            break
    print(df.info())
    df.columns = df.columns.str.strip()
    while True:
        option = input("Choose an option:\n1 - Open New File\n2 - Get Head of file\n"+
                       "3 - Get Info on file\n4 - Group between 1 and 3 column\n"+
                       "5 - Get count of specified column\n6 - Exit\n")
        if option == "1":
            df = openFile()
            df.columns = df.columns.str.strip()

        elif option == "2":
            count = input('Specify the number of rows to retrieve or enter 0\n')
            if count != int(0):
                print(df.head(int(count)))
            print(df.head())

        elif option == "3":
            print(df.info())

        elif option == "4":
            cols = input('Enter between 1 and 3 columns separated by a comma\n')
            group = cols.split(',')
            df = groupCols(df, group)
            showStats(df)

        elif option == "5":
            col = input('Enter column name to get count of\n')
            print(df[col].value_counts())

        elif option == "6":
            exit()

        else:
            print("Could not understand option. Enter numeric value\n")





if __name__ == "__main__":
    main()
