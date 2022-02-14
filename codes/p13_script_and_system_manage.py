def parse_cmd():
    import argparse

    parser = argparse.ArgumentParser(description="search some files")
    parser.add_argument(dest="filenames", metavar="filename", nargs="*")
    parser.add_argument(
        "-p",
        "--pas",
        metavar="pattern",
        required=True,
        dest="patterns",
        action="append",
        help="text pattern to search for",
    )
    parser.add_argument("-v", dest="verbose", action="store_true", help="verbose mode")

    parser.add_argument("-o", dest="outfile", action="store", help="output file")

    parser.add_argument(
        "--speed",
        dest="speed",
        action="store",
        choices={"slow", "fast"},
        default="slow",
        help="search speed",
    )
    args = parser.parse_args()

    print(args.filenames)
    print(args.patterns)
    print(args.verbose)
    print(args.outfile)
    print(args.speed)


def prompt_password():
    import getpass

    # user = input('Enter your username: ')
    user = getpass.getuser()
    passwd = getpass.getpass()

    def svc_login():
        # function to handle password
        pass

    if svc_login(user, passwd):
        print("Yay!")
    else:
        print("Boo!")


def learn_log():
    import logging

    log = logging.getLogger(__name__)
    log.addHandler(logging.NullHandler)

    def func():
        log.critical("A Critical Error")
        log.debug("A debug message")


def learn_timer():
    import time

    class Timer:
        def __init__(self, func=time.perf_counter):
            self.elapsed = 0.0
            self._func = func
            self._start = None

        def start(self):
            if self._start is not None:
                raise RuntimeError("Already started")
            self._start = self._func()

        def stop(self):
            if self._start is None:
                raise RuntimeError("Not started")
            end = self._func()
            self.elapsed += end - self._start
            self._start = None

        def reset(self):
            self.elapsed = 0.0

        @property
        def running(self):
            return self._start is not None

        def __enter__(self):
            self.start()
            return self

        def __exit__(self, *args):
            self.stop()

    def countdown(n):
        while n > 0:
            n -= 1

    # Explicit start/stop
    t = Timer()
    t.start()
    countdown(100000)
    t.stop()
    print(t.elapsed)

