#coding=UTF-8
import shutil
import os
import io


def openArchive(location):
  archive = io.open(f"static\data\pdf\{location}","r", encoding="utf-8")
  archive.readline()
  database= {
  "curso": archive.readline().rstrip("\n").strip("Curso:;"), 
  "instrutor": "Instrutor: " + archive.readline().rstrip("\n").strip("Instrutor:;"), 
  "local": "Local: " + archive.readline().rstrip("\n").strip("Local:;"),
  "carga": "Carga Horária: " + archive.readline().rstrip("\n").strip("Carga Horária:;"), 
  "data": "Data: " + archive.readline().rstrip("\n").strip("Data:;"), 
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

