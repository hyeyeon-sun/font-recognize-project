{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from PIL import Image\n",
    "from pytesseract import *\n",
    "import configparser\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "config = configparser.ConfigParser()\n",
    "config.read(os.path.dirname(os.path.realpath(__file__)) + os.sep+'envs'+os.sep+'property.ini')\n",
    "\n",
    "def ortToStr(fullPath, ourTxtPath, fileName, lang='eng')\n",
    "    img = Image.open(fullPath)\n",
    "    txtName = os.path.join(outTxtPath,fileName.split('.')[0])\n",
    "    \n",
    "    ourText = image_to_string(img, lang=lang, config = )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name '__file__' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-f3dac51f4378>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[0mconfig\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconfigparser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mConfigParser\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;31m#Config File 읽기\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 9\u001b[1;33m \u001b[0mconfig\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdirname\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrealpath\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m__file__\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msep\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m'envs'\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msep\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m'property.ini'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;31m#이미지 -> 문자열 추출\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name '__file__' is not defined"
     ]
    }
   ],
   "source": [
    "from PIL import Image     #pip install pillow\n",
    "from pytesseract import * #pip install pytesseract\n",
    "import configparser\n",
    "import os\n",
    "\n",
    "#Config Parser 초기화\n",
    "config = configparser.ConfigParser()\n",
    "#Config File 읽기\n",
    "config.read(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'envs' + os.sep + 'property.ini')\n",
    "\n",
    "#이미지 -> 문자열 추출\n",
    "def ocrToStr(fullPath, outTxtPath, fileName, lang='eng'): #디폴트는 영어로 추출\n",
    "    #이미지 경로\n",
    "\n",
    "    img = Image.open(fullPath)\n",
    "    txtName = os.path.join(outTxtPath,fileName.split('.')[0])\n",
    "\n",
    "    #추출(이미지파일, 추출언어, 옵션)\n",
    "    #preserve_interword_spaces : 단어 간격 옵션을 조절하면서 추출 정확도를 확인한다.\n",
    "    #psm(페이지 세그먼트 모드 : 이미지 영역안에서 텍스트 추출 범위 모드)\n",
    "    #psm 모드 : https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage\n",
    "    outText = image_to_string(img, lang=lang, config='--psm 1 -c preserve_interword_spaces=1')\n",
    "\n",
    "    print('+++ OCT Extract Result +++')\n",
    "    print('Extract FileName ->>> : ', fileName, ' : <<<-')\n",
    "    print('\\n\\n')\n",
    "    #출력\n",
    "    print(outText)\n",
    "    #추출 문자 텍스트 파일 쓰기\n",
    "    strToTxt(txtName, outText)\n",
    "\n",
    "    \n",
    "    \n",
    "#문자열 -> 텍스트파일 개별 저장\n",
    "def strToTxt(txtName, outText):\n",
    "    with open(txtName + '.txt', 'w', encoding='utf-8') as f:\n",
    "        f.write(outText)\n",
    "\n",
    "        \n",
    "        \n",
    "        \n",
    "#메인 시작\n",
    "if __name__ == \"__main__\":\n",
    "\n",
    "    #텍스트 파일 저장 경로\n",
    "    outTxtPath = os.path.dirname(os.path.realpath(__file__))+ config['Path']['OcrTxtPath']\n",
    "\n",
    "    #OCR 추출 작업 메인\n",
    "    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__)) + config['Path']['OriImgPath']):\n",
    "        for fname in files:\n",
    "            fullName = os.path.join(root, fname)\n",
    "            #한글+영어 추출(kor, eng , kor+eng)\n",
    "            ocrToStr(fullName, outTxtPath, fname,'kor+eng')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<configparser.ConfigParser object at 0x000001DA79427CC0>\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "image_to_string() got an unexpected keyword argument 'encoding'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-38-8487a057e2ff>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     52\u001b[0m             \u001b[0mfullName\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mroot\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     53\u001b[0m             \u001b[1;31m#한글+영어 추출(kor, eng , kor+eng)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 54\u001b[1;33m             \u001b[0mocrToStr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfullName\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moutTxtPath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfname\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'kor+eng'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-38-8487a057e2ff>\u001b[0m in \u001b[0;36mocrToStr\u001b[1;34m(fullPath, outTxtPath, fileName, lang)\u001b[0m\n\u001b[0;32m     21\u001b[0m     \u001b[1;31m#psm(페이지 세그먼트 모드 : 이미지 영역안에서 텍스트 추출 범위 모드)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     22\u001b[0m     \u001b[1;31m#psm 모드 : https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 23\u001b[1;33m     \u001b[0moutText\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mimage_to_string\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mimg\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlang\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlang\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconfig\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'--psm 1 -c preserve_interword_spaces=1'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mencoding\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'utf-8'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     24\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     25\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'+++ OCT Extract Result +++'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: image_to_string() got an unexpected keyword argument 'encoding'"
     ]
    }
   ],
   "source": [
    "from PIL import Image     #pip install pillow\n",
    "from pytesseract import * #pip install pytesseract\n",
    "import configparser\n",
    "import os\n",
    "\n",
    "#Config Parser 초기화\n",
    "config = configparser.ConfigParser()\n",
    "print(config)\n",
    "#Config File 읽기\n",
    "config.read(os.path.dirname(os.path.realpath('__file__')) +os.sep + 'ocr'+ os.sep + 'envs' + os.sep + 'property.ini')\n",
    "\n",
    "#이미지 -> 문자열 추출\n",
    "def ocrToStr(fullPath, outTxtPath, fileName, lang='eng'): #디폴트는 영어로 추출\n",
    "    #이미지 경로\n",
    "\n",
    "    img = Image.open(fullPath)\n",
    "    txtName = os.path.join(outTxtPath,fileName.split('.')[0])\n",
    "\n",
    "    #추출(이미지파일, 추출언어, 옵션)\n",
    "    #preserve_interword_spaces : 단어 간격 옵션을 조절하면서 추출 정확도를 확인한다.\n",
    "    #psm(페이지 세그먼트 모드 : 이미지 영역안에서 텍스트 추출 범위 모드)\n",
    "    #psm 모드 : https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage\n",
    "    outText = image_to_string(img, lang=lang, config='--psm 1 -c preserve_interword_spaces=1',encoding='utf-8')\n",
    "\n",
    "    print('+++ OCT Extract Result +++')\n",
    "    print('Extract FileName ->>> : ', fileName, ' : <<<-')\n",
    "    print('\\n\\n')\n",
    "    #출력\n",
    "    print(outText)\n",
    "    #추출 문자 텍스트 파일 쓰기\n",
    "    strToTxt(txtName, outText)\n",
    "\n",
    "    \n",
    "    \n",
    "#문자열 -> 텍스트파일 개별 저장\n",
    "def strToTxt(txtName, outText):\n",
    "    with open(txtName + '.txt', 'w', encoding='utf-8') as f:\n",
    "        f.write(outText)\n",
    "\n",
    "        \n",
    "        \n",
    "        \n",
    "#메인 시작\n",
    "if __name__ == \"__main__\":\n",
    "\n",
    "    #텍스트 파일 저장 경로\n",
    "    outTxtPath = os.path.dirname(os.path.realpath('__file__'))+ os.sep + 'ocr'+config['Path']['OcrTxtPath']\n",
    "\n",
    "    #OCR 추출 작업 메인\n",
    "    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath('__file__'))+ os.sep + 'ocr' + config['Path']['OriImgPath']):\n",
    "        for fname in files:\n",
    "            fullName = os.path.join(root, fname)\n",
    "            #한글+영어 추출(kor, eng , kor+eng)\n",
    "            ocrToStr(fullName, outTxtPath, fname,'kor+eng')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dlgpd\\fontProject\\python\\ocr\\envs\\property.ini\n"
     ]
    }
   ],
   "source": [
    "from PIL import Image     #pip install pillow\n",
    "from pytesseract import * #pip install pytesseract\n",
    "import configparser\n",
    "import os\n",
    "\n",
    "config = configparser.ConfigParser()\n",
    "config.read('property.ini')\n",
    "\n",
    "print(os.path.dirname(os.path.realpath('__file__')) +os.sep + 'ocr'+ os.sep + 'envs' + os.sep + 'property.ini')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dlgpd\\fontProject\\python\\ocr\\\\resource\\\\ocr_result_txt\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "print(os.path.dirname(os.path.realpath('__file__'))+ os.sep + 'ocr'+config['Path']['OcrTxtPath'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jasom\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    from PIL import Image\n",
    "except mportError:\n",
    "    import Image \n",
    "    \n",
    "import pytesseract\n",
    "import cv2\n",
    "\n",
    "pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'\n",
    "\n",
    "text = pytesseract.image_to_string(Image.open('please.png'))\n",
    "print(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    " \n",
    "def  drawOpenCVText():\n",
    "    # Create a black image\n",
    "    img = np.zeros((640, 720, 3), np.uint8)\n",
    "    #change the black image to white image by filling all values with 255\n",
    "    img.fill(255)\n",
    " \n",
    "    \"\"\"                      \n",
    "    Availble font lists\n",
    "    FONT_HERSHEY_COMPLEX \n",
    "    FONT_HERSHEY_COMPLEX_SMALL\n",
    "    FONT_HERSHEY_DUPLE ㅇ\n",
    "    FONT_HERSHEY_PLAIN\n",
    "    FONT_HERSHEY_SCRIPT_COMPLEX\n",
    "    FONT_HERSHEY_SCRIPT_SIMPLEX\n",
    "    FONT_HERSHEY_SIMPLEX\n",
    "    FONT_HERSHEY_TRIPLEX ㅇ\n",
    "    FONT_ITALICㅇ\n",
    "    \"\"\"\n",
    "    fontscale = 1.0\n",
    "    # (B, G, R)\n",
    "    color = (0, 0, 0)\n",
    "    # select font\n",
    "    fontface = cv2.FONT_HERSHEY_COMPLEX\n",
    "    cv2.putText(img, text, (25, 40), fontface, fontscale, color)\n",
    "    \n",
    "    fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL\n",
    "    cv2.putText(img, text, (25, 80), fontface, fontscale, color)\n",
    "    fontface = cv2.FONT_HERSHEY_DUPLEX\n",
    "    cv2.putText(img, text, (25, 120), fontface, fontscale, color)\n",
    "    fontface = cv2.FONT_HERSHEY_PLAIN\n",
    "    cv2.putText(img, text, (25, 160), fontface, fontscale, color)\n",
    "    fontface = cv2.FONT_HERSHEY_SCRIPT_COMPLEX\n",
    "    cv2.putText(img, text, (25, 200), fontface, fontscale, color)\n",
    "    fontface = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX\n",
    "    cv2.putText(img, text, (25, 240), fontface, fontscale, color)\n",
    "    fontface = cv2.FONT_HERSHEY_SIMPLEX\n",
    "    cv2.putText(img, text, (25, 280), fontface, fontscale, color)\n",
    "    fontface = cv2.FONT_HERSHEY_TRIPLEX\n",
    "    cv2.putText(img, text, (25, 320), fontface, fontscale, color)\n",
    "    fontface = cv2.FONT_ITALIC\n",
    "    cv2.putText(img, text, (25, 360), fontface, fontscale, color)\n",
    " \n",
    "    cv2.namedWindow('putText Example')\n",
    "    #display and save image\n",
    " \n",
    "    cv2.imshow('putText Example', img)\n",
    "    cv2.imwrite(\"output.jpg\", img)\n",
    " \n",
    "    cv2.waitKey(0)\n",
    "    cv2.destroyAllWindows()\n",
    " \n",
    "def main():\n",
    "    drawOpenCVText()\n",
    " \n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import cv2 as cv\n",
    "\n",
    "def makeImage(name):\n",
    "    img_w = 826\n",
    "    img_h = 500\n",
    "    bpp = 3\n",
    "\n",
    "    img = np.zeros((img_h, img_w, bpp), np.uint8)\n",
    "    img.fill(255)\n",
    "\n",
    "    black = (0,0,0)\n",
    "\n",
    "\n",
    "    center_x = int(img_w / 2.0)\n",
    "    center_y = int(img_h / 2.0)\n",
    "\n",
    "\n",
    "    thickness = 1\n",
    "\n",
    "\n",
    "    location = (center_x - 130, center_y + 150)\n",
    "    font = name  # normal size serif font\n",
    "    fontScale = 1.3\n",
    "    cv.putText(img, 'Dasom', location, font, fontScale, black, thickness)\n",
    "\n",
    "    cv.imshow(\"image\", img)\n",
    "    cv.waitKey(0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "makeImage(cv.FONT_HERSHEY_TRIPLEX)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "location = (center_x - 200, center_y - 100)\n",
    "font = cv2.FONT_HERSHEY_DUPLEX  # hand-writing style font\n",
    "fontScale = 2\n",
    "cv.putText(img, 'Dasom', location, font, fontScale, black, thickness)\n",
    "\n",
    "\n",
    "location = (center_x - 150, center_y + 20)\n",
    "font = cv.FONT_HERSHEY_TRIPLEX  # italic font\n",
    "fontScale = 2\n",
    "cv.putText(img, 'Dasom', location, font, fontScale, black, thickness)\n",
    "\n",
    "\n",
    "\n",
    "location = (center_x - 130, center_y + 150)\n",
    "font = cv.FONT_ITALIC  # normal size serif font\n",
    "fontScale = 1.2\n",
    "cv.putText(img, 'Dasom', location, font, fontScale, black, thickness)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
