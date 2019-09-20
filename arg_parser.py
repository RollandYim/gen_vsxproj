#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file: arg_parser.py
@time: 2019/9/20 11:26
@author: rolandxwren
@email: rolandxwren@gmail.com
"""
import optparse
import os


class ArgParser:
    """
    解析参数.
    """

    code_root = ""  # 代码根目录.
    solution_path = ""  # 工程保存路径.
    include_folders = ""  # 包含目录, 逗号分隔, 为空包含所有.

    need_show_help = False  # 显示帮助.

    _parser = optparse.OptionParser(usage="%prog --code code_root --solution solution_path")
    _parser.add_option("-c", "--code", dest="code_root", default="", help="code root, default current dir")
    _parser.add_option("-s", "--solution", dest="solution_path", default="", help="solution path, default current dir")
    _parser.add_option("-i", "--include", dest="include_folders", default="",
                       help="include folders, default including all")

    _include_folder_list = list()

    @classmethod
    def parse_args(cls, cur_dir):
        (option, args) = cls._parser.parse_args()

        cls.code_root = option.code_root
        if len(cls.code_root) == 0:
            cls.code_root = cur_dir
        cls.code_root = cls.code_root.replace("/", "\\")

        cls.solution_path = option.solution_path
        if len(cls.solution_path) == 0:
            cls.solution_path = cur_dir
        cls.solution_path = cls.solution_path.replace("/", "\\")

        cls._include_folder_list = list()
        cls.include_folders = option.include_folders
        for f in cls.include_folders.split(","):
            f = os.path.join(cls.code_root, f)
            f = f.replace("/", "\\")
            cls._include_folder_list.append(f)

        if hasattr(option, "help"):
            cls.need_show_help = option.help

    @classmethod
    def show_help(cls):
        """
        在终端显示帮助信息.
        :return: 无
        """
        cls._parser.print_help()

    @classmethod
    def dump_args(cls):
        return "{\n  code_root: " + cls.code_root + ",\n" \
               + "  solution_path: " + cls.solution_path + ",\n" \
               + "  include_folders: " + cls.include_folders + ",\n" \
               + "  _include_folder_list: " + ','.join(cls._include_folder_list) + ",\n" \
               + "}"

    @classmethod
    def get_solution_name(cls, def_name):
        pos = cls.solution_path.rfind("\\")
        if pos >= 0:
            return cls.solution_path[pos + 1:]
        return def_name

    @classmethod
    def is_folder_included(cls, folder):
        if len(cls._include_folder_list) == 0:
            return True
        for f in cls._include_folder_list:
            if folder.startswith(f) or f.startswith(folder):
                return True
        return False


g_arg_parser = ArgParser()
