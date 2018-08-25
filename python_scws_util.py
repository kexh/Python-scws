# -*- coding: utf-8 -*-
'''
@author: kexh
@create: 2018/08/15
'''
import os.path
import _scws

'''
usage:

a = PyScws.get_scws_result("your_word", xdb_handle="type_1")
print(a)

'''

xdb_handle_dict = {
	"type_1": os.path.join("dir_path", "type_1.utf8.xdb"),
	"type_2": os.path.join("dir_path", "type_2.utf8.xdb"),
	"type_3": os.path.join("dir_path", "type_3.utf8.xdb")
}


class PyScws(object):
	@classmethod
	def get_scws(cls, xdb_handle=None):
		if xdb_handle is None or xdb_handle not in xdb_handle_dict:
			raise Exception("must a meaningful xdb handle to init.")
		xdb_path = xdb_handle_dict[xdb_handle]
		# print(xdb_path)
		_scws.scws_new()
		_scws.scws_set_charset("UTF8")
		_scws.scws_set_xdb(xdb_path)
		_scws.scws_set_multi(8)
		return _scws

	@classmethod
	def get_scws_result(cls, sent, xdb_handle=None):
		result = []
		try:
			d = cls.get_scws(xdb_handle).get_res(sent)
			for c in d:
				if c[1] == xdb_handle[:2] or len(c[0]) > 1:
					result.append(c[0])
		except Exception as e:
			print("error when get_scws_result[{}]: {}, {}".format(xdb_handle, sent, e))
		return result


