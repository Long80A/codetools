codetools
=========

开源一些自己常用的小工具
1、二进制可执行文件和十六进制可显示字符转换工具
把可执行文件/home/test.bin转为十六进制显示
python Bin2HexText.py /home/test.bin test.txt
把十六进制字符转为二进制并运行
python HexText2Bin.py test.txt my.bin
chmod u+x my.bin
