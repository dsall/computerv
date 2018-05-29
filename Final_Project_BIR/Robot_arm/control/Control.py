from pynput import keyboard
import time

class Binder:
    def __init__(self):
        self.prs_bindings = {}
        self.rls_bindings = {}
        self.listener = None
        self.echo = False

    def start(self, block=False):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        if block:self.listener.join()

    def stop(self):
        keyboard.Listener.stop
        self.listener = None

    def handle_event(self, key, bindings, event):
        code = format(key)
        code = code.replace("'", '')
        code = code.replace("Key.", '')
        if self.echo: print(event, ':', code)
        codes = bindings.keys()
        if code in codes:
            func = bindings[code][0]
            args = bindings[code][1]
            func(*args)
            #self.listener.wait()

    def on_press(self, key):
        self.handle_event(key, self.prs_bindings, 'press')

    def on_release(self, key):
        self.handle_event(key, self.rls_bindings, 'release')

    def bind(self, code, func, args=[], on = 'p'):
        if on.startswith('p'): self.prs_bindings[code] = (func, args)
        if on.startswith('r'): self.rls_bindings[code] = (func, args)



# def test(text='werwerwrwe'):
#     print('hurrah:' + text)
#
#
# def test2(text='release'):
#     print('hurrah:' + text)
#
# a = Binder()
# a.echo=True
# a.bind('s', test)
# a.bind('s', test2, on='r')
# a.start()
#
# print(a.prs_bindings)
# time.sleep(5)
# a.stop()
# print('deon')
