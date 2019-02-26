# -*- coding: UTF-8 -*-

"""
 @Author: 郝天飞/Talen Hao (talenhao@gmail.com)
 @Site: talenhao.github.io
 @Since: 2019/02/22 15:42:46 PM
"""

import psutil
import json
import socket
import sys

name = "app listen ports"


class GetListenPorts(object):
    """

    """

    def __init__(self, exe=True, cmdline=False):
        """
        Do you want add exe and the first cmdline item in APPNAME?
        :param exe: exe
        :param cmdline: cmdline
        """
        self.exe = exe
        self.cmdline = cmdline

    def process(self):
        data = {}
        all_listen_app = []

        for proc in psutil.process_iter():
            for pcon in proc.connections():
                if pcon.status == psutil.CONN_LISTEN and pcon.family == socket.AF_INET:
                    macros_key_pairs = {}
                    # add exe or cmdline or both in macros {#APPNAME}, default only add exe.
                    app_name_list = [proc.name()]
                    if self.exe:
                        app_name_list.append(proc.exe())
                    if self.cmdline:
                        app_name_list.append(proc.cmdline())
                    app_name = "__".join(app_name_list)
                    macros_key_pairs["{#APPNAME}"] = app_name
                    # python2.x
                    if sys.version_info.major < 3:
                        try:
                            listen_port = pcon.laddr.port
                        except AttributeError:
                            listen_port = pcon.laddr[1]
                    # python3.x
                    else:
                        try:
                            listen_port = pcon.laddr.port
                        except AttributeError:
                            listen_port = pcon.laddr[1]
                    macros_key_pairs["{#APPPORT}"] = str(listen_port)
                    if macros_key_pairs not in all_listen_app:
                        all_listen_app.append(macros_key_pairs)
        data["data"] = all_listen_app
        jsonData = json.dumps(data, sort_keys=True, indent=4)
        return jsonData


if __name__ == "__main__":
    getlistport = GetListenPorts()
    items = getlistport.process()
    print(items)
