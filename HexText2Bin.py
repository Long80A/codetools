#!/usr/bin/python  
#encoding: utf-8
import binascii 
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Example: python ", sys.argv[0] , "in.txt", "out.exe"
        sys.exit(1)

    txt_name = sys.argv[1]
    bin_name = sys.argv[2]
    fh = open(txt_name, 'r')
    fout = open(bin_name,'wb')
    info = fh.read()
    asciistr = binascii.a2b_hex(info)
    fout.write(asciistr)
