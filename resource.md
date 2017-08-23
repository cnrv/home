---
layout: default
---

# RISC-V资源列表

## 处理器实现

+ BOOM: Christopher Celio的RV64乱序处理器实现。Chisel, BSD Licensed。
  [[GitHub](https://github.com/ucb-bar/riscv-boom)]
  [[Doc](https://ccelio.github.io/riscv-boom-doc/)]

+ bwitherspoon: RV32微处理器。SystemVerilog, ISC Licensed。
  [[GitHub](https://github.com/bwitherspoon/core)]

+ F32: 针对FPGA的RV32微处理器，VHDL，BSD Licensed。
  [[GitHub](https://github.com/f32c/f32c)]

+ GRVI: Gray Research LLC. 针对FPGA优化的RV32微处理器，commercial licensed。
  [[Web](http://fpga.org/grvi-phalanx/)]

+ invicta: 一级流水线的RV32微处理器。Verilog，BSD Licensed。
  [[GitHub](https://github.com/qmn/riscv-invicta)]

+ Kamikaze: RV32微处理器。Verilog，MIT Liencensed。
  [[GitHub](https://github.com/rgwan/kamikaze)]

+ KCP53000: Samuel A. Falvo II的RV64处理器实现。Verilog, MPL Licensed。
  [[GitHub](https://github.com/KestrelComputer/polaris)]

+ nanorv32: 2机流水线的RV32实现。Verilog, GPLv2 Licensed。
  [[GitHub](https://github.com/rbarzic/nanorv32)]

+ OpenV: 支持RV32的开源微处理器，Verilog，MIT Licensed，OnChipUIS，来源于哥伦比亚的Universidad Industrial de Santander。
  [[GitHub](https://github.com/onchipuis/mriscv)]

+ ORCA: 支持RV32的开源微处理器，VHDL，BSD Licensed，VectorBlox。
  [[Github](https://github.com/VectorBlox/orca)]

+ PicoRV32: Clifford Wolf设计的(针对FPGA)RV32微处理器，Verilog，ISC Licensed。
  [[GitHub](https://github.com/cliffordwolf/picorv32)]

+ Potato: 针对FPGA的RV32微处理器。VHDL，BSD Licensed。
  [[GitHub](https://github.com/skordal/potato)]

+ RI5CY：支持RV32的开源微处理器
  - PULPino: SystemVerilog，Solderpad Licensed, 来源于苏黎世理工和博洛尼亚大学的PULP项目。
    [[GitHub](https://github.com/pulp-platform/pulpino)]
    [[Web](http://www.pulp-platform.org/)]

+ RIDERCORE: RISC-V乱序处理器设计。Verilog, BSD Licensed。
  [[GitHub](https://github.com/ridecore/ridecore)]

+ River: GNSS Senor Ltd.基于Rocket架构开发的RV64处理器。VHDL, BSD Licensed。
  [[GitHub](https://github.com/sergeykhbr/riscv_vhdl)]

+ Rocket: 支持RV64/32的开源处理器
  - Rocket-Chip: Chisel，BSD Licensed, Free chips project, UC Berkeley分离的开源工程。
    [[GitHub](https://github.com/freechipsproject/rocket-chip)]
  - Freedom: Chisel，Apache Licensed, SiFive, UC Berkeley分离的初创企业。
    [[GitHub](https://github.com/sifive/freedom)]
    [[Web](https://www.sifive.com/products/freedom/)]
  - lowRISC：Chisel+SystemVerilog，Solderpad Licensed, 从剑桥大学发起的非盈利组织。
    [[GitHub](https://github.com/lowrisc/lowrisc-chip)]
    [[Web](http://www.lowrisc.org)]
  - RoCC: the Rocket customized coprocessor interface 和Rocket处理器紧密互联的的协处理器接口。
    [[BSG](https://bitbucket.org/taylor-bsg/bsg_riscv)]

+ RV12: RoaLogic的RV32微处理器。Verilog, RoaLogic non-commercial Licensed。
  [[GitHub](https://github.com/RoaLogic/RV12)]

+ SCR1: Syntacore的RV32开源微处理器。SystemVerilog，Solerpad Licensed。
  [[GitHub](https://github.com/syntacore/scr1)]

+ SHAKTI：印度IIT-Madras的RISC-V处理器系列，Bluespec, BSD Licensed。
  [[Bitbucket](https://bitbucket.org/casl/shakti_public)]

+ Sodor: 教学用的RISC-V处理器。Chisel, BSD Licensed。
  [[GitHub](https://github.com/ucb-bar/riscv-sodor)]

+ uRV: 针对FPGA的RV32微处理器。Verilog，LGPLv3 Licensed.
  [[ohwr](http://www.ohwr.org/projects/urv-core)]

+ VexRiscv: 用SpinalHDL编写的针对FPGA的RV32微处理器。SpinalHDL, MIT Licensed。
  [[GitHub](https://github.com/SpinalHDL/VexRiscv)]

+ YARVI: Tommy Thorn设计的RV32I微处理器，Verilog，GPL2v Licensed。
  [[GitHub](https://github.com/tommythorn/yarvi)]

## 其他硬件模块

+ RISCV-FPU：王逵的FPU设计。
  [[GitHub](https://github.com/cnrv/RISCV-FPU)]

## 操作系统

+ Linux
  - [RISCVEMU](https://bellard.org/riscvemu/): Fabrice Bellard维护的RISC-V Linux emulator。
  - [JSLinux](https://bellard.org/jslinux/): Fabrice Bellard维护的可在浏览器里运行的RISC-V操作系统。

## 开发工具

+ GNU工具链
  - Palmer Dabbelt的[RISC-V GCC参数解释](https://www.sifive.com/blog/2017/08/14/all-aboard-part-1-compiler-args/)
  - Palmer Dabbelt的[FAQ about RISC-V Software](http://www.dabbelt.com/~palmer/riscv-faq.html)。

+ 运行和软件仿真
  - [rv8](https://rv8.io/): x86-64上的RISC-V二进制仿真器，支持即时编译优化。

+ 在线调试
  - [embecosm/riscv-gdbserver](https://github.com/embecosm/riscv-gdbserver): 由[Embecosm](http://www.embecosm.com/)维护的用于连接GDB的宿主机library，现在还只能用于调试Embecosm的picorv32 port。

## 文档

+ 标准文档
  - RISC-V User Spec V 2.20
    [[PDF](https://content.riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf)]
    [[GitHub](https://github.com/riscv/riscv-isa-manual)]
  - RISC-V Privileged Spec V 1.10
    [[PDF](https://content.riscv.org/wp-content/uploads/2017/05/riscv-privileged-v1.10.pdf)]
    [[GitHub](https://github.com/riscv/riscv-isa-manual)]

+ Chisel
  - [FAQ](https://github.com/freechipsproject/chisel3/wiki/Frequently-Asked-Questions)
  - [User Guide](https://github.com/freechipsproject/chisel3/wiki/Short-Users-Guide-to-Chisel)

+ Rocket
  - [SiFive platforms](https://www.sifive.com/documentation/)
  - [lowRISC SoCs](http://www.lowrisc.org/docs/)
  - [TileLink](https://www.sifive.com/documentation/tilelink/tilelink-spec/)
  - [Rocket-chip阅读笔记](https://github.com/cnrv/rocket-chip-read)


+ 教学课程
  - Cornell ECE 4750 [Computer Architecture](http://www.csl.cornell.edu/courses/ece4750/2016f/handouts.html)
  - MIT 6.175 [Constructive Computer Architecture](http://csg.csail.mit.edu/6.175/)
  - 丹麦技术大学(DTU) [Computer Architecture and Engineering course](https://github.com/schoeberl/cae-lab)

+ 书籍
  - David Patterson John Hennessy著：[Computer Organization and Design RISC-V Edition](https://www.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-812275-4)


## 其他

+ [CNRV中国镜像](https://github.com/cnrv/clone-helpers/blob/master/README.md): 提供大量RISC-V相关工程的国内下载镜像。
+ [RISC-V wiki](https://github.com/riscv/riscv-wiki/wiki): 由Arun维护的近官方RISC-V维科页面。
+ [What Every Programmer Should Know About Floating-Point Arithmetic](http://floating-point-gui.de/)

------------------------

**如果本页中的连接失效，请联系CNRV更新，或直接向网页源码[发送PR](https://github.com/cnrv/home/pulls)修正。**

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/cn/80x15.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/">知识共享署名-非商业性使用-相同方式共享 3.0 中国大陆许可协议</a>进行许可。
