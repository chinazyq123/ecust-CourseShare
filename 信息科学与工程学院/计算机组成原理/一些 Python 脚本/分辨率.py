分辨率横 = 1280
分辨率竖 = 1024
基色x位 = 8
print(f'为了保存一帧图像最少需要{基色x位}*3*{分辨率横}*{分辨率竖}*1024b ={基色x位*3*分辨率横*分辨率竖}bit/帧的缓存')
print(f'{基色x位*3*分辨率横*分辨率竖//8}B/帧的缓存')
网络速度 = 100  # Mbit/s
print(f'需要 {基色x位*3*分辨率横*分辨率竖/(网络速度*10**6)} s')
