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

    

      
  
 
