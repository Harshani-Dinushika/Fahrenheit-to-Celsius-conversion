while True:
    def genFibo(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return genFibo(x - 1) + genFibo(x - 2)


    def showFibo(listfibo):
        print(f"The Fibonacci sequence is {' , '.join(str(k) for k in listfibo)}")


    def main():
        listfibo = []
        for x in range(0, 10):
            listfibo.append(genFibo(x))
        showFibo(listfibo)


    if __name__ == "__main__":
        main()
        break
