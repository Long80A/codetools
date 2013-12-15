#!/usr/bin/python
#encoding: utf-8
import binascii 
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Example: python ", sys.argv[0] , "in.exe", "out.txt"
        sys.exit(1)

    bin_name = sys.argv[1]
    txt_name = sys.argv[2]
    fh = open(bin_name, 'rb')
    fout = open(txt_name,'w')
    info = fh.read()
    hexstr = binascii.b2a_hex(info)
    fout.write(hexstr)
