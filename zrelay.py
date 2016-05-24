#Fowards quieted users messages to a ops channel, only works when the channel has +z and the bot is op.
from utils import add_handler
from fnmatch import fnmatch
name = "zrelay"

def main(irc):
    if name not in irc.plugins.keys():
        irc.plugins[name] = {"syntax": "Message sent from quieted user ({0}): '{1}'", "channels": []}

def on_pubmsg(irc,conn,event):
    for chanset in irc.plugins[name]["channels"]:
        for quiet in irc.state['channels'][chanset['main']]['quiets']:
            if fnmatch(event.source, quiet):
                irc.privmsg(chanset['ops'], irc.plugins[name]["syntax"].format(event.source, " ".join(event.arguments)))
                break
    
add_handler(on_pubmsg, name)
