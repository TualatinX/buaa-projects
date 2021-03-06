# Chapter06: Application Layer

> 5%

## Key Points

- **DNS域名解析**、高速缓存
- SMTP和POP3
- HTTP

## 域名系统DNS

### 域名服务器

> page 255

- 根域名服务器
  - 任播：不同地点的主机，具有相同的IP
- 顶级域名服务器
- 权限域名服务器
- 本地域名服务器
  - 主域名服务器，辅助域名服务器

两种解析方式：递归查询/迭代查询 page 258

### 高速缓存

> page 259

为了提高DNS查询效率，并减轻根域名服务器的负荷和减少互联网上的DNS查询报文数量，在域名服务器中广泛使用了高速缓存。其用来存放最近查询过的域名以及从何处获得域名映射信息的记录。

## HTTP

URL格式

> page 266

- <协议>://<主机>:<端口>/<路径>
- 对于http而言，即为http://<主机>:<端口>/<路径>

操作过程

> page 267

- 面向事务的应用层协议
- 使用TCP协议来传输

非持续连接/持续连接 page 269

- 非持续连接
  - 传输时间+2xRTT
  - 一个RTT用于连接TCP
  - 一个RTT用于请求和接收万维网文档
- 持续连接
  - 非流水线方式：收到前一个相应后才能发出下一个请求（每访问一次对象都要用去一个往返时间RTT）
  - 流水线方式：收到相应报文之前就能够接着发送新的请求报文（客户访问所有的对象只需花费一个RTT时间）

Cookie存放于服务器端 page 273

## 邮件

> page 284

组成：

- 用户代理UA
- 邮件服务器
- 简单邮件传送协议（SMTP）
- 邮件读取协议（POP3）

### SMTP

> page 287

- 规定了在两个相互通信的SMTP进程之间应如何交换信息
- 不使用中间的邮件服务器
- 限于传送7位的ASCII码

### POP3

> page 289

- 也使用客户服务器的工作方式
- 在接收邮件的用户计算机中的用户代理必须运行POP3客户程序
- 读取了邮件之后，POP3服务器便将邮件删除，使得不能在多处查看

另有IMAP，二者对比 page 290
