from .singleton import singleton
@singleton
class Foo():
    def __init__(self,arg):
        self.arg = arg
        print("create ",self.num_instance," ",arg)
    def out(self):
        print(self.arg)
@singleton
class Fuu():
    def __init__(self):
        print("create")

if __name__ == "__main__":
  import threading
  import time
  import logging
  import random

  def worker():
      for i in range(2):
          r = random.random()
          time.sleep(int(r))
          d = Foo(r)
          d.out()
          print(d)
  thread = []
  for i in range(20):
      t = threading.Thread(target=worker)
      thread.append(t)
      t.start()

  print('Waiting for worker threads')
  for t in thread:
      t.join()
  print('Done')
