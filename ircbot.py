"An IRC bot that responds to the users"
"Made By Sambuddha Basu"
import socket
SERVER = 'irc.freenode.net'
PORT = 6667
CHANNEL = '#randomchannel'
BOTNICK = 'askbot'
def ping():
    irc.send("PONG :pingis\n")
def sendmsg(msg, usernick=None):
    if usernick:
        irc.send("PRIVMSG " + CHANNEL + " :" + msg + " " + usernick + "\n")
    else:
	irc.send("PRIVMSG " + CHANNEL + " :" + msg + "\n")
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((SERVER, PORT))
irc.send("USER " + BOTNICK + " " + BOTNICK + " " + BOTNICK + " :I am a good bot\n")
irc.send("NICK " + BOTNICK + "\n")
irc.send("JOIN " + CHANNEL + "\n")
while 1:
    msg = irc.recv(2048)
    msg = msg.strip('\n\r')
    print msg
    if msg.lower().find(":hello " + BOTNICK) != -1:
	usernick = msg[1:msg.find("!uid")]
        sendmsg("Hello", usernick)
    if msg.lower().find(":hi " + BOTNICK) != -1:
	usernick = msg[1:msg.find("!uid")]
	sendmsg("Hi", usernick)
    if msg.lower().find(":creator " + BOTNICK) != -1:
	sendmsg("I am an IRC bot. My creator is Sambuddha Basu samgtr")
    if msg.lower().find(":site " + BOTNICK) != -1:
	sendmsg("Our website is at https://bmark.us/")
    if msg.lower().find(":repo " + BOTNICK) != -1:
	sendmsg("The central bookie repo is at https://github.com/bookieio/Bookie")
    if msg.lower().find(":issue " + BOTNICK) != -1:
	sendmsg("The open issues can be found at https://github.com/bookieio/Bookie/issues?state=open")
    if msg.lower().find(":pr " + BOTNICK) != -1:
	sendmsg("The pull requests can be found at https://github.com/bookieio/Bookie/pulls")
    if msg.find("PING :") != -1:
        ping()
