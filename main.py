import logging
from logging.handlers import RotatingFileHandler
import storage
from app import App

def _configure_logging():
 handler=RotatingFileHandler(storage.ROOT/'editor.log',maxBytes=512*1024,backupCount=2,encoding='utf-8')
 handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s'))
 root=logging.getLogger()
 root.setLevel(logging.WARNING)
 root.addHandler(handler)

if __name__=='__main__':
 _configure_logging()
 App().mainloop()
