from utils import add_cmd
import random
name = "coin"
cmds = ["coin", "cat", "dog"]

def flipper(irc,event,args):
    irc.reply(event, "{0} flips a coin..".format(event.source.nick))
    irc.reply(event, "The coin lands on {0}.".format(random.choice(["heads", "tails"])))
    
def cat(irc,event,args):
    irc.reply(event, "{0} throws a cat into the air..".format(event.source.nick))
    irc.reply(event, "The cat lands on its feet.")
    
def dog(irc,event,args):
    irc.reply(event, "{0} throws a dog into the air..".format(event.source.nick))
    irc.reply(event, "The dog lands on its {0}.".format(random.choice(["tail", "nose"])))

add_cmd(flipper, "coin")
add_cmd(cat, "cat")
add_cmd(dog, "dog")
