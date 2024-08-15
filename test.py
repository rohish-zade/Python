import os

# os.makedirs(f'{success_files_path}', exist_ok=True)
a = True
b = False

for num in range(1, 11):
    if b:
       continue
    print(num)
else:
    print("No numbers after 4")

