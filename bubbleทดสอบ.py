def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # เพิ่มตัวแปรเพื่อตรวจสอบการสลับ
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # มีการสลับเกิดขึ้น
        
        # ถ้าไม่มีการสลับเลย ให้หยุดการทำงาน
        if not swapped:
            break

# ทดสอบการทำงาน
arr_test = [1, 2, 3, 4, 5,6,7,8,9,10]
bubble_sort(arr_test)
print("Sorted array:", arr_test)
