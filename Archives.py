#coding=UTF-8
import shutil
import os
import io


def openArchive(location):
  archive = io.open(f"static\data\pdf\{location}","r", encoding="utf-8")
  archive.readline()
  database= {
  "curso": archive.readline().strip("\n").replace(";", " "), 
  "instrutor": archive.readline().strip("\n").replace(";", " "), 
  "local": archive.readline().strip("\n").replace(";", " "),
  "carga": archive.readline().strip("\n").replace(";", " "), 
  "data": archive.readline().strip("\n").replace(";", " "), 
  "nomes": []
  }
  archive.readline()
  for line in archive:
    database['nomes'].append(line.rstrip("\n").strip(";"))
  archive.close()
  os.remove(f"static/data/pdf/{location}")
  return database

def zipFile():
  dir = 'static/data/pdf'
  shutil.make_archive('PDF', 'zip', 'static/data/pdf')  
  for file in os.scandir(dir):
    os.remove(file.path)

