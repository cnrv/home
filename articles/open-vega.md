---
layout: default
---

# CNRV快讯: 来自NXP的ARM和RISC-V混合MCU: RV32M1

近日一款名为VEGAborad的MCU开发板发布，开发板还支持包括蓝牙BLE等射频收发器。

重点是这个开发板的主芯片为一颗来自Freescale/NXP的，包含两个ARM核和两个RISC-V核的MCU **RV32M1**。

![VEGAboard](/assets/images/articles/open-vega/open-vega-board.jpeg)

根据其在Github上公开的Datesheet:

- 一颗ARM Cortex-M4F和RISC-V RI5CY
    - 主频48MHz（高速模式可至72MHz）
    - 两者只能开启一个
    - 共享Cache并且共享总线Master接口
- 一颗ARM Cortex-M0+和RISC-V ZERO-RISCY
    - 主频48MHz（高速模式可至72MHz）
    - 两者只能开启一个
    - 共享Cache并且共享总线Master接口
- 片上1.25MB程序闪存，384KB SRAM，48KB ROM包含內建的Bootloader，支持片外存储接口扩展
- 176 VFBGA，9 mm x 9 mm
- 多协议无线收发器，支持蓝牙等协议
- 包含丰富的外设

![Vega Block Diagram](/assets/images/articles/open-vega/open-vega-block-diagram.png)

简单讲，这是一颗具有无线收发器的MCU芯片，内置高低性能的ARM和RISC-V核各两个，共4个。但只能同时开启当中的两个使用。

另外，国内IoT OS厂商睿赛德(RT-Thread)也即将发布对这款开发版的支持，可以持续关注这个Repo路径的更新: [RT-Thread/rt-thread/bsp/rv32m1_vega](https://github.com/RT-Thread/rt-thread/tree/master/bsp/rv32m1_vega)

Links:
- VEGA网站 [open-isa.org](http://open-isa.org)
- 开发板Github资源网址（包含SDK，文档等）: [repo: open-isa-org/open-isa.org](https://github.com/open-isa-org/open-isa.org)
- RTT支持: [RT-Thread/rt-thread/bsp/rv32m1_vega](https://github.com/RT-Thread/rt-thread/tree/master/bsp/rv32m1_vega)

*特约记者：郭雄飞, 2018年12月2日报道*
