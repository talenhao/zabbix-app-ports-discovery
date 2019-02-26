zabbix low-level discovery插件.

自动发现服务器上所有应用的监听端口,并使用APP名称标记应用以免重复及增加可读性.

#Usage:
```
    Install:
        pip install zabbix-app-ports-discovery
    Add to you script:
        import applistenports
        getlistport = applistenports.GetListenPorts()
        items = getlistport.process()
        print(items)
输出格式为zabbix low-level discovery要求的json格式


{
    "data": [
        {
            "{#APPNAME}": "sshd__/usr/sbin/sshd",
            "{#APPPORT}": "22"
        },
        {
            "{#APPNAME}": "master__/usr/libexec/postfix/master",
            "{#APPPORT}": "25"
        },
        {
            "{#APPNAME}": "zabbix_agentd__/usr/sbin/zabbix_agentd",
            "{#APPPORT}": "10050"
        },
        {
            "{#APPNAME}": "zabbix_server__/usr/sbin/zabbix_server_pgsql",
            "{#APPPORT}": "10051"
        }
    ]
}

```
