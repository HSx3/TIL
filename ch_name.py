import os

os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):         # . = 현재 위치
#   os.rename(filename, "SAMSUNG " + filename)
    os.rename(filename, filename.replace("SAMSUNG", "SSAFY"))