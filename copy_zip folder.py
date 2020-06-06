from zipfile import ZipFile
import os
from os.path import basename
import shutil, os

def Copy_Folder(Source,Destination):
    shutil.copytree(Source, Destination)
    print("Folder Copied Successful")
    Zip_Folder(Destination)
    print("Zip Folder created Successful")
def Copy_File(Source,Destination):
    shutil.copy(Source, Destination)
    print("File Copied Successful")
def Zip_Folder(Folder_Name):
    with ZipFile('sampleDir.zip', 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(Folder_Name):
            for filename in filenames:
               filePath = os.path.join(folderName, filename)
               zipObj.write(filePath, basename(filePath))
    
def Unzip_Folder(zip_File, Destination):
    with ZipFile(zip_File, 'r') as zipObj:
                 zipObj.extractall(Destination)
##x=Copy_Folder('/home/shiva/Downloads/Files/', '/home/shiva/sai')
##y=Copy_File('/home/shiva/Downloads/Files/Customer.csv', '/home/shiva/sai.csv')
##Zip_Folder('/home/shiva/sai')
##Unzip_Folder('sampleDir.zip','/home/shiva/sai1')
