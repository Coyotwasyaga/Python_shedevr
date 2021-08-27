from colorama import Fore, Back

print(Fore.GREEN)
print(Back.BLACK)


def presentation():
    print("This function extend functions object class Job,\nwhich have as several function... ")


if __name__ == "__main__":
    presentation()


class New_class:

    def __init__(self):
        self.value = None
        self.count = None
        self.data = None

    def add_value(self):
        self.value = str(input())
        print("Correct input?")
        self.count = len(self.value)
        print(self.count, self.value)

    def given(self):
        data = self.data
        self.data = input()
        print(data)

    def type_print(self):
        self.value = float(input())
        self.count = list(input())

        self.data = str(input())
        print(type(self.value), type(self.count), type(self.data))

    def matrix(self):
        self.value = ("\t'1,0,1,0,1'\n,"
                      "\t'0,1,0,1,0'\n,"
                      "\t'1,0,1,0,1'\n,"
                      "\t'0,1,0,1,0'\n")

        self.count = {'Was': '1987', 'Jozef Rose': '1959', 'John Brown': '1973'}
        self.data = '\n"This is the string type data special for this class!"'
        print(self.value, self.count, self.data)


class Job(New_class):
    from colorama import Fore, Back
    print(Fore.GREEN)
    print(Back.BLACK)

    def pyramid(self):
        I = []
        i = 0
        while i < 10:
            i += 1
            I.append(i)
            print(I)

    def show_pd(self):
        import pandas as pd
        df = pd.read_csv(
            r"c:\Users\Василий-Алибабаич!!!\AppData\Local\Programs\Python\Python37\Lib\site-packages\sklearn\datasets"
            r"\data\breast_cancer.csv")
        print(df)

    def PIL_object(self):
        from PIL import Image
        print("Please choose 1 or 2 for select option...\n",
              "Type input must be int\n")
        i = int(input())
        
        if i == 1:
            Image = Image.open("d:\MY_DOWNLOAD_FILES\guido-van-rossum.jpg")
            Image.paste(Image)
            Image.save('d:\MY_DOWNLOAD_FILES\guido-van-rossum.jpg', quality=85)
            Image.show()
        elif i == 2:
            Image = Image.open("d:\MY_DOWNLOAD_FILES\LOSTARK_210202_2325.jpg")
            Image.show()
        else:
            Image = Image.open("d:\MY_DOWNLOAD_FILES\BB1dDpJ9.jpg")
            Image.show()
