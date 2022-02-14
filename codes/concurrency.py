def learn_thread():
    """start and stop thread"""
    # Code to excute in an independent thread
    import time

    def countdowm(n):
        while n > 0:
            print("T-minus", n)
            n -= 1
            time.sleep(5)

    from threading import Thread

    # Create a thread object
    t = Thread(target=countdowm, args=(10,))
    # Launch this thread
    t.start()

    if t.is_alive():
        print("still running")
    else:
        print("complete")

    import time
    from threading import Thread

    class CountdownTask:
        def __init__(self):
            self._runing = True

        def terminate(self):
            self._runing = False

        def run(self, n):
            while self._runing and n > 0:
                print("T-minus", n)
                n -= 1
                time.sleep(5)

    c = CountdownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()
    c.terminate()
    t.join()
    import socket

    class IOTask:
        def terminate(self):
            self._runing = False

        def run(self, sock):
            sock.settimeout(5)
            while self._runing:
                try:
                    data = sock.recv(8192)
                    break
                except socket.timeout:
                    continue
            return

    import multiprocessing

    c = CountdownTask(5)
    p = multiprocessing.Pool(target=c.run)
    p.start()
