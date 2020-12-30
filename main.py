import pywhatkit

number = input('Enter the WhatsApp no(add country code & no space): ')
msg = input('Enter the message: ')
hr, min = input('Enter time in format <hh:mm>: ').split(':')

pywhatkit.sendwhatmsg(number, msg, int(hr), int(min))
