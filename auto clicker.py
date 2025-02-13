import pyautogui
import random
import time
import keyboard
import math  

min_delay = 0.02  
max_delay = 0.05 
zone_size = 30  
x_variance = 2  
y_variance = 2  
wait_time = 15  
pause_probability1 = 1 / 1000
pause_probability2 = 1 / 30
pause1 = 10
pause2 = .5 

def move_smoothly(x_start, y_start, x_end, y_end, duration):
    steps = int(duration * 100) 
    for i in range(steps):
        t = i / float(steps - 1)
        smooth_t = (1 - math.cos(t * math.pi)) / 2  
        x = int(x_start + (x_end - x_start) * smooth_t)
        y = int(y_start + (y_end - y_start) * smooth_t)
        pyautogui.moveTo(x, y)
        time.sleep(duration / steps)  

print(f"Autoclicker démarré ! Positionnez la souris dans la zone et attendez {wait_time} secondes.")
print("Appuyez sur 'Esc' pour arrêter.")

time.sleep(wait_time)

x, y = pyautogui.position()        
x_min = max(x - zone_size // 2, 0)  
x_max = x + zone_size // 2
y_min = max(y - zone_size // 2, 0)
y_max = y + zone_size // 2

try:
    while True:

        x_click = random.randint(x_min, x_max)
        y_click = random.randint(y_min, y_max)
    
        move_smoothly(x, y, x_click, y_click, duration=random.uniform(0.02, 0.05))

        pyautogui.click()

        if random.random() < pause_probability1:
            print("Pause de 10 secondes...")
            time.sleep(pause1)
        
        if random.random() < pause_probability2:
            print("Pause de 0.5 secondes...")
            time.sleep(pause2)

        time.sleep(random.uniform(min_delay, max_delay))

        if keyboard.is_pressed("esc"):
            print("\nAutoclicker arrêté.")
            break

except KeyboardInterrupt:
    print("\nProgramme arrêté manuellement.")
