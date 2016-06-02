from utils import add_cmd
import random
name = "coin"
cmds = ["coin"]

def flipper(irc,event,args):
    irc.reply(event, "{0} flips a coin..".format(event.source.split("!")[0]))
    irc.reply(event, "The coin lands on {0}.".format(random.choice(["heads", "tails"])))

add_cmd(flipper, "coin")
