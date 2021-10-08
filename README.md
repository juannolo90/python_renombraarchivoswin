# Problema o Necesidad: Organizacion bloqueo cambio de wallpaper y personalizacion de fondo en windows 10.

## Version 1.0  
   ### Programa python para renombrar archivos aletoreamente en un directorio
   * Tareas:
       * Renombrar archivo fondo.jpg por otro nombre(fechahora)
       * Seleccionar archivo de directorio aletoreamente
       * Renombrar archivo seleccionado a fondo.jpg para ser usado por la definicion y clave de registro
   ### Se desarrollo batch windows el cual se deja en cada inicio y apagado de windows
   #### Codigo
      echo "Cambiando Fondo"
      sleep 2
      C:\app\Cnombre.exe
      REG DELETE HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v Wallpaper /f
      REG ADD HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v Wallpaper /t REG_SZ /d "C:\Wallpaper\fondo.jpg"

    
## Indicar a windows ejecutar un programa al inicio y apagado de windows
   programa GPEDIT -->> Configuracion de equipo -->> Configuracion de Windows --> Scripts --> INICIO O APAGADO
      
      

  
 
![2021-10-08_17-20-20](https://user-images.githubusercontent.com/83789483/136620604-65613ec5-a956-4527-b713-0f81740a943d.png)
