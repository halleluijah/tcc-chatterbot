import aiml
import os

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-standard.xml")
kernel.respond("load aiml b")

# clean the prompt
os.system('CLS')

# Press CTRL-C to break this loop
while True:
    #print kernel.respond(raw_input("Enter your message >> "))
    message = raw_input("Enter your message >> ")
    print "Alice >> " + kernel.respond(message)