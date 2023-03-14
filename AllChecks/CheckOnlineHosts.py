import os

##Create a new file with the current arp output
arpNow = os.system(r"arp -a > C:\Users\oaloos\Desktop\arpNow.txt")

#Read the baseline arp output
with open (r"C:\Users\oaloos\Desktop\arp.txt") as old:
    OldArp = old.read()

#Read the current arp output
with open (r"C:\Users\oaloos\Desktop\arpNow.txt") as new:
    NewArp = new.read()

#Check if current matches the baseline
if OldArp == NewArp:
    print('True')
else:
    print('False')
