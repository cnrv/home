# RISC-V Day 2018Shanghai 会议内容预告

## RISC-V在大陆的发展

## 商业和开源的CPU实现（一）

前三个演讲分别来自晶心科技（AndesTech）、Syntacore和SiFive。

![andestech](/assets/images/articles/rv-impl-x3.png)

这三家公司都有自己的商业RISC-V CPU IP核。

今年作为RISC-V Linux元年，这三家公司都推出了可以支持Linux操作系统的CPU方案。

晶心科技(AndesTech)目前是亚太第一家主板上市的CPU IP公司，其产品已经广泛的被诸多消费类电子芯片采用。晶心支持RISC-V的CPU包括N25、NX25、A25和AX25，其中A代表是否支持Linux（包含MMU），X代表是否64位。本次研讨会晶心科技的CTO Charlie Su会带来演讲《面向AIoT的基于RISC-V的完整解决方案》。

Syntacore是一家来自俄罗斯的IP公司，专注于提供基于RISC-V的CPU IP，从低端的MCU到复杂的CPU都有提供(SCR1-SCR5)，其中SCR5是可以运行Linux的CPU，而SCR1则在Github上完全开源（Solderpad Hardware License）。来自Syntacore的Pavel Khabarov将会带来《兼容RISC-V的SCR处理器系列IP核》的演讲。

SiFive是由UC Berkeley的RISC-V开发团队孵化出的Fabless，而且最知名的RISC-V开源项目rocket-chip也有大量的SiFive工程师维护。SiFive今年发布了其Freedom U540芯片和开发板HiFive Unleashed，并且在Crowdsupply一售而空。U540是首个可以运行Linux的量产RISC-V芯片，他们在去年发布的HiFive1开发板也得到了广泛的关注。在这场研讨会上，来自SiFive的VP Jack Kang将会发布和介绍SiFive全新的IP系列，让我们拭目以待看看SiFive要给我们带来什么惊喜。（演讲：《来自SiFive的全新IP系列》）

另外，下午的演讲中会有若干个演讲会基于SiFive的HiFive1和HiFive Unleashed开发板来作为软件开发平台。

## 商业和开源的CPU实现（二）

Codasip是一家来自捷克的高科技公司并且很早就加入RISC-V基金会。这次他们的CTO Zdenek Prikryl将会介绍他们的RISC-V处理器自动化生成工具。小编的理解是这个工具可以根据客户的需求生成所需要的可读的RTL代码、基于UVM的Testbench和工具链等开发环境。而他们也有自己的一套高层次描述语言: CodAL，用于描述你所需要的处理器，以支持一些SIMD等高性能操作，最终的目的当然是为了得到最优化的系统。（演讲：《增强的RISC-V处理器自动化生成工具》）

![Codasip](/assets/images/articles/risc_v-codasip-bk-862x345.jpg)

在大陆地区非常活跃的胡振波在CPU设计领域具有非常深厚的功底和多年的经验。他开发了蜂鸟系列商业处理器，并且开源了其中的E203处理器，与此同时胡振波最近还出版了国内第一本讲述RISC-V的书《手把手教你设计CPU - RISC-V处理器篇》。买了书的同学不要忘了来找他签名～

![手把手教你设计CPU - RISC-V处理器篇](/assets/images/articles/huzhenbo-book.jpg)

蜂鸟处理器包含了EAI接口，这个接口支持扩展蜂鸟处理器来添加自定义指令。在蜂鸟的演讲之后，紧随着的是北大的两名本科生陈浩和陈强带来的简短演讲，他们利用蜂鸟的这个接口来开发了一个CNN加速器。小编也表示很期待。（演讲：《一个为RISC-V实现的CNN加速器》）

## 活动详细信息

**RISC-V Day 2018 Shanghai是RISC-V基金会本年度在中国大陆地区举办的唯一一场线下研讨会。**

时间: 2018年6月30日 8点开始注册

地点：上海市杨浦区邯郸路220号复旦大学光华楼东辅楼202室 **吴文政报告厅**




