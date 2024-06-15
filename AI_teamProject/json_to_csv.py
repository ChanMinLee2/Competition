import json
import csv
import os

# JSON 파일 경로
json_file_path = 'Training.json'

# CSV 파일 경로 설정
csv_file_path = os.path.splitext(json_file_path)[0] + '.csv'

# JSON 파일 열기
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# CSV 파일 열기 및 데이터 작성
with open(csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # 헤더 작성
    writer.writerow(data[0].keys())

    # 데이터 작성
    for row in data:
        writer.writerow(row.values())

print(f"CSV 파일이 생성되었습니다: {csv_file_path}")
