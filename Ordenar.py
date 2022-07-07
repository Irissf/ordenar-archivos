from distutils import extension
from genericpath import exists
import os
import shutil
# importamos libreria os del sistema operativo

home = "D:/Users/Usuario/Downloads"

for file in os.listdir(home):
    if file.endswith(""):
        nameFileDivide = file.split(".") #dividimos el nombre para separar la extensión
        
        # los ficheros no tienen extension, por lo que si el array es de 1, podemos omitirlo
        if(len(nameFileDivide)>1):
            extension = (nameFileDivide[len(nameFileDivide)-1])
            nameFile = os.path.join("",file)

            #comprobar si existe un directorio con la extension que estamos iterando
            existeDir = os.path.isdir(home+"/"+extension)

            if(existeDir):
                #si existe movemos fichero
                shutil.move(((home)+"/"+nameFile),((home)+"/"+extension))
            else:
                os.mkdir((home)+"/"+extension)
                shutil.move(((home)+"/"+nameFile),((home)+"/"+extension))
