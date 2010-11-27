#!/usr/bin/env python
"""Playing around with the multiprocessing module.
"""
import argparse
import logging
import multiprocessing
import os
import sys

def squarer(n):
    """Return the square of the given argument"""
    square = n*n
    print "Process {} squared {} to {}".format(os.getpid(), n, square)
    return square

def square_array_pipe(p):
    """Read an array off of a pipe, square all elements and send it back on."""
    a = p.recv()
    p.send([i*i for i in a])

def square_array_queue(q, array):
    """Square an array of number and put results individually on queue."""
    for i in array:
        s = i*i
        q.put(s)
    q.put(None)  # Indicate we're done

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    # Set up out output via logging module
    output = logging.getLogger(argv[0])
    output.setLevel(logging.DEBUG)
    output_handler = logging.StreamHandler()
    # Set up formatter to just print message without preamble
    output_handler.setFormatter(logging.Formatter("%(message)s"))
    output.addHandler(output_handler)

    # Argument parsing
    parser = argparse.ArgumentParser(
        description=__doc__, # printed with -h/--help
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    # Only allow one of debug/quiet mode
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("-d", "--debug",
                                 action='store_const', const=logging.DEBUG,
                                 dest="output_level", default=logging.INFO,
                                 help="print debugging")
    verbosity_group.add_argument("-q", "--quiet",
                                 action="store_const", const=logging.WARNING,
                                 dest="output_level",
                                 help="run quietly")
    parser.add_argument("-f", "--log_file",
                        help="Log output to file", metavar="FILE")
    parser.add_argument("-p", "--num_processes", type=int,
                        help="Use num processes", metavar="NUM")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    args = parser.parse_args()
    output_handler.setLevel(args.output_level)
    if args.log_file:
        file_handler = logging.FileHandler(args.log_file)
        file_handler.setFormatter(logging.Formatter("%(asctime)s:%(message)s"))
        output.addHandler(file_handler)
        output.debug("Logging to file {}".format(args.log_file))

    output.info("Creating pool with {} processes".format(args.num_processes))
    pool = multiprocessing.Pool(processes=args.num_processes)
    output.info("Spawning a map across processes")
    pool.map(squarer, range(10))
    output.info("Pool map completed")

    output.info("Sending array to process via pipe to be squared")
    a = range(10)
    print "Array: {}".format(a)
    parent_pipe, child_pipe = multiprocessing.Pipe()
    p = multiprocessing.Process(target=square_array_pipe, args=[child_pipe])
    parent_pipe.send(a)
    p.start()
    result = parent_pipe.recv()
    p.join()
    print "Result: {}".format(result)

    output.info("Reading squared array from process via queue")
    a = range(10)
    print "Array: {}".format(a)
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=square_array_queue, args=[q, a])
    p.start()
    while True:
        result = q.get()
        if result is not None:
            print "Result: {}".format(result)
        else:
            break
    p.join()

    return(0)

if __name__ == "__main__":
    sys.exit(main())
