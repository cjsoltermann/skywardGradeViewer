#!/usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup

baseUrl = 'https://skyward.iscorp.com/scripts/wsisa.dll/WService=wsedujacksonvilleil/'

def makeRequest(program, data):
  r = requests.post(baseUrl + program, data)
  return r

def getSession(login, password):
  loginData = {
    'requestAction':'eel',
    'method':'extrainfo',
    'codeType':'tryLogin',
    'codeValue':login,
    'login':login,
    'password':password
  }
  r = makeRequest('skyporthttp.w', loginData)
  return r.text.lstrip('<li>').rstrip('</li>').split('^')

def submitSession(session):
  registerData = {
    'dwd':session[0],
    'web-data-recid':session[1],
    'wfaacl-recid':session[2],
    'wfaacl':session[3],
    'nameid':session[4],
    'duserid':session[5],
    'User-Type':session[6],
    'Allow-Special':session[8],
    'displaySecond':session[9],
    'hAutoOpenPref':session[10],
    'insecure':session[11],
    'enc':session[13],
    'encses':session[14]
  }

  r = makeRequest('sfhome01.w', registerData);
  return r.text

def getGradebook(session):
  encses = session[14]
  sessionid = session[1] + u'\u0015' + session[2]
  r = makeRequest('sfgradebook001.w', data = {'encses':encses,'sessionid':sessionid})
  return r.text

def listTeachers(gradebook):
  soup = BeautifulSoup(gradebook, 'html.parser')
  tables = soup.findAll('table')
  teachers = []
  for i in tables:
    teachers.append(i.text.strip().split('\n'))
  for teacher in teachers:
    if(len(teacher) == 1):
      print(teacher[0])
      continue
    print()
    print(teacher[1])
    print('\t'+teacher[0])
    print('\t'+teacher[2])
  

def main():
  if len(sys.argv) < 3:
    print("Usage:",sys.argv[0],"[LOGIN] [PASSWORD]") 
    exit(1)
  session = getSession(sys.argv[1],sys.argv[2])
  submitSession(session)
  gradebook = getGradebook(session)
  listTeachers(gradebook)

if __name__ == "__main__":
  main()
