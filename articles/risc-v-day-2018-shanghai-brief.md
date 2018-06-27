# RISC-V Day Shanghai有那些精彩内容?

**报名即将截止！**

RISC-V正在全世界范围内迅速的发展，目前RISC-V基金会的会员已经超过了100个。目前一些较早投入的公司已经纷纷有了产出，而很多公司也开始关注并且研究如何通过RISC-V来提高自身的竞争力；而对于学术界来说，RISC-V也意味着科研工作少了很多专利和授权方面的牵绊，可以更加专注在自己的科研领域里。

**RISC-V Day 2018 Shanghai将会是本年度唯一由基金会在中国大陆举办的研讨会**，议程：[https://tmt.knect365.com/risc-v-day-shanghai/agenda/1](https://tmt.knect365.com/risc-v-day-shanghai/agenda/1)

这次为期一天的研讨会汇集了大大小小一共16个演讲。上午的议程主要集中展示商业和开源的RISC-V CPU IP，分别来自AndesTech、SiFive、Syntacore、Codasip和来自国内的蜂鸟；而下午的议程则讨论处理器架构研究、处理器安全和的生态系统等话题。相比技术话题，或许能够认识更多业内的朋友对参会者来说更有价值。

小编在这里对整个活动做一个简单的预告。

## 商业和开源的CPU实现（一）

前三个演讲分别来自晶心科技（AndesTech）、Syntacore和SiFive。

![andestech](/assets/images/articles/rv-impl-x3.png)

这三家公司都有自己的商业RISC-V CPU IP核。今年作为RISC-V的Linux元年，这三家公司都推出了可以支持Linux操作系统的CPU方案。

晶心科技(AndesTech)目前是亚太第一个在主板上市的CPU IP公司，其产品已经广泛的被诸多消费类电子芯片采用。晶心支持RISC-V的CPU包括N25(F)、NX25(F)、A25和AX25，其中A代表是否支持Linux（包含MMU），X代表是否64位。本次研讨会晶心科技的CTO Charlie Su会带来演讲《面向AIoT的基于RISC-V的完整解决方案》。

Syntacore是一家来自俄罗斯的IP公司，专注于提供基于RISC-V的CPU IP，从低端的MCU到复杂的CPU都有提供(SCR1-SCR5)，其中SCR5是可以运行Linux的CPU，而SCR1则在Github上完全开源（Solderpad Hardware License）。来自Syntacore的Pavel Khabarov将会带来《兼容RISC-V的SCR处理器系列IP核》的演讲。

SiFive是由UC Berkeley的RISC-V开发团队孵化出的Fabless，而且最知名的RISC-V开源项目rocket-chip也有大量的SiFive工程师维护。SiFive今年发布了其Freedom U540芯片和开发板HiFive Unleashed，并且在Crowdsupply一售而空。U540是首个可以运行Linux的量产RISC-V芯片，他们在去年发布的HiFive1开发板也得到了广泛的关注。在这场研讨会上，来自SiFive的Jack Kang将会发布和介绍SiFive全新的IP系列，让我们拭目以待看看SiFive要给我们带来什么惊喜。另外，下午的演讲中会有若干个演讲会基于SiFive的HiFive1和HiFive Unleashed开发板来作为软件开发平台。（演讲：《来自SiFive的全新IP系列》）

## 商业和开源的CPU实现（二）

Codasip是一家来自捷克的高科技公司，而且很早就加入RISC-V基金会。这次他们的CTO Zdenek Prikryl将会介绍他们的RISC-V处理器自动化生成工具。小编的理解是这个工具可以根据客户的需求生成所需要的可读的RTL代码、基于UVM的Testbench和工具链等开发环境。而他们也有自己的一套高层次描述语言: CodAL，用于描述你所需要的处理器，以支持一些SIMD等高性能操作，最终的目的当然是为了得到最优化的系统。（演讲：《增强的RISC-V处理器自动化生成工具》）

![Codasip](/assets/images/articles/risc_v-codasip-bk-862x345.jpg)

在大陆地区非常活跃的胡振波在CPU设计领域具有非常深厚的功底和多年的经验。他开发了蜂鸟系列商业处理器，并且开源了其中的E203处理器，与此同时胡振波最近还出版了国内第一本讲述RISC-V的书《手把手教你设计CPU - RISC-V处理器篇》。买了书的同学不要忘了来找他签名～

![手把手教你设计CPU - RISC-V处理器篇](/assets/images/articles/huzhenbo-book.jpg)

蜂鸟处理器包含了EAI接口，这个接口支持扩展蜂鸟处理器来添加自定义指令。在蜂鸟的演讲之后，紧随着的是北大的两名在读研究生陈浩和陈强带来的简短演讲，他们利用蜂鸟的这个接口来开发了一个CNN加速器。小编也表示很期待。（演讲：《一个为RISC-V实现的CNN加速器》）

## RISC-V架构

下午的第一个演讲依然非常令人期待和兴奋，Greenwaves这家来自法国的公司，他们最近发布的GAP8处理器得到了非常多人的关注。 GAP8是一个8+1核的RISC-V处理器并且附加了CNN加速器，小编认为这是RISC-V在IoT领域的一个非常好的应用。8个基于RISC-V标准的处理器可以并行的处理数据（SPMD）同时配合专用的加速器可以实现诸如图像和语音识别等边缘计算的应用。CNRV前段时间也专门报道了用他们GAP实现的[Crazyflie 2.0无人机](https://mp.weixin.qq.com/s?src=11&timestamp=1530022835&ver=962&signature=boyPQ6JxrNkOvuVY9C3xdd09Lg7gbs0Vco7TAPUoqwxmk8J5giwK-OZW5*NUD06279hqdnD-ZmifkLqTPaI24hjKL0i-iwu3hPXf3LuZHErRn3SsccfHk*m8EJu-loC9&new=1)，这个无人机可以通过AI算法实现自主飞行。同时GAP8处理器的功耗也非常低，能支持长时间电池供电。这次研讨会来自Greenwaves的大牛将会介绍这款芯片及其架构，他讲一步步的分析如何分析和优化硬件资源来达成这项挑战的。（题目：《面向边缘计算的，基于RISC-V的高性能、超低功耗应用处理器及其架构》）

![GAP8](/assets/images/bi-weekly-rpts/2018-03-02/gap8_arch.png)

下午的第二个演讲是来自中科院计算所包云岗老师团队的黄博文带来的演讲《OpenPrefetch - 构造一个工业级的RISC-V处理器预取方案》，指令预取技术是提高处理器性能的非常有效的手段，但目前很多开源的处理器都缺少非常好的预取方案，这个演讲将会介绍OpenPrefetch，一个开放的指令预取研究平台，这将有效的帮助这些处理器提高其性能。

关于架构的最后一个演讲者是来自成都大学的本科生万瑞罡，别看他是个本科生，可是据我所知万同学从高中就开始设计CPU了，他将带来一个简短的演讲，来聊聊如何减少RISC-V处理器对FPGA资源的占用。（题目：《减少RISC-V软核处理器资源占用的若干方法》）

## RISC-V和安全

最近半年CPU安全领域事件频发，小编认为仍然处于不断进化中的RISC-V处理器能够非常好的从中吸收很多有益的养分。关于处理器安全，这次研讨会有两个演讲，一个来自工业界、一个来自学术界。

腾御安的王翔将会介绍他们将CoreBoot移植到RISC-V上的相关经验，腾御安是一家顶级的安全公司，他们帮助了很多互联网和手机企业提高了对他们服务和产品的安全性。（题目《自由的固件: Coreboot的RISC-V移植》）

来自信工所的李小欣将会介绍他们如何防御最近出现的AnC攻击。他们在开源的BOOM处理器上对进行了一系列安全性的研究和探索。(题目《在RISC-V SoC中防御新近出现的AnC攻击》)

## RISC-V的生态

生态系统的发展是体现一个指令集架构的发展成熟度的重要标志。

第一个演讲来自RedHat的傅伟，他将会带来关于Fedora在RISC-V处理器上最新的移植进展，Fedora发行版作为RedHat的先导项目，移植本身的复杂度并不低，最初的Fedora移植工作是在qemu上进行的，这次傅伟将会演示已经在HiFive Unleashed上成功启动的Fedora系统，果断来围观吧。

接下来两个演讲分别来自两家国内非常优秀的RTOS领域的公司，睿赛德的RT-Thread和翼辉的SylixOS。

RT-Thread很早就在HiFive1上将RT-Thread移植成功并且开源，这次他们会分享他们在RISC-V移植过程中的相关经验。（演讲：《RT-Thread的RISC-V移植》）

翼辉最近将其SylixOS移植到了HiFive Unleashed上，他们还在这个操作系统上成功的跑起来了QT，他们将带来一些现场演示，不容错过。可以看看他们最近发表的这篇文章[《SylixOS RISC-V 移植最新进展和技术分析》](https://mp.weixin.qq.com/s?src=11&timestamp=1530029517&ver=962&signature=dDHUqSWVg-SG-u7K-CtGoPt89do1I9rxL30rVqAfQz9C-unmWjO8hqT62kkcqg*5UApT53qdoC8F3dADRiWIqlu*pFds3bSNM*FgZfI-uAaPE00Hr3mPC0u124Esr1oU&new=1) （演讲《面向对称多处理器的RTOS SylixOS的RISC-V移植》）

介绍完操作系统，接下来会有两个开发板的介绍。

Microsemi为HiFive Unleashed设计了配套的FPGA开发板，并且提供了非常丰富的接口支持，这次他们讲演示在这个平台上实现一些深度学习的应用。（演讲：《在Mi-V Unleashed Kit上的基于Linux/RISC-V的深度学习演示》）

PerfXLab是一家非常优秀的技术公司，知名的线性代数库OpenBLAS就是他们创始人的作品，PerfXLab还提供商业化的数学库。基于他们在行业里深厚的经验，他们发布了Perf-V开发板，未来将会有很多相关领域的应用可以借助这块开发板进行。（演讲：《为RISC-V社区设计的Perf-V创意开发板及其未来生态支持》)

## 活动详细信息

时间: 2018年6月30日 8点开始注册

地点：上海市杨浦区邯郸路220号复旦大学光华楼东辅楼202室 **吴文政报告厅**

详细的注册指南请点击[这个链接](https://mp.weixin.qq.com/s?src=11&timestamp=1530030076&ver=962&signature=boyPQ6JxrNkOvuVY9C3xdd09Lg7gbs0Vco7TAPUoqww321769C*Vc5rPjySxFqFg1c1Ro-d92aR4PNAv-3ewl5cUCWqMz6GbgHaDRBo-WScABAS1Xi-gYl8zCrWMYRxz&new=1)

----

作者：郭雄飞

