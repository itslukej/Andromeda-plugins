import socket, ssl
from utils import add_cmd

name="ssl"
cmds=["ssl"]

def getinfo(hostname):
    try:
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
        s.connect((hostname, 443))
        cert = s.getpeercert()
        
        subject = dict(x[0] for x in cert['subject'])
        issued_to = subject['commonName']
        issuer = dict(x[0] for x in cert['issuer'])
        issued_by = issuer['commonName']
        return [issued_to, issued_by]
    except:
        return "Error"
    
def ssl_info(irc,event, args):
    info = getinfo(" ".join(args))
    print(" ".join(args))
    if info == "Error":
        irc.reply(event, info)
        return None
    irc.reply(event, "The certificate is issued to {0} and issued by {1}".format(info[0], info[1]))

add_cmd(ssl_info, "ssl")
