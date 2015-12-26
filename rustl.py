# -*- coding: windows-1251 -*-
# Утилита для замедления чтения текста
# (может использоваться как профилактическое средство при повышенной скорости чтения в Интернете)
# Способствует обдумываю читаемого текста.

def w2u(s): return unicode(s,"cp1251")
def u2d(s): return s.encode("cp866")

# lib.ru:А.П.Чехов.Лошадиная фамилия
s = """
       Взбудоражилась вся усадьба. Нетерпеливый, замученный генерал пообещал дать пять рублей тому, кто вспомнит настоящую фамилию, и за Иваном Евсеичем стали ходить целыми толпами... 
       -- Гнедов! -- говорили ему. -- Рысистый! Лошадицкий! 
       Но наступил вечер, а фамилия всё еще не была найдена. Так и спать легли, не послав телеграммы. 
"""

def f(s):
  # http://stackoverflow.com/questions/1228299/change-one-character-in-a-string-in-python
  # s[6] = 'W'
  # http://www.cyberforum.ru/python/thread526284.html
  # return range(FROM, TO', STEP)
  n = len(s)
  a = list(s)
  for i in xrange(0,n,2):
    a[i] = a[i].upper() # Поднять каждый второй символ в верхний регистр
  for i in xrange(1,n,2):
    a[i] = a[i].lower() # Опустить все остальные (в windows-1251 python не умеет lower/upper)
  return "".join(a)

s = w2u(s)
s = s.replace("\n"," ")
s = s.replace("  ","")
print u2d(f(s))
