from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from kya.app import Kya

def test_esc(qtbot, monkeypatch):
    """Pressing Esc should quit"""
    quit_calls = []
    monkeypatch.setattr(QApplication, 'quit', lambda: quit_calls.append(1))

    w = Kya('applauncher')
    w.show()
    qtbot.addWidget(w)
    qtbot.keyClick(w, Qt.Key_Escape)
    assert quit_calls == [1]
