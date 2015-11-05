#!/usr/bin/python

import os
import imaplib
import ConfigParser
import logging

# TODO add logging to .imapshell/imapshell.log
# TODO receives commands in mail body and creates from them executable script in /tmp/ or user defined directory
# TODO 
# TODO there have to be minimal security: only from authorized users with PGP/GPG signature or password 
# TODO if received command form unauthorized user have to reply with instructions and create lock file to prevent additional 
def getconf():
    """Reads configuration from files, returns dictionary or None"""

    if (os.path.isfile('imapshell.conf')) or (os.path.isfile(os.path.expanduser('~/.imapshell/imapshell.conf'))):
        cnf = {}
        config = ConfigParser.RawConfigParser()
        config.read(['imapshell.conf', os.path.expanduser('~/.impashell/imapshell.conf')])
        cnf['server'] = config.get('server', 'mailserver')
        cnf['user'] = config.get('server', 'user')
        cnf['mailpaswd'] = config.get('server', 'mailpaswd')
        cnf['secret'] = config.get('server', 'secret')
        cnf['folder'] = config.get('server', 'folder')
        cnf['shell'] = config.get('localuser', 'shell')
        cnf['sudo'] = config.get('localuser', 'sudo')
        cnf['sudopaswd'] = config.get('localuser', 'sudopaswd')
    else:
        logging.warning('There is no configuration file please create ~/.imapshell/imapshell.conf')
        cnf = None
    return (cnf)
def getmail(secret):
    """Receives mail from INBOX label by IMAP with specified string in header.
    
    Returns two strings """

if '__name__' == '__main__':
    cfg = getconf()
    if cfg['ssl'] == 'yes':
        server = imaplib.IMAP4_SSL(host=cfg['server'])
    else:
        server = imaplib.IMAP4(host=cfg['server'])
    
    server.login(cgf['user'],cfg['mailpaswd'])
    server.select(cfg['folder'])
    res, uids = server.search(None, 'ALL')
    res, a= server.fetch(1, '(BODY[HEADER])')

