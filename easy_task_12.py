import os

print(os.listdir())
for i in range(1, 10):
    if os.path.exists(f'dir_{i}'):
        os.rmdir(f'dir_{i}')
