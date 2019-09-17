from singleton import singleton
@singleton
class Foo():
    def __init__(self,arg):
        self.arg = arg
        print("create Foo",arg)
    def out(self):
        print(self.arg)
@singleton
class Fuu():
    def __init__(self):
        print("create Fuu")

if __name__ == "__main__":
  import threading
  import time
  import logging
  import random

  def worker_foo():
      r = random.random()
      time.sleep(int(r))
      d = Foo(r)
      d.out()
      print(d)
  def worker_fuu():
      r = random.random()
      time.sleep(int(r))
      d = Fuu()
      print(d)
  thread = []
  for i in range(10):
      t = threading.Thread(target=worker_foo)
      thread.append(t)
      t.start()
      t = threading.Thread(target=worker_fuu)
      thread.append(t)
      t.start()

  print('Waiting for worker threads')
  for t in thread:
      t.join()
  print('Done')
