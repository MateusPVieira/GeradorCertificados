import shutil

import os
 

def openArchive(location):
  archive = open(f"static\data\pdf\{location}", encoding ='ISO-8859-1')
  database= {"curso": archive.readline().rstrip("\n"), "instrutor": archive.readline().rstrip("\n"), "local": archive.readline().rstrip("\n"), "carga": archive.readline().rstrip("\n"), "data": archive.readline().rstrip("\n"), "nomes": []}

  for line in archive:
    database['nomes'].append(line.rstrip("\n")) 
  archive.close()
  return database

def zipFile():
  dir = 'static\data\pdf'
  shutil.make_archive('PDF', 'zip', 'static/data')  
  for file in os.scandir(dir):
    os.remove(file.path)

