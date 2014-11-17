filew = open('numbers.txt','w')
#user input
uinput = ''
count = 0
total = 0

#loop to get inputs
while True:
    uinput = input('Enter your numbers(press E to Exit):')
    if uinput == str():
        if uinput != 'e':
           break
        else:
            print ('Please Enter numbers only')
            continue 
    else:
       write = filew.write(uinput + '\n')
       count = count + 1
       total = total + int(uinput)

print ('Thank you for using my app')

Average = total / count
      
filew.write('Average is: '+ str(Average))
print ('the average is: ' + str(Average))