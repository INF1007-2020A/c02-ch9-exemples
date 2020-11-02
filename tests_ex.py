#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import inspect

from code_to_test import *


class MyTests(unittest.TestCase):
	def test_fibonacci_number(self):
		values = [i for i in range(10)]
		expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
		output = [fibo for fibo in fibonacci_numbers(10)]
		self.assertListEqual(
			output,
			expected
		)

	def test_build_recursive_sequence_generator(self):
		def fibo_def(last_elems):
			return last_elems[-1] + last_elems[-2]
		fibo = None
		try:
			fibo = build_recursive_sequence_generator([0, 1], fibo_def, False)
		except:
			self.fail("l'appel échoue")
		self.assertTrue(
			inspect.isgeneratorfunction(fibo),
			"L'objet retourné n'est pas un générateur"
		)
		values = [
			1,
			2,
			5,
			10
		]
		expected = [
			[0],
			[0, 1],
			[0, 1, 1, 2, 3],
			[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
		]
		output = [[fib for fib in fibo(v)] for v in values]
		self.assertListEqual(
			output,
			expected
		)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
