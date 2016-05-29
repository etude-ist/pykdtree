# -*- coding: utf-8 -*-

#       pykdtree.py
#
#       Copyright 2016  Michał Tyburski (etude-ist) <logika01@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from ctypes import *
from ctypes.util import find_library

kdtree_lib = find_library("kdtree")
if kdtree_lib is None:
    print "kdtree library: https://github.com/jtsiomb/kdtree"
    exit(-1)
kdtree = CDLL(kdtree_lib)


class KdHyperrect(Structure):

    _fields_ = [
        ("dim", c_uint),
        ("min", POINTER(c_double)),
        ("max", POINTER(c_double)),
    ]


# This feels strange...
class KdNode(Structure):
    pass


class KdNode(Structure):

    _fields_ = [
        ("pos", POINTER(c_double)),
        ("dir", c_uint),
        ("data", c_void_p),
        ("left", POINTER(KdNode)),
        ("right", POINTER(KdNode)),
    ]


class ResNode(Structure):
    pass


class ResNode(Structure):

    _fields_ = [
        ("item", POINTER(KdNode)),
        ("dist_sq", c_double),
        ("next", POINTER(ResNode)),
    ]


# void (*destr)(void*);
callback_type = CFUNCTYPE(c_void_p, c_void_p)


class KdTree(Structure):

    _fields_ = [
        ("dim", c_uint),
        ("root", POINTER(KdNode)),
        ("rect", POINTER(KdHyperrect)),
        ("destr", callback_type),
    ]


class KdRes(Structure):

    _fields_ = [
        ("tree", POINTER(KdTree)),
        ("rlist", POINTER(ResNode)),
        ("riter", POINTER(ResNode)),
    ]


# struct kdtree *kd_create(int k)
kdtree_create = kdtree.kd_create
kdtree_create.restype = POINTER(KdTree)
kdtree_create.argstype = [c_uint]


# void kd_free(struct kdtree *tree)
kdtree_free = kdtree.kd_free
kdtree_free.restype = None
kdtree_argstype = [POINTER(KdTree)]


# void kd_clear(struct kdtree *tree)
kdtree_clear = kdtree.kd_clear
kdtree_clear.restype = None
kdtree_clear.argstype = [POINTER(KdTree)]


# void kd_data_destructor(struct kdtree *tree, void (*destr)(void*))
kdtree_data_destructor = kdtree.kd_data_destructor
kdtree_data_destructor.restype = None
kdtree_data_destructor.argstype = [POINTER(KdTree), callback_type]


# int kd_insert(struct kdtree *tree, const double *pos, void *data)
kdtree_insert = kdtree.kd_insert
kdtree_insert.restype = c_uint
kdtree_insert.argstype = [POINTER(KdTree), POINTER(c_double), c_void_p]


# int kd_insertf(struct kdtree *tree, const float *pos, void *data)
kdtree_insertf = kdtree.kd_insertf
kdtree_insertf.restype = c_uint
kdtree_insertf.argstype = [POINTER(KdTree), POINTER(c_float), c_void_p]


# int kd_insert3(struct kdtree *tree, double x, double y, double z, void *data)
kdtree_insert3 = kdtree.kd_insert3
kdtree_insert3.restype = c_uint
kdtree_insert3.argstype = [POINTER(KdTree), POINTER(c_double),
                           POINTER(c_double), POINTER(c_float), c_void_p]


# int kd_insert3f(struct kdtree *tree, float x, float y, float z, void *data)
kdtree_insert3f = kdtree.kd_insert3f
kdtree_insert3f.restype = c_uint
kdtree_insert3f.argstype = [POINTER(KdTree), c_float,
                            c_float, c_float, c_void_p]


# struct kdres *kd_nearest(struct kdtree *kd, const double *pos)
kdtree_nearest = kdtree.kd_nearest
kdtree_nearest.restype = POINTER(KdRes)
kdtree_nearest.argstype = [POINTER(KdTree), POINTER(c_double)]


# struct kdres *kd_nearestf(struct kdtree *tree, const float *pos)
kdtree_nearestf = kdtree.kd_nearestf
kdtree_nearestf.restype = POINTER(KdRes)
kdtree_nearestf.argstype = [POINTER(KdTree), POINTER(c_float)]


# struct kdres *kd_nearest3(struct kdtree *tree, double x, double y, double z)
kdtree_nearest3 = kdtree.kd_nearest3
kdtree_nearest3.restype = POINTER(KdRes)
kdtree_nearest3.argstype = [POINTER(KdTree), c_double, c_double, c_double]


# struct kdres *kd_nearest3f(struct kdtree *tree, float x, float y, float z)
kdtree_nearest3f = kdtree.kd_nearest3f
kdtree_nearest3f.restype = POINTER(KdRes)
kdtree_nearest3f.argstype = [POINTER(KdTree), c_float, c_float, c_float]


# struct kdres *kd_nearest_range
# (struct kdtree *kd, const double *pos, double range)
kdtree_nearest_range = kdtree.kd_nearest_range
kdtree_nearest_range.restype = POINTER(KdRes)
kdtree_nearest_range.argstype = [POINTER(KdTree), POINTER(c_double), c_double]


# struct kdres *kd_nearest_rangef
# (struct kdtree *kd, const float *pos, float range)
kdtree_nearest_rangef = kdtree.kd_nearest_rangef
kdtree_nearest_rangef.restype = POINTER(KdRes)
kdtree_nearest_rangef.argstype = [POINTER(KdTree), POINTER(c_float), c_float]


# struct kdres *kd_nearest_range3
# (struct kdtree *tree, double x, double y, double z, double range)
kdtree_nearest_range3 = kdtree.kd_nearest_range3
kdtree_nearest_range3.restype = POINTER(KdRes)
kdtree_nearest_range3.argstype = [POINTER(KdTree), c_double,
                                  c_double, c_double, c_double]


# struct kdres *kd_nearest_range3f
# (struct kdtree *tree, float x, float y, float z, float range)
kdtree_nearest_range3f = kdtree.kd_nearest_range3f
kdtree_nearest_range3f.restype = POINTER(KdRes)
kdtree_nearest_range3f.argstype = [POINTER(KdTree), c_double,
                                   c_float, c_float, c_float]


# void kd_res_free(struct kdres *rset)
kdtree_res_free = kdtree.kd_res_free
kdtree_res_free.restype = None
kdtree_res_free.argstype = [POINTER(KdRes)]


# int kd_res_size(struct kdres *set)
kdtree_res_size = kdtree.kd_res_size
kdtree_res_size.restype = c_uint
kdtree_res_size.argstype = [POINTER(KdRes)]


# void kd_res_rewind(struct kdres *rset)
kdtree_res_rewind = kdtree.kd_res_rewind
kdtree_res_rewind.restype = None
kdtree_res_rewind.argstype = [POINTER(KdRes)]


# int kd_res_end(struct kdres *rset)
kdtree_res_end = kdtree.kd_res_end
kdtree_res_end.restype = c_uint
kdtree_res_end.argstype = [POINTER(KdRes)]


# int kd_res_next(struct kdres *rset)
kdtree_res_next = kdtree.kd_res_next
kdtree_res_next.restype = c_uint
kdtree_res_next.argstype = [POINTER(KdRes)]


# void *kd_res_item(struct kdres *rset, double *pos)
kdtree_res_item = kdtree.kd_res_item
kdtree_res_item.restype = c_void_p
kdtree_res_item.argstype = [POINTER(KdRes), POINTER(c_double)]


# void *kd_res_itemf(struct kdres *rset, float *pos)
kdtree_res_itemf = kdtree.kd_res_itemf
kdtree_res_itemf.restype = c_void_p
kdtree_res_itemf.argstype = [POINTER(KdRes), POINTER(c_float)]


# void *kd_res_item3f(struct kdres *rset, float *x, float *y, float *z)
kdtree_res_item3f = kdtree.kd_res_item3f
kdtree_res_item3f.restype = c_void_p
kdtree_res_item3f.argstype = [POINTER(KdRes), POINTER(c_float),
                              POINTER(c_float), POINTER(c_float),
                              POINTER(c_float)]


# void *kd_res_item_data(struct kdres *set)
kdtree_res_item_data = kdtree.kd_res_item_data
kdtree_res_item_data.restype = c_void_p
kdtree_res_item_data.argstype = [POINTER(KdRes)]


class KdTreeWrapper(object):

    def __init__(self):
        pass

    def set_kdtree(self, kdtree, size):
        self.t = kdtree
        self.size = size

    def get_kdtree(self):
        return self.t.contents

    def create(self, size):
        b = kdtree_create(size)
        self.set_kdtree(b, size)

    def insert(self, pos, data):
        n = len(pos)
        arr_type = c_double * self.size
        arr = arr_type()
        i = 0
        while i < self.size:
            arr[i] = pos[i]
            i += 1
        kdtree_insert(self.t, byref(arr), (c_char_p)(data))

    def search(self, node, r):
        acc = []
        pos = (c_double * self.size)()
        i = 0
        while i < self.size:
            pos[i] = node[i]
            i += 1
        rst = kdtree_nearest_range(self.t, byref(pos), (c_double)(r))
        arr = (c_double * self.size)()
        while not kdtree_res_end(rst):
            d = kdtree_res_item(rst, byref(arr))
            vec = [arr[i] for i in range(self.size)]
            acc.append((vec, c_char_p(d).value))
            kdtree_res_next(rst)
        kdtree_res_free(rst)
        return acc

    def __del__(self):
        kdtree_free(self.t)


def new_kdtree(size=2):
    t = KdTreeWrapper()
    t.create(size)
    return t
