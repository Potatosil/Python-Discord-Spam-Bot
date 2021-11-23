import pyautogui, time
from time import sleep

spamnum = int(input(f"Input Number: "))
spamtext = input(f"What is the Message u want to send?: ")

time = 0
while time != 10:
	time += 1
	sleep(1)
	print("spammer waitinig.." + str(time))

def spam (msg, maxMsg):
	count = 0
	while count != maxMsg:
		count += 1
		print("sendmessage:" + str(count))
		pyautogui.write(msg)
		pyautogui.press("enter")
		if count == spamnum or count == spamnum*2 or count == spamnum*3 or count == spamnum*4 or count == spamnum*spamnum or count == spamnum*6 or count == spamnum*7 or count == spamnum*8 or count == spamnum*9 or count == spamnum*20:
			sleep(5)


spam(spamtext, spamnum)

sleep(2)

pyautogui.write("done")
pyautogui.press("enter")
