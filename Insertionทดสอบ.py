import time
def insertion_sort_with_steps(arr):
    print(f"เริ่มต้น: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nรอบที่ {i}: พิจารณา key = {key}")
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            print(f"  ย้าย {arr[j+2]} ไปทางขวา: {arr}")
        
        arr[j+1] = key
        print(f"  แทรก {key} ลงในตำแหน่ง {j+1}: {arr}")
def insertion_sort_desc(arr):
    for i in range(1, len(arr)):  # เริ่มจาก index ที่ 1 เพราะ index 0 ถือว่าถูกจัดเรียงแล้ว
        key = arr[i]  # เก็บค่าของตัวที่กำลังจะจัดเรียง
        j = i - 1
        # เปลี่ยนเงื่อนไขเป็น j >= 0 และ arr[j] < key เพื่อให้เรียงจากมากไปน้อย
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]  # เลื่อนค่าที่น้อยกว่าขึ้นไป
            j -= 1
        arr[j + 1] = key  # วางค่าที่เหมาะสมลงตำแหน่งใหม่
    return arr

# ทดสอบฟังก์ชัน
arr = [5, 3, 8, 4, 2]
sorted_arr = insertion_sort_desc(arr)
print("ข้อมูลก่อนเรียง:", arr)

start_time = time.time()
sorted_data = insertion_sort_desc(arr.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
insertion_sort_with_steps(arr.copy())
print("เรียงลำดับจากมากไปน้อย:", sorted_arr)
