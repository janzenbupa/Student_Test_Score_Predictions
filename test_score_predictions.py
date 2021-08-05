import pandas as pd

class Data(object):
    def viewData(self, filePath: str):
        try:
            df = pd.read_csv(filePath)
        except Exception as ex:
            print(str(ex))
            return

        print(df.info())
        print(df.describe())
        print(df.head())
        print(df.shape[0])
        print("Number of schools per setting:\n%r" % (
            df['school_setting'].value_counts()))
        print("Number of schools per type:\n%r" %(
            df['school_type'].value_counts()))

        print(df.groupby(['school_type','school_setting','gender']).mean())



def main():
    file = input('Enter the file path of the csv file:\n')
    data = Data()
    data.viewData(file)



if __name__ == "__main__":
    main()
