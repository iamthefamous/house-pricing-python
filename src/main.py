from src.core.house_analyzer import HouseAnalyzer


def main():
    while True:
        print("Options: ")
        print("1. Evaluvate the house")
        print("0. Exit")
        
        a = input("Choose your option: ")
        
        if a == 1:
            analyzer = HouseAnalyzer()
            analyzer.run()