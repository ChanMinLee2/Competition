import os
import glob
import argparse


parser = argparse.ArgumentParser(description='교통 CCTV 돌발상황 분석 프로그램')

# 입력받을 인자 
parser.add_argument('--data_dir', required=True, help='이미지 경로를 입력하세요') # 우리한테 new_images 경로
parser.add_argument('--result_dir', required=True, help='분석결과가 저장될 경로를 입력하세요') # 우리한테 final_labels 경로

# 인자값 저장
args = parser.parse_args()
print(args)

# 이미지 폴더에서 파일 경로 불러오기
file_pathes = glob.glob(os.path.join(args.data_dir,'*.jpg'))
print(file_pathes)

# 분석결과 저장 폴더 생성
if not os.path.exists(args.result_dir):
    os.makedirs(args.result_dir)

# 돌발 분석
for file_path in file_pathes:
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # 분석
    result_bboxes=[]

    # 분석 결과 작성
    result_txt = open(os.path.join(args.result_dir,file_name+'.txt'),'w')
    if len(result_bboxes):
        result_txt.close()
    else:
        for bbox in result_bboxes:
            result_txt.write("{:d} {:f} {:f} {:f} {:f}\n".format(bbox[0], bbox[1], bbox[2], bbox[3] bbox[4]))
        result_txt.close()

