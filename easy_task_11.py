import os

for i in range(1, 10):
    if not os.path.exists(f'dir_{i}'):
        os.mkdir(f'dir_{i}')
