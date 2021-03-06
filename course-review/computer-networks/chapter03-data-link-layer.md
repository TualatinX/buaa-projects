# Chapter03: Data Link Layer

> 30%

## Key Points

- 数据帧的概念和可靠传输
- 奇偶校验和**循环冗余校验**
  - 计算
- 链路层协议（停等式ARQ、**回退N帧**、选择重传、**滑动窗口**、HDLC、PPP）
- MAC地址
  - 基本概念和用途
- 局域网的类别、**特点**和通信方式
- **CSMA/CD**算法的原理和应用
- **交换机**和网桥的工作原理

## Basics

> page 70

- 链路：一个结点到相邻结点的一段物理线路（有线or无线）
- 数据链路：除物理线路外加之必要的通信协议来控制数据的传输
- 帧：数据链路层将网络层交下来的数据（IP数据报，又数据报、分组、包）构成帧发送到链路上

> page 72

- 封装成帧：在一段数据（IP数据报）的前后分别添加首部和尾部（识别开始和结束）
- 最大传送单元MTU：数据部分长度上限
- 帧定界：SOH(Start Of Header) & EOT (End Of Transmission)
- 透明传输：加入转义字符ESC进行字节填充解决传输的数据恰为SOH or EOT的问题
- 差错检测：循环冗余检验CRC

## 差错检测

> page 74

- 奇偶校验：末尾添一位，使1的个数为偶数
- CRC校验：注意要在末尾补0（比除数少一位）

## 链路层协议

### 滑动窗口

- 停等式ARQ、**回退N帧**、选择重传

[Reference: 回退N帧协议与选择重传协议](https://www.cnblogs.com/yellowzunzhi/articles/10620377.html)

### HDLC

> page 76

高级数据链路控制HDLC(High-level Data Link Control)

现在已很少使用。

### 点对点协议PPP

> page 77

Point-to-Point Protocol

互联网用户通常都要连接到某个ISP才能接入到互联网。PPP协议就是**用户计算机和ISP进行通信**时所使用的数据链路层协议。

- 简单
  - 接受方每收到一个帧，就进行CRC检验。如果CRC检验正确，就收下这个帧；反之，就丢弃，其他什么也不做。
- 封装成帧
  - 帧定界符（标志帧的开始和结束的字符）
- 透明性
- 多种网络层协议
  - 能够在同一条物理链路上同时支持多种网络层协议（如IP和IPX等）的运行
- 多种类型链路
  - 串行/并行；同步/异步；低速/高速；电/光；交换（动态）/非交换（静态）
- 差错检测
- 检测连接状态
- 最大传送单元
  - MTU（数据链路层的帧可以载荷的数据部分的最大长度，而不是帧的总长度）
- 网络层地址协商
  - 提供机制使通信的两个网络层的实体能够通过协商知道或能够配置彼此的网络层地址。
- 数据压缩协商
  - 提供方法来协商使用数据压缩算法

> page 79

帧格式

- 首末为定界符

字节填充

- 转义符
- 零比特填充

## CSMA/CD算法

> !!! page 85

载波监听多点接入/碰撞检测

截断二进制指数退避

## 局域网

> page 82

类别、特点、通信方式

按网络拓扑进行分类：

- 星形网
- 环形网
- 总线网

局域网工作的层次跨越了数据链路层和物理层。

如何让众多用户能够合理而方便地共享通信媒介资源？

- 静态划分信道
- 动态媒体接入控制
  - 随机接入（必须有解决碰撞的网络协议）
  - 受控接入（探询/轮询）

以太网是在局域网中属于随机接入的那一种。

### 适配器

> page 84

进行数据串行传输和并行传输的转换。

由于数据率并不相同，因此在适配器中必须装有对数据进行缓存的存储芯片。

## MAC地址

> page 93

[Reference: MAC帧与PPP帧的区别](https://blog.csdn.net/u012316120/article/details/52432694)

（在局域网中）

## 网络设备&冲突域/广播域

[Reference](https://blog.csdn.net/modi000/article/details/80718070)

[Reference: 理解广播域和冲突域，二者有什么区别？](http://www.kokojia.com/article/27609.html)

### 冲突域&广播域

- 广播域（Broadcast Domain）

广播域是一个逻辑上的计算机组，接收同样广播消息的节点集合。如：在该集合中的任何一个节点传输一个广播帧，则所有其他能收到这个帧的节点都被认为是该广播帧的一部分。由于许多设备都极易产生广播，所以如果不维护，就会消耗大量的宽带，降低网络的效率。由于广播域被认为是OSI中的第二层概念，所以像Hub、交换机等第一、第二层连接的节点都被认为都是同一个广播域。而路由器，第三层交换机则可以划分广播域，即可以连接不同的广播域。

VLAN是用来把一个大的网络划分成多个小的虚拟网络，也就是它具有划分多个广播域、缩小广播域大小的功能。因为不同的VLAN间时不能直接通信的，VLAN间的通信必须依靠三层路由，就像不同子网间的连接一样，所以VLAN也是不转播广播包的，可以起到缩小广播域的作用。

- 冲突域（Collision Domain）

冲突域是一种物理分段，是指连接在同一物理介质上的所有站点的集合。这些站点之间存在介质争用现象（如传统以太网中的CSMA/CD介质检测原理），也就是它们在数据通信时需要共享某部分公用介质。冲突域指的是不会产生冲突的最小范围。在同一冲突域中的计算机等设备互联时，会通过同一个物理通道，同一时刻只允许一个设备发送的数据在这条通道中通过，其他设备发送的数据则要等到这个通道处于"闲"时才可以通过，否则会出现冲突，这时就可能出现大量的数据包因为延时而被丢弃或者丢失。

冲突域的大小可以衡量设备的性能，我们知道以前的集线器、中继器都是典型的共享介质的集中连接设备，都是工作在OSI/RM第一层--物理层上的设备。连接在这些设备上的其他设备都处于同一个冲突域中，不能划分冲突域，即所有的端口上的数据报文都要排队等待通过。

工作在OSI/RM第二层--数据链路层上的设备，如网桥和交换机也有冲突域的概念，但是它们都是可以划分冲突域的，也可以连接不同的冲突域。如果我们把集线器、中继器上的传输通道看成是一根电缆的话，则可将网桥、交换机的交换通道看成是一束电缆，有多条独立的通道（是矩阵设计的），这样就可以允许同一时刻进行多方通信了。

网桥与中继器类似，传统的网桥只有两个端口，可用于连接不同的网段。也就是可以把网桥看成是可以连接两个冲突域的设备。连接在同一网桥上的两个网段各自成为一个冲突域。交换机则是网桥的扩展，它有许多端口，而且每个端口就是一个冲突域，即一个或多个端口的高速传输不会影响其他端口的传输，因为不同端口发送的数据不需要在同一条通道中排队通过，而只是在同一端口中的数据才要在对应端口通道中排队。

### 中继器

信号在传输过程中会不断衰减，为了不让信号衰减对通信产生影响，产生了中继器：仅做放大信号用，把信号传导偏远的地方

### 集线器

试想，如果每个设备只有一个对外接口，那么意味着只能建立一对点好点的通信。为了能够让通信“一对多”，需要将信号复制广播，于是，产生了集线器：把一个端口的信息重复广播到其它7个端口上（假设是8口HUB）。所以HUB也可以叫做multiport repeater。广播会产生冲突，HUB都有碰撞检测功能，有碰撞基本上就是避让，一个人说完了，另一个人再说，所以效率低。

集线器的主要功能是对接收到的信号进行再生整形放大，以扩大网络的传输距离，同时把所有节点集中在以它为中心的节点上。它工作于OSI(开放系统互联参考模型)参考模型第一层，即“物理层”。集线器与网卡、网线等传输介质一样，属于局域网中的基础设备，采用CSMA/CD（一种检测协议）介质访问控制机制.

**集线器原理：**

基本上不具有类似于交换机的"智能记忆"能力和"学习"能力。它也不具备交换机所具有的MAC地址表，所以它发送数据时都是没有针对性的，而是采用广播方式发送。也就是说当它要向某节点发送数据时，不是直接把数据发送到目的节点，而是把数据包发送到与集线器相连的所有节点。

### 网桥

> page 99

最初人们使用的是网桥。网桥对收到的帧根据其MAC帧的目的地址进行转发和过滤。当网桥收到一个帧时，并不是向所有的接口转发此帧，而是根据此帧的目的MAC地址，查找网桥中的地址表，再确定将帧转发到哪一个接口，或是丢弃。

### 交换机

> page 99

以太网交换机本质上是多接口的网桥。

以太网交换机的每个接口都直接与一个单台主机或另一个以太网交换机项链，且全双工方式，具有并行性。

相互通信的主机都是独占传输媒体，无碰撞地传输数据。

交换表（地址表）通过自学习算法（page 100）逐渐建立。
