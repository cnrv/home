## 2018 RISC-V巴塞罗那 Workshop特别报道 (1)

### Welcome Address & Foundation Overview, Rick O' Connor

- 巴塞罗那的第8届RISC-V workship是开办以来第3大的workshop，有325人参加。
- 现在的统计，2018年第一季度，RISC-V基金会有约140个成员，来自25个国家。
- 下一次的RISC-V workshop 将在印度 IIT Madras Chennai, 7月18-19日。

![RISC-V Members](/assets/images/articles/risc-v-workshop-barcelona/riscv-members.jpg)

![RISC-V Growth](/assets/images/articles/risc-v-workshop-barcelona/riscv-growth.jpg)

### State of the Union: RISC-V, Krste Asanovic

- 指令集op-code空间关键词的区分：standard 现有的标准，custom 留给公司定义非标准扩展的部分，永远不会被标准使用，reserved 标准现在没有使用但是将来可能会被使用的空间。
- ISA compliance 测试是用来保证使用RISC-V标准指令集编译的用户态程序可以运行在所有RISC-V的处理器上。

> A system us minimally RISC-V-ISA-compliant if it runs claimed RISC-V unprivileged code correctly.

- Platform compliance 测试用来确定RISC-V软件的运行环境。该测试需要由生态环境的提供者来协助完成。

> A platform specification provides tight constraints on system configuration and options to support software ecosystem.
> Platform compliance test provided by relevant ecosystem.

- Linux ABI已经完成，内存模型现在正在公示期。
- RISC-V成立了安全工作小组： Rambus的Helena Handschuh为主席。

> - Develope consensus around best security practice.
> - Develope and publish RISC-V security road map.
> - Create repos and new attack trends, threats and countermeasures.
> - Identify top 10 open challenges in security.

### The State of RISC-V Software, Palmer Dabbelt & Arun Thomas

- LLVM 的RISC-V支持现在已经将RV32IM\[A\]FD支持融入主线，但是现在还差硬浮点、64位和RVC支持。
- U-boot融入主线（RV32I），谢谢Andes的协助
- UEFI支持正在进行中
- Zephyr, SeL4融入主线，FreeRTOS准备中
- GDB支持融入主线，但是还没有发布。OpenOCD的支持还不太稳定。现有商业支持：Seggar和Lauterbach, UltraSoC。IAR也在准备中。
- 商业仿真器： Imperas OVP可以在10s之内启动Linux
- 感谢AndesTech（Kito Cheng）对软件生态环境的贡献。

![Open Standard Work](/assets/images/articles/risc-v-workshop-barcelona/open-standard-work.jpg)

![RISC-V LLVM Porting](/assets/images/articles/risc-v-workshop-barcelona/riscv-llvm-porting.jpg)

###Vector ISA Proposal Update, Roger Espasa

- 最近的更新
  * Register types moved to an extension.
  * Widening multiples.
  * Debating whether reductions should be in base or not.
  * Worked on overlaying V-reg and F-reg to save state -- won't happen.
  * Fixed point vclip instruction (not really new, but reporting out)
  * Mask support for speculative vectorization
  * Possibility to fit integer MADD within encoding
- 问答环节：现在离V扩展草案完成最缺什么？答：缺少编译器的支持实现，现在等待Alex Bradbury在LLVM中对V的支持。
- 问答环节：如果V扩展能使用更多的op-code空间，什么功能可能会需要空间？答：对2D vector（矩阵计算）的支持可以利用更多的空间来加速。


### Rishiyur: Formal spec update

- 什么是ISA的formal spec？
  * 提供一个清楚的并且可以阅读的标准。
  * 精确精确并且完整。
  * 机器可读。
  * 可以被执行
  * 可以作为输入用于其他的工具中（定理证明，模型检查和验证工具）
- 现状：
  * 基金会将formal model和memory model小组分开。
  * 现有很多个formal模型（3个Haskell, 1个SAIL, 1个L3和1个Verilog）
  * Galios已经开始使用formal spec来验证指令集安全
- 在两三个月后，将发布formal spec的草案，支持RV32IMAC和RV64IMAC, user/super/machine三个优先级，RVSTO内存模型
- 希望能取代Spike成为RISC-V标准实现
- 将加入对浮点和RVWMO的支持。

### RISC-V Memory Consistency Model Task Group Update, Daniel Lustig

- RISC-V内存模型现在已经进入公示期（五月2日至6月16日）
- 对标准的修改部分：
  * 第6章：RISC-V弱内存模型RVWMO
  * 第20章：Zam扩展，支持非对齐的原子操作
  * 第21章：Zsto扩展，RISC-V的total store order模型扩展
  * 附录A：解释文档和Litmus测试
  * 附录B：Formal memory model specification
- 默认的原子操作不支持非对齐的原子操作
- 所有的硬软件都将用RVWMO(弱内存模型)为默认内存模型，但是可以选择使用RVSTO(total store order)内存模型。
- 使用RVSTO模型的代码不兼容RVWMO的硬件
- 7000多个Litmus测试已经上线，也可用于测试内存模型的兼容性

![RVWMO in a Nutshell 1](/assets/images/articles/risc-v-workshop-barcelona/rvwmo-1.jpg)

![RVWMO in a Nutshell 2](/assets/images/articles/risc-v-workshop-barcelona/rvwmo-2.jpg)

### Unleashing the Power of Data with RISC-V, Martin Fink 

- 世界上50%的数据都存储在西部数据的设备上
- 西部数据将实现自己的RISC-V核（两个），双发射，根据西部数据自己的数据负载情况优化的流水线
- 需要自己设计处理器的原因：通用处理器不符合专用数据场景的性能要求，接口不开放
- 将来，更多的设计需要在端节点快速的处理大量的数据
- 西部数据将分析现有硬件License的局限性
- 西部数据将在明年第一季度推出第一个带RISC-V处理器的芯片
- 提问环节：
  * 这个是西部数据自己设计的核吗？回答：是的，我们有自己的研发团队。我们可能会在将来开源我们的核。最困难的部分在片上连接部分。我们也许需要把这一部分剥离。
  * 西部数据实现的两个核有什么区别吗？为什么是2个？回答：实际上我们的芯片内有20多个核，这只是其中的两个。我们根据profiling的结果，对处理器实现做了调整，也使用了特殊指令。

![Unleashing the Power of Data with RISC-V](/assets/images/articles/risc-v-workshop-barcelona/wd-riscv.jpg)

### RISC-V Debugging: Custom ISA Extensions, Multicore, DTM Variants, Markus Goehrle

- Lauterbach现在占有了欧洲40%的JTAG市场
- 现在已经提供可调试同步多核和非同步多核的产品，基于debug spec v0.13
- 支持调试Linux
- 支持调试异质核系统
- 也可支持特殊指令集扩展（继承至TRACE32或者使用一个辅助调试单元）
- 希望RISC-V的debug实现不要碎片化

### Jeremy: GDB for RISC-V

- GDB已经融入主线，现在主要支持bare-metal模式
- GDB支持的是比较高级的抽象，其实核具体DTM的实现关系不大，更主要的是和平台以及ABI的定义联系更紧密
- 下面的工作：
  * 支持XML的目标平台定义
  * 支持内存映射表(memory map)
  * 支持远程IO（remote IO）
  * 支持non-DWARF的stack unwinding
  * 支持GDB simulator
  * 支持Linux调试

### Simon: software environment

- 现在的多核调试缺乏确定性、可重复性和可控性
- Imperas可以仿真U54-MC平台并在10秒内启动Linux
- 仿真速度100-2000MIPS
- 和UltraSoC共享调试接口，可实现仿真和实际调试接口的对换
- 提问： imperas的仿真是周期精确的吗？回答：不是，是指令精确的，支持时间模型，可以和外围设备直接交互

### HiFive Unleashed: World's First Multi-Core RISC-V Linux Dev Board, Yunsup Lee

- SiFive提供半导体云服务Silicon Cloud Services (SiFive SCS)
- 目标：设计芯片就如订购一个披萨
- 推出ChipLink: 基于TileLink支持一致性的片间串行通讯
- SPEC的libquntum性能不好是由于编译器的优化不够
- 和ADS合作将AI加速器放到FPGA内部，实现了HiFive+Microsemi+AI的人脸识别系统
- ONCHIP使用了Freedom Everywhere实现了180nm的流片代工，ONCHIP的模拟IP现在可以从SiFive获得
- SiFive开启了设计大赛，请大家建议基于HiFive Unleashed的工程，优胜者可获得流片机会
- 希望众多厂商一起将HiFive开发板的价格拉低

![SiFive U540](/assets/images/articles/risc-v-workshop-barcelona/sifive-u540.jpg)

![SiFive Unleash](/assets/images/articles/risc-v-workshop-barcelona/sifve-unleashed.jpg)

### HiFive Unleashed Expansion Options and Capabilities, Ted Marena

- Mi-V支持ChipLink，可作为HiFive的扩展板，也可以单独使用
- 支持PCIe hub，SSD
- 1999美金
- **Mi-V中的软核已开源**

![SiFive U540 and MicroSemi](/assets/images/articles/risc-v-workshop-barcelona/sifive-microsmi.jpg)

### Simulating Heterogeneous Multi-node 32-bit and 64-bit RISC-V Systems Running Linux and Zephyr with the Open Source Renode Framework, Michael Gielda

- Renode.io是一个开源的系统仿真器，可同时仿真多核。
- 也可用于仿真IoT无线局域网

### Debian GNU/Linux Port for RISC-V 64-bit, Manuel Fernandez Montecelo

- 2016年的ABI调整直接导致Debian和Fedora的porting停滞
- 2017年重新开始，现在已经完成1000多个包的编译
- 2017年3月份，实现了第二次干净的编译
- 完成了75%的平台无关包编译
- 完成了13k平台相关包中的9k个
- 已经有GUI支持

### Fedora on RISC-V, Richard Jones

- Fedora最从先融入主线的原则，不在支线保留关键特性的开发
- Redhat经常将好的商业软件买去然后开源其代码
- Fedora的编译历时两个月，16,000不同的编译生成和13,000个二进制文件
- 建议RISC-V指令集不要过分依赖于Linux的机制。成功的指令级必须要能支持Windows

![Fedora on RISC-V](/assets/images/articles/risc-v-workshop-barcelona/fedora-riscv.jpg)

### Smallest RISC-V Device for Next-Generation Edge Computing, Seiji Munetoh

- 实现了SHA256
- GF14LPP, Pulpino, RV32IMC, 2KB data SRAM 
- 0.076mm2 295umx296um

![Smallest RISC-V Chip](/assets/images/articles/risc-v-workshop-barcelona/smallest-riscv-ibm.jpg)

----

作者：宋威

编辑：郭雄飞

----

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/cn/80x15.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/">知识共享署名-非商业性使用-相同方式共享 3.0 中国大陆许可协议</a>进行许可。商业转载请联系作者。
