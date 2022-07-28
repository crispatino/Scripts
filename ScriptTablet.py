
import pyautogui as pa
import time 

i = input("Cuantas veces quieres iterar?")
pa.press('Win') # Abre buscador
pa.write("Control panel") # Escribe control panel
pa.press("Enter") # Entra a control panel
time.sleep(1)
pa.hotkey('win', 'up') # Maximiza la ventana
time.sleep(1)
pa.moveTo(736,295) # Selecciona device and printers
pa.click()
time.sleep(1)
for ciclo in range(0,int(i)):
    pa.press('tab', presses=5)
    time.sleep(1)
    pa.write('Multimedia Devices')
    time.sleep(1)
    pa.press('tab', presses=2)
    time.sleep(1)
    pa.press('space')
    pa.moveTo(272,79)
    pa.click()
    pa.press('y')