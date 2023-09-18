sec= input("seconds:")
sec= int(sec)
hour= sec // 3600
seconds = sec % 3600
minutes = sec // 60
seconds = sec % 60
print(sec,"seconds is",hour,"hours",minutes,"minutes",seconds,"seconds")