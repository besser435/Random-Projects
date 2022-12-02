

import main_classes


def main():
    print("main file")


    option = main_classes.options()
    print(option.countdown)
    option.countdown = 5
    print(option.countdown)
    



if __name__ == "__main__":
    main()


