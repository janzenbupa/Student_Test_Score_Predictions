import pandas as pd

class Data:
    def __init__(self):
        self.df = None

    def OpenFile(self, filePath: str):
        try:
            self.df = pd.read_csv(filePath)
        except Exception as ex:
            print(str(ex))
            print("Reenter file path before proceeding...\n")
            return

    def Head(self, coun: int = 0):
        if coun == 0:
            print(self.df.head())
            return
        print(self.df.head(coun))

    def Info(self):
        print(self.df.info())

    def GroupCols(self, col1: str, col2: str = "", col3: str = ""):
        try:
            if not col2 and not col3:
                grouped = self.df.groupby([col1])
                self.GetStats(grouped)
            elif col2 and not col3:
                grouped = self.df.groupby([col1, col2])
                self.GetStats(grouped)
            elif col2 and col3:
                grouped = self.df.groupby([col1, col2, col3])
                self.GetStats(grouped)
            elif not col2 and col3:
                grouped = self.df.groupby([col1, col3])
                self.GetStats(grouped)
        except Exception as ex:
            print(str(ex))
        return

    def GetCount(self, col: str) -> int:
        if col:
            return self.df[col].value_counts()
        return 0

    def GetStats(self, dfStats):
        print("Mean : %r" %(dfStats.mean()))
        print("Variance: %r" % (dfStats.var()))
        print("Std Dev: %r" % (dfStats.std()))



def main():
    d = Data()
    while True:
        option = input("Choose an option:\n1 - Open New File\n2 - Get Head of file\n"+
                       "3 - Get Info on file\n4 - Group between 1 and 3 column\n"+
                       "5 - Get count of specified column\n6 - Exit\n")
        if option == "1":
            file = input('Enter the file path of the csv file:\n')
            d.OpenFile(file)
            continue

        elif option == "2":
            count = input("Enter number of rows to retrieve or enter 0\n")
            d.Head(int(count))
            continue

        elif option == "3":
            d.Info()

        elif option == "4":
            cols = input("Enter between 1 and 3 columns separated by a comma\n")
            group = cols.split(',')
            if len(group) == 1:
                d.GroupCols(group[0])
            elif len(group) < 3:
                d.GroupCols(group[0], group[1])
            else:
                d.GroupCols(group[0], group[1], group[2])

        elif option == "5":
                col = input("Enter column name to get count of\n")
                print(d.GetCount(col))

        elif option == "6":
            exit()

        else:
            print("Could not understand option. Enter numeric value\n")
            



if __name__ == "__main__":
    main()
