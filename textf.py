#Добавление, изменение и удаление строк из файла
#Тупий Екатерина 3 курс, ИВТ
# добавление
textfile = "text.txt"
handle = open(textfile,'r')#открываем для заааапоминания
lines = handle.readlines()#зааапоминаем
handle.close()
handle = open(textfile,'w')#открываем для записи
text = "Lermontov"
for i in lines:
	handle.write(i)#заааписываем что запоминили
handle.write(text)
lines.append(text)#запоминаем новое
handle.close()
# изменение
handle = open(textfile,'w')
lines[0] = "Poem"
for i in lines:
	handle.write(i)
handle.close()
#удаление
handle = open(textfile,'w')
lines.pop(3)
for i in lines:
	handle.write(i)
handle.close()