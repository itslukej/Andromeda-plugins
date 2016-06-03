from utils import add_cmd
import random
name = "coin"
cmds = ["coin", "cat"]

def flipper(irc,event,args):
    irc.reply(event, "{0} flips a coin..".format(event.source.split("!")[0]))
    irc.reply(event, "The coin lands on {0}.".format(random.choice(["heads", "tails"])))
    
def cat(irc,event,args):
    irc.reply(event, "{0} throws a cat into the air..".format(event.source.split("!")[0]))
    irc.reply(event, "The cat lands on its feet.")

add_cmd(flipper, "coin")
add_cmd(cat, "cat")
