import pyautogui, time
from time import sleep

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
		if count == 5 or count == 5*2 or count == 5*3 or count == 5*4 or count == 5*5 or count == 5*6 or count == 5*7 or count == 5*8 or count == 5*9 or count == 5*20:	
			sleep(5)
				

spam("i am a spambot made by potato, sub to potato", 100)

sleep(2)

pyautogui.write("done")
pyautogui.press("enter")




		
