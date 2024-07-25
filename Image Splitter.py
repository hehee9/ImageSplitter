'''
이미지 분할기 v1.0.0
제작자 Hehee
https://x.com/HeheeMashup
'''

import os
import sys
import subprocess
import msvcrt

try:
    from PIL import Image
except ImportError:
    # PIL 모듈이 없는 경우
    install_pil = input("PIL 모듈이 설치되어 있지 않습니다. 설치하시겠습니까? (y/n) ")
    if install_pil.lower() == 'y':
        print("PIL 모듈을 설치합니다")
        # pip을 사용하여 Pillow 라이브러리 설치
        import subprocess
        subprocess.check_call([f"{sys.executable}", "-m", "pip", "install", "pillow"])
        from PIL import Image
        print("PIL 모듈이 설치되었습니다. 이미지 작업을 시작합니다")
    else:
        print("PIL 모듈이 설치되어 있지 않아 프로그램을 실행할 수 없습니다.")
        exit()

# 현재 폴더 경로 가져오기
folder_path = os.getcwd()

# 특정 폴더를 경로로 할 경우
#folder_path = "폴더 경로"


# 폴더 내의 모든 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".png", ".gif", ".webp"))]

if not image_files:
    print("폴더에 이미지 파일이 없습니다.\n\n아무 키나 눌러 종료")
    msvcrt.getch()
    exit()
    

''' ---------------- 이미지 분할 작업 ---------------- '''

for image_file in image_files:
    # 이미지 파일 경로 생성
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)
    width, height = image.size
    
    # 이미지를 좌우로 반으로 나누기
    left_image = image.crop((0, 0, width // 2, height))
    right_image = image.crop((width // 2, 0, width, height))
    
    # 새로운 파일 이름 생성
    base_name, ext = os.path.splitext(image_file)
    left_file_name = f"{base_name}_L{ext}"
    right_file_name = f"{base_name}_R{ext}"
    
    # 이미지 저장
    left_image.save(os.path.join(folder_path, left_file_name))
    right_image.save(os.path.join(folder_path, right_file_name))
    
    print(f"저장됨: {left_file_name} and {right_file_name}")

print("아무 키나 눌러 종료")
msvcrt.getch()
