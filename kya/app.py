import asyncio
import os
import socket
import signal
from pathlib import Path
import sys

from PyQt5.QtWidgets import QApplication
from quamash import QEventLoop

from .kya import Kya

sockfile = Path(os.environ['XDG_RUNTIME_DIR']) / 'kya' / 'ipc_sock'

def get_sock():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sock.connect(str(sockfile))
        return sock
    except ConnectionRefusedError:
        sockfile.unlink()
    except FileNotFoundError:
        sockfile.parent.mkdir(parents=True, exist_ok=True)

class Application(QApplication):
    def __init__(self):
        super().__init__([])
        loop = self.loop = QEventLoop(self)
        asyncio.set_event_loop(loop)
        self.loop.add_signal_handler(signal.SIGINT, loop.stop)
        asyncio.async(asyncio.start_unix_server(self.ipc_handler, str(sockfile)))
        self.w = Kya('applauncher')
        self.w.show()
        self.ipc_cmds = {
            'show': self.w.show
        }

    def ipc_handler(self, reader, writer):
        cmd = yield from reader.readline()
        cmd = cmd.decode('utf-8').strip()
        # print(cmd)
        if cmd and cmd in self.ipc_cmds:
            self.ipc_cmds[cmd]()

    def exit(self, retcode=0):
        super().exit(retcode)
        sockfile.unlink()

def run():
    ipc_sock = get_sock()
    if ipc_sock is None:
        app = Application()
        app.loop.run_forever()
    else:
        ipc_sock.send(b'show\n')
