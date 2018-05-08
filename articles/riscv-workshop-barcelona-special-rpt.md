## 2018 RISC-V巴塞罗那 Workshop特别报道

### Rick O'Conner: Welcome Address

- 巴塞罗那的第8届RISC-V workship是开办以来第3大的workshop，有325人参加。
- 现在的统计，2018年第一季度，RISC-V基金会有约140个成员，来自25个国家。
- 下一次的RISC-V workshop 将在印度 IIT Madras Chennai, 7月18-19日。

### Krste: State of the Union

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

### Palmer: State of Software

- LLVM 的RISC-V支持现在已经将RV32IM\[A\]FD支持融入主线，但是现在还差硬浮点、64位和RVC支持。
- U-boot融入主线（RV32I），谢谢Andes的协助
- UEFI支持正在进行中
- Zephyr, SeL4融入主线，FreeRTOS准备中
- GDB支持融入主线，但是还没有发布。OpenOCD的支持还不太稳定。现有商业支持：Seggar和Lauterbach, UltraSoC。IAR也在准备中。
- 商业仿真器： Imperas OVP可以在10s之内启动Linux
- 感谢Andes（Kito Cheng）对软件生态环境的贡献。


作者：宋威

----

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/cn/80x15.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/">知识共享署名-非商业性使用-相同方式共享 3.0 中国大陆许可协议</a>进行许可。商业转载请联系作者。
