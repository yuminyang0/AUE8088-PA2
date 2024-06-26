import json

# 파일 경로
file_path = 'datasets/kaist-rgbt/KAIST_annotation.json'

# JSON 파일 열기 및 확인
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("파일이 올바른 JSON 형식입니다.")
except json.JSONDecodeError as e:
    print("JSON 형식 오류:", e)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다:", file_path)
