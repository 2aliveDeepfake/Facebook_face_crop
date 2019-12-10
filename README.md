# Facebook_face_crop
영상 프레임에서 얼굴 부분 추출한 코드
</br>
</br>
동작 원리 : 이미지에서 눈(2) 코(1) 입(2) 5개 점을 찾아서 얼굴 위치 파악
</br>
</br>
# get_result_code 폴더로 이동
</br>
cd get_result_code
</br>
# precrop.py 실행
</br>
python precrop.py -i "../images/" -o "../output/"
</br>
( python precrop.py -i "input 이미지 디렉토리" -o "output 디렉토리" )

