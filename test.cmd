@echo off

set tc=%1

if "%tc%" EQU "-1" (
   echo test case 1: good
   python make_zip.py --verbose --files file_a.txt file_b.txt
)

if "%tc%" EQU "-2" (
   echo test case 1: bad -- file missing
   python make_zip.py --verbose --files file_a.txt file_x.txt
)

if "%tc%" EQU "-3" (
   echo test case 1: good -- complete call
   python make_zip.py --verbose -r TTEVO_GEN4_B3_3_RC1 --output TTEVO_GEN4 --files subdir/file_sub_a.txt file_a.txt file_b.txt
)
