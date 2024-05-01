def hanoi_tower(n, source, target, auxiliary):
    if n == 1:
        print(f"Переміщення диска {n} з {source} на {target}")
        return
    hanoi_tower(n-1, source, auxiliary, target)
    print(f"Переміщення диска {n} з {source} на {target}")
    hanoi_tower(n-1, auxiliary, target, source)

def main():
    n = int(input("Введіть кількість дисків: "))
    hanoi_tower(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()
