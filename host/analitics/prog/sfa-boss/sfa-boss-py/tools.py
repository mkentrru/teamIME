import numpy as np
import matplotlib.pyplot as plt
import os
import configuration as conf


def die(msg):
	print(msg)
	exit(1)


class Data:
	ods = None  # original data set
	pds = None  # prepared data set

	def __init__(self, path, dtype):
		if not os.path.exists(path):
			die('Data: root path does not exists: ' + path)
		self.path = path
		self.dtype = dtype

	def add_dataset_from_file(self, subdir, name, filetype):
		if filetype is 'csv':
			name += '.csv'
		elif filetype is 'npy':
			name += '.npy'

		full_path = self.path + subdir + name
		if not os.path.exists(full_path):
			die('Data: dataset doesnot exists: ' + full_path)

		if filetype is 'csv':
			arr = np.loadtxt(full_path, delimiter=conf.csv_delimiter, dtype=self.dtype)
			if self.ods is None:
				self.ods = arr
			else:
				self.ods = np.append (self.ods, arr, axis=0)
		print(self.ods)


def plot_series(series, cuts_position, cuts_length, cuts_count):
	plot_config = cuts_count * 100 + 11
	plt.figure(figsize=(8, 9))

	for i in range(cuts_count):
		plt.subplot(plot_config)
		plot_config += 1
		plt.plot(
			range(cuts_position, cuts_position + cuts_length),
			series[cuts_position: cuts_position + cuts_length: 1],
			linewidth=1.0)
		cuts_position += cuts_length


def bar_series(series):
	plt.figure(figsize=(8, 9))
	plt.subplot(111)

	sub_columns_fix = 1
	sub_columns_count = np.shape(series)[0]
	columns_count = np.shape(series)[1]
	columns_width = sub_columns_fix * (sub_columns_count + 2)

	x = np.arange(0, columns_width * columns_count, columns_width)

	sub_column_index = 0
	for r in series:
		plt.bar(x + sub_column_index * sub_columns_fix, r, linewidth=0.1)
		sub_column_index += 1
	# plt.bar(x, avarage, linewidth=0.1)
