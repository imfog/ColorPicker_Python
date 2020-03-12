import argparse
import cv2
import numpy as np


# コマンドライン引数の設定
parser = argparse.ArgumentParser(description='入力画像から色をピックアップする系のおっさん')

parser.add_argument('path', help='入力画像のフルパス')
parser.add_argument('-c', '--count', type=int,
                    default=3, help='初期値は3 , 3から7まで対応')

args = parser.parse_args()

img = cv2.imread(args.path)


# モザイク化する
# todo 縮小後が二桁にあるぐらいにする
def mosaic(src, ratio=0.01):
    small = cv2.resize(src, None, fx=ratio, fy=ratio,
                       interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

# テスト用の表示
def testshow(img):
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

testshow(mosaic(img))