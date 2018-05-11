## 2018 RISC-V巴塞罗那 Workshop特别报道 (2)

### Fast Interrupts for RISC-V, Krste Asanovic, University of California, Berkeley

 - 基金会成立新的快速中断工作小组来支持嵌套抢占的中断处理
 - 当前的RISC-V标准支持两种中断方案
   * 直接连到处理器核的本地异常。这种方式不需要仲裁，可以从scause CSR中直接确定中断源，但是只有两种中断源（软件中断和定时器中断）。
   * 全局中断。全局中断通过平台中断控制器(PLIC)管理并路由中断信号。PLIC在多个硬件核心之间转发中断，处理器需要读取中断控制器的寄存器确定中断源。
 - 当前的中断响应支持中断向量，每个向量有4字节的空间来放1条32比特的指令
 - 当前中断模式存在的问题：
   * 除了特权模式外，不支持中断抢占
   * 本地中断支持向量操作但是优先级是固定的
   * 中断向量表只能跳转到上下1MB范围内的中断服务程序
   * PLIC有可变的优先级，但是不支持向量操作
   * PLIC需要两次IO访问去完成或转发中断。
 - 内嵌式（inline）和函数式的中断服务程序都需要被支持
 - 内嵌式的中断服务需要中断服务自己去保存需要使用的寄存器，速度较快，上下文切换代价较小
 - 函数式的中断服务程序需要中断调用去保存上下文，代价较大，使用硬件加速效果也不会明显
 - 解决上下1MB的限制：
   * 在中断向量中保存函数指针需要先读取指针，难以实现原子操作。
   * SiFive的建议是使用新的中断优先级，然后用指令将可跳空间扩大至2GB
 - 支持中断抢断之后，中断的优先级也需要保存进上下文。
 - 可以尝试将mpp/mil/mie融入mcause寄存器来减少上下文保存代价
 - 问题：是否会发布实例代码？会。
 - 现在为什么只留了4B给每一个中断向量？节约空间，因为很多指令都跳转到相同的地址，不需要保存上下文。如果保存上下文，调用需要四条指令，开销太大。

### RISC-V DSP (P) Extension Proposal, Chuan-Hua Chang, Andes Technologies and Richard Herveille, RoaLogic BV

- P扩展指令集将定义Packed-SIMD指令
- Andes目前已经被超过25亿的嵌入式SoC使用
- Andes的Change是P扩展指令集工作小组的主席，预计P扩展将首先基于Andes的V3 DSP指令集
- P指令集将基于通用寄存器，支持8/16/32宽度的数据类型。采用GPR比独立的寄存器要更加高效，支持高性能的通用程序开发
- P指令集希望支持的数据类型和指令可以被编译器很好的识别
- 如果编译器不能识别，将提供对软件开发人员提供的Instrinic函数以方便其使用这些DSP指令
- 最后的办法是提供相应的库和中间件
- 在RV32中支持对64比特的Vector操作需要使用一对RV32中的寄存器，需要编译器自动生成DSP指令
- 提问：编译器支持的难度在哪里？答：似乎数据类型是最难的部分


### RISC-V ISA Cryptographic Extensions Proposal Summary, Richard Newell, Microsemi 

- 介绍了ucTEE和crypto扩展的情况
- 该组现在已经成为会员最多的工作组
- ucTEE是现在是针对一个没有MMU的系统
- 为了更好的开展工作，ucTEE和crypto现已拆分为两个工作组

### Formal Assurance for RISC-V Implementatons, Daniel Zimmerman, Galois and Joseph Kiniry, Galois

- 我们如何确保指令集定义的准确性
- 有两件事情需要证明：
  * 系统做该做什么
  * 系统不该做任何其他的（经常被忽略）
- 怎么能确定一个处理器是RV32I兼容的呢？ 答案是形式化的验证它
- 是否可行呢？等价证明工具通常存在于Verilog或者SystemVerilog相关的工具
- 所以为了实现这一点，需要：
  * 一份机器可读的标准，以及对于一个实现的正确性安全性标准(Specification)
  * 一种证明其一致性的方法
  * 简化、理解和探索这些测量的方法
- 现在的模型很多，如何选取测试和验证模型？使用大量的测试，使用仿真覆盖率，使用多模型的仿真结果比较
- 安全属性这部分是最难的，非常难于证明。在证明这件事上很难达成一致。
- 一个领域特定语言：LANDO，用来描述架构、正确性和安全性相关的属性
- 有效的度量很重要：我们必须帮助工程师去理解和了解其设计的有效性，并且将其可视化
- 挑战
  * 精确的衡量
  * 安全度量的发展
  * 需要商业工具在有效性证明、验证和可度量性方面的支持

### Undefined, Unspecified, Non-deterministic, and Implementation Defined Behavior in Verifiable Specifications, Cliford Wolf, Symbiotic EDA

- 未定义的行为：在某种情况下不会去做的；如果一些程序尝试做了未规定的事情，对于该程序来说整个规范是无效的
- 未定义的值：未定义操作得到的结果
- 未指定的值：指令没有做其他破坏性更大的事情，仅仅是返回了规范没有明确指定的值
- 具体实现定义的行为/值：某些时候这是相比其他方法来说最好的选择
- RISCV-V 规范里存在漏洞
- 提倡使用实现定义的行为
- 完整定义的行为最好不过了

### Foundatonal HPC Systems for 2020 and Beyond, Steven Wallach, Micron Technology

- 2.0的体系结构需要考虑安全，是一个已内存为核心的体系结构
- 2.0体系结构将使用128比特的地址空间，其中高64比特为目标ID,一个唯一的和ISA无关并且时不变的ID(带版本的)
- 低64比特为子节地址，所以RV64和RV128直接兼容
- 使用安全体系结构，加密指令，通过彻底隔离来抵御Spectre和Meltdown攻击
- 3.0的体系结构? 使用语言来提高安全

### Mateo: BSC processor initiative

- BSC现有400多的研究人员
- HPC的应用需要RISC-V支持长向量，有限的控制流，分层次的加速，支持MPI和OpenMP，并支持机器学习的加速
- BSC在招人

### Securing High-performance RISC-V Processors from Time Speculaton, Christopher Celio, Esperanto and Jose Renau, Esperanto

- 我们依然可以不用修改ISA就构建高性能的CPU: 我们只需要改进微架构就可以
- 如何理解时间攻击？并提出N种解决方案。见Slide
- 我们可以定义时间域，一个时间域不能影响另一个时间域的性能，但是时间域很难定义
- 从大层面来说，我们需要消除假设执行的痕迹，一旦假设失败，必须销毁所有的痕迹，而且要避免影响内存带宽（也是侧信道）
- RISC-V需要做什么？
    - 不需要增减指令（除了为了优化性能所需的Save/Restore）
    - 讨论和沟通好的微架构设计机制
    - 在平台标准上的尽可能多的合作
    - 要知道很多设计决策都影响安全性
    - 性能计数器的可见性不应跨越时域
- 请给我们分享你的想法，给出你的反馈
- **我们希望RISC-V成为一个成功的指令集**

![Espertante](/assets/images/articles/risc-v-workshop-barcelona/esperante-1.jpg)

### Use of RISC-V on Pixel Visual Core, Mat Cockrell 

- Pixel Visual核是由谷歌从头自行设计的领域专用处理器（Domain Specific Core)，包含8核 A53
- 其总线上又多个加速器
- 在众多RISC-V核中，Google选择了RI5CY

![Google RISC-V RI5CY](/assets/images/articles/risc-v-workshop-barcelona/google-ri5cy.jpg)

### Linux-Ready RV-GC AndesCore with Architecture Extensions, Charlie Su, Andes Technologies

- CoDense：在RVC基础上代码密度的进一步提高
- 支持P-ext中的DSP/SIMD指令
- 支持定制化指令
- 非指令集扩展（基于CSR）：向量中断和缓存管理等
- N25/NX25 V5 AndesCore
    - 在TSMC 28nm HPC工艺下：小核：3.7万门 @ 1GHz, 大核：15.9万门 @ 1.15GHz
    - 单精度除法需要15个周期，双精度29个周期，可后台执行
    - 软件友好的非对齐数据存取（如果不支持将导致异常处理100个周期左右）

![Andes DSP P-ext](/assets/images/articles/risc-v-workshop-barcelona/andes-1.jpg)

### Processor Trace in a Holistc World, Gajinder Panesar, UltraSoC

- 提供可视化的程序执行过程很重要
- 一种实现的方式是记录处理器分支记录
- For cores retire N instructions, need to replicated N times
- 如果一个核可以在一个周期内执行N条指令，trace的接口就要扩大N倍
- 对于多发射的核心，trace的接口也必须扩大至相应指令发射数
- 输出需要被编码（压缩）
- 现在每条指令需要平均0.252个bit，压缩的效率还不错（不包含打包所需的额外开销）
- RISC-V的trace工作小组将致力于标准化trace的格式和接口
- 问：trace在host端实现分支预测可以提高其压缩率么？答：可以

![UltraSoC 1](/assets/images/articles/risc-v-workshop-barcelona/ultrasoc-1.jpg)

![UltraSoC 2](/assets/images/articles/risc-v-workshop-barcelona/ultrasoc-2.jpg)

### RISC-V Meets 22FDX: an Open Source Ultra-low Power Microcontroller Platorm for Advanced FDSOI Technologies, Pasquale Davide Schiavone, ETH Zurich, Sanjay Charagulla, GlobalFoundries

![PULP-1](/assets/images/articles/risc-v-workshop-barcelona/pulp-1.jpg)

![PULP-2](/assets/images/articles/risc-v-workshop-barcelona/pulp-2.jpg)

![PULP-3](/assets/images/articles/risc-v-workshop-barcelona/pulp-3.jpg)

![PULP-4](/assets/images/articles/risc-v-workshop-barcelona/pulp-4.jpg)

![PULP-5](/assets/images/articles/risc-v-workshop-barcelona/pulp-5.jpg)

### Ariane: An Open-Source 64-bit RISC-V Applicaton Class Processor and latest Improvements, Florian Zaruba, ETH Zurich and Luca Benini, ETH Zurich

- PULP已经支持IEEE754的浮点单元了

![PULP Ariane 1](/assets/images/articles/risc-v-workshop-barcelona/pulp-ariane-0.jpg)

![PULP Ariane 2](/assets/images/articles/risc-v-workshop-barcelona/pulp-ariane.jpg)

----

编辑：CNRV编辑部

----

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/cn/80x15.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/">知识共享署名-非商业性使用-相同方式共享 3.0 中国大陆许可协议</a>进行许可。商业转载请联系作者。
