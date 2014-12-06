import pickle
import logging
import unittest
import nose
import sys
from nose.plugins import Plugin


class TestSimpleCase(unittest.TestCase):

    def test(self):
        return True


class NosePlugin(Plugin):

    name = 'noseplugin'

    def prepareTest(self, test):
        logging.warn('Plugin count (before pickle): {}'.format(len(test.config.plugins.plugins)))

        pickled_config = pickle.dumps(test.config)
        unpickled_config = pickle.loads(pickled_config)

        logging.warn('Plugin count (after pickle): {}'.format(len(unpickled_config.plugins.plugins)))

    def startTest(self, test):
        logging.warn('Plugin was successfully loaded!!!!!')



if __name__ == '__main__':
    argv = ['nosetests', '--with-noseplugin']

    processes = sys.argv[1]

    if int(processes) > 1:
        argv.append('--processes={}'.format(processes))

    logging.warn('Running tests with {} processes'.format(processes))

    nose.main(argv=argv, addplugins=[NosePlugin()])