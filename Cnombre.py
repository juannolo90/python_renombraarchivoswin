import os
import random
import time
diahora = str(time.strftime("%A%H%M_%S"))
print(diahora)
new = 'fondo.jpg'
dir = r'C:\\Wallpaper'
try:
    os.chdir(dir)
    acambiar='nuevo_'+diahora+'.jpg'
    os.rename(new,acambiar)
    filename =  random.choice(os.listdir(dir))
    path = os.path.join(dir,filename)
    old= str(path)
    os.rename(old,new) 
    print('Archivo Renombrado')
    time.sleep(3)
except Exception as e:
    print('Error en le ejecucion del propgrama ' + str(e))
    time.sleep(3)



