import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # กำหนดค่าเริ่มต้นว่ายังไม่มีการสลับ
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # สลับค่าถ้าลำดับผิด
                swapped = True  # มีการสลับเกิดขึ้น
        
        if not swapped:
            break  # ถ้าไม่มีการสลับในรอบนี้ ให้หยุดการทำงานทันที

# ตัวอย่างการใช้งาน
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)