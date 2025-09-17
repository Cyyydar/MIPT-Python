

l = int(input())
r = int(input())

while l <= r:
    mid = (l + r) // 2
    answer = input(f"Число равно {mid}?")
    
    if answer == 'да':
        print('Ваше число -', mid )
        break
    else:
        answer = input(f"Число меньше {mid}?")
        if answer == 'да':
            r = mid - 1
        else:
            l = mid + 1
else:
    print("Число не входит в диапазон")

