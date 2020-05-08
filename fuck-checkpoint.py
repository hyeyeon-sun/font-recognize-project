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
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name '__file__' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-790803b70910>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[0mconfig\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconfigparser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mConfigParser\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;31m#Config File 읽기\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 9\u001b[1;33m \u001b[0mconfig\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdirname\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrealpath\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m__file__\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msep\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m'envs'\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msep\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m'property.ini'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;31m#이미지 -> 문자열 추출\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
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
    "#문자열 -> 텍스트파일 개별 저장\n",
    "def strToTxt(txtName, outText):\n",
    "    with open(txtName + '.txt', 'w', encoding='utf-8') as f:\n",
    "        f.write(outText)\n",
    "\n",
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
    "            ocrToStr(fullName, outTxtPath, fname,'kor+eng')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
