import os, platform, time
aarch = platform.architecture()[0]
if "64bit" in aarch:
  os.system("clear")
  print(" \x1b[1;92mtool loading... ")
  import itssecret
else:
  print(" \x1b[1;91merror ")
