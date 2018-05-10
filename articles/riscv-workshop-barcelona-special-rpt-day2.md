## 2018 RISC-V巴塞罗那 Workshop特别报道 (2)

### Fast Interrupts for RISC-V, Krste Asanovic, University of California, Berkeley

 - A new task group
 - handling support for nested preempted interrupts
 - Current interrupt scheme: two kinds, 1. local interrupts, directly to one hart, determine source throu scause
 - 2 global interrupts, PLIC, inter route between cores, read of memory mapped register return source
 - vectored interrupts, 4B per interrupts (?)
 - Problem with the current interrupt scheme:
 - no preemption except by privilege mode
 - fixed priority for local interrupts but vectored
 - vectortable holds jump instruction, can onlly jump -/+ 1MiB
 - PLIC has variable priorities, but no vector
 - PLIC need two memory access to claim/complete
 - Proposals, see photo
 - Two interrupt handler interfaces, see photo, Krste, both are needed (about saving the context)
 - Inline interrupt handler, see example in photo, every register is callee saved, save as you go
 - C ABI has higher context switch cost, see photo
 - Putting that in hardware does not help much as the memory access speed is the same
 - Vector options: put function pointers in table (hardware has to fetch pointer and jump to it atomically, difficult)
 - Add new +/- 2GB offset instruction only visible to new interrupt ISA mode (SiFive)
 - Now context needs to restore mil, interrupt levels as well.
 - pack mpp/mil/mie into mcause to reduce the number of CSR
 - Other issues: see photo
 - Question: whether to publish software examples? Yes.
 - Why only one instruction in the table? save space. Many will jump to the same address. no context saving. call need 4 instructions, larger overhead.

### RISC-V DSP (P) Extension Proposal, Chuan-Hua Chang, Andes Technologies and Richard Herveille, RoaLogic BV

- P扩展，Packed-SIMD
- 2.5 billion Andes embedded SoCs
- Andes目前已经Ship超过25亿个打在Andes嵌入式核的SoC
- P is chaired by Chang, ratify packed-SIMD
- Change目前是P-ext的主席，P扩展正在等待批准阶段
- Based onAndeStar V3 DSP.
- 这个标准扩展是基于AndeSar V3的DSP指令集
- Based on generalpurpose registers. 8/16/32 data types
- 基于GPR，支持8/16/32宽度的数据类型
- GPR is more efficient than separate register. high performance generic code programming.
- 采用GPR比独立的寄存器要更加高效，支持高性能的通用程序开发
- Provide data types and istructions can be recognized by compiler
- 支持的数据类型和指令可以被编译器很好的识别
- provide instrinic functions for software developers to use the dSP instructions
- 提供对软件开发人员提供的Instrinic函数以方便其使用这些DSP指令
- Provide libraries or middlewares to suers.
- 提供相应的库和中间件
- 64-bit, use pair of registers in RV32, needed for compuilers to generate DSP instructions automatically.
- 对64-bit来说，使用一对RV32中的寄存器，需要编译器自动生成DSP指令
- Question: more about compiler support? Seems like data types is the most difficult part.
- 提问：编译器支持是怎样的？答：似乎数据类型是最难的部分

![Andes DSP P-ext](/assets/images/articles/risc-v-workshop-barcelona/andes-1.jpg)

### RISC-V ISA Cryptographic Extensions Proposal Summary, Richard Newell, Microsemi 

- ucTEE, crypto
- 介绍了ucTEE和crypto扩展的情况
- have more member than any other group
- 该组比其他组有更多的会员参与
- ucTEE, a system without MMU.
- ucTEE是一个没有MMU的系统
- now ucTEE and crypto divided into two groups.
- 目前ucTEE和crypto已经分成了两个小组
- Security standing committee
- ？？？

### Formal Assurance for RISC-V Implementatons, Daniel Zimmerman, Galois and Joseph Kiniry, Galois

- How can we assure about these definitions?
- 我们如何确保指令集定义的准确性
- need to prove two things:1. the system does what suppose to do 2. the system does not do anything else （often overlooked）
- 有两件事情需要证明：
    1. 系统做该做什么
    2. 系统不该做任何其他的（经常被忽略）
- How can we know it is RV32I?
- 怎么能确定一个处理器是RV32I兼容的呢？
- answer: formally verify it.
- 答案是形式化的验证它
- Whether it is feasible? equivalent tools only exist in Verilog/SystemVerilog
- 是否可行呢？等价证明工具通常存在于Verilog或者SystemVerilog相关的工具
- In order to do this:
- 所以为了实现这一点，需要：
    - machine readable specification, correctness and security specification of an implementation
    - 一份机器可读的标准，以及对于一个实现的正确性安全性标准(Specification)
    - a way to measure the conformance
    - 一种证明其一致性的方法
    - ways to work with summarize, understand and explore of such measurements
    - 简化、理解和探索这些测量的方法
- How can we choose? rigorous execution.ad hoc test, simulation coverage analysis, bisimulation(multiple specs and compare the behaviour),
- ??
- verification (formally reasoning), verification coverage analysis, bisimulation as well.
- ??
- security properties are different! Very difficult to prove. No consensus to prove something.
- 安全属性这部分是最难的，非常难于证明。在证明这件事上很难达成一致。
- a domain lanaguage called LANDO to specify: architecture, correnctness and security properties
- 一个领域特定语言：LANDO，用来描述架构、正确性和安全性
- Workingwith measurement, we must help engineers to understand and explore the effects of designs, and visualize it.
- 有效的度量很重要：我们必须帮助工程师去理解和了解其设计的有效性，并且将其可视化
- Changelles: accuracy of measuremenet, evolution of security metrics, addition of more commercial tools on the backends for validation, verification and measurement
- 挑战
    - 精确的衡量
    - 安全度量的发展
    - 需要商业工具在有效性证明、验证和可度量性方面的支持

### Undefned, Unspecifed, Non-deterministc, and Implementaton Defned Behavior in Veri fable Specifcatons, Cliford Wolf, Symbiotc EDA

- undefined behaviour: do not do that case. usually means the whole spec as a whole is void for some programs
- undefined values, the result is used as the output of a not specified operations
- unsepcified value
- implementation defined behaviour/value: sometimes the best choice
- specification holes for RISC-V
- promote to use implementation defined bahviour
- fully specified behaviour is more preferred

### Foundatonal HPC Systems for 2020 and Beyond, Steven Wallach, Micron Technology

- Security within micro-architecture (architecture 2.0), memory centric computing
- Summary of RV128: object-ID(64)+byte-offset(64): object-ID, unique identifier, ISA independent, time persistent
- direct mapping between RV64 to RV128
- secure micro-architecture
- encrypted memory, defnese against spectre and meltdown
- architecture 3.0? + language based security
- Mateo: BSC processor initiative
- more than 400 people doing research
- background of BSC, see photo
- european plan, see photo
- HPC needs long vector in RISC-V, limited number of control flow, hierarchical accelerating, MPI+OpenMP, accelerating for ML
- BSC is hiring, RTL/microarch, verification, FPGA design

### Keynote: European Processor Initatve & RISC-V, Mateo Valero, Barcelona Supercomputng Center

### Securing High-performance RISC-V Processors from Time Speculaton, Christopher Celio, Esperanto and Jose Renau, Esperanto

- We can still build high-performance CPUs without change the ISA
- We only need micro-architecture improvements.
- Time domain: the performanc of one domain should not affect the performance of another, but time domain is hard to define.
- High -level: no trace, able to kill the trace after speculation.
- avoid bandwidth effect.
- What should RISC-V do? Nothing. Common strategy for tagging? Common tagging architecture, information flow? tagging/capability, more related to platform spec. Right now, adding security without touching anything.

![Espertante](/assets/images/articles/risc-v-workshop-barcelona/esperante-1.jpg)

### Use of RISC-V on Pixel Visual Core, Mat Cockrell 

- Pixel visual core, google design, domain specific core, from scratch. 8 cores. A53
- Pixel Visual核是由谷歌从头自行设计的领域专用处理器（Domain Specific Core)，包含8核 A53
- multiple accelerator on the bus.
- 其总线上又多个加速器
- In the three candidates, they choose RI5CY. (Wei: Google prefer SV than Chisel for the first time publicly)
- 在众多RISC-V核中，Google选择了RI5CY（宋威：谷歌更加喜欢SystemVerilog而非Chisel）

![Google RISC-V RI5CY](/assets/images/articles/risc-v-workshop-barcelona/google-ri5cy.jpg)

### Linux-Ready RV-GC AndesCore with Architecture Extensions, Charlie Su, Andes Technologies

- Code size reduction ontop of RVC (CoDense)
- CoDense：在RVC基础上代码密度的进一步提高
- DSP/SIMD instruction to P extension
- 支持P-ext中的DSP/SIMD指令
- custom instruction
- 支持定制化指令
- non-instruction extension: CSR-based: vectored interrupt, cache management, etc.
- 非指令集扩展（基于CSR）：向量中断和缓存管理等
- N25/NX25 V5 AndesCore
    - at 28nm HPC, small: 37KG 1GHz large: 159KG 1.15GHz
    - 在TSMC 28nm HPC工艺下：小核：3.7万门 @ 1GHz, 大核：15.9万门 @ 1.15GHz
    - DiV 15 cycles for SP, 29 cycles for DP, run in background.
    - 单精度除法需要15个周期，双精度29个周期，由独立的流水线执行
    - misaligned acces is good for software, 100 cycles are needed for exception handler
    - 软件友好的非对齐数据存取，异常处理需要100个周期左右

### Processor Trace in a Holistc World, Gajinder Panesar, UltraSoC

- providing visibility of program execution is important
- 提供可视化的程序执行过程很重要
- one method of achieving this is via processor banch trace
- 一种实现的方式是记录处理器分支记录
- For cores retire N instructions, need to replicated N times
- 如果一条指令执行了N遍，那么就要复现N次
- For multiple issue cores, also replicate th esmae interface for th eissue times
- 对于多发射的核心，要复现其发射次数
- encode the output
- 输出需要被编码（压缩）
- bits per instruction, average 0.252, encode efficiency, does not include package overhead
- 每条指令需要平均0.252个bit，压缩的效率还不错（不包含打包所需的额外开销）
- standardize the format and the interface
- 格式和接口需要标准化
- Question: using branch prediction to compress the data? if decoder matches, yes. future work.
- 问：分支预测可以提高其压缩率么？答：可以

![UltraSoC 1](/assets/images/articles/risc-v-workshop-barcelona/ultrasoc-1.jpg)

![UltraSoC 2](/assets/images/articles/risc-v-workshop-barcelona/ultrasoc-2.jpg)

### RISC-V Meets 22FDX: an Open Source Ultra-low Power Microcontroller Platorm for Advanced FDSOI Technologies, Pasquale Davide Schiavone, ETH Zurich, Sanjay Charagulla, GlobalFoundries

![PULP-1](/assets/images/articles/risc-v-workshop-barcelona/pulp-1.jpg)

![PULP-2](/assets/images/articles/risc-v-workshop-barcelona/pulp-2.jpg)

![PULP-3](/assets/images/articles/risc-v-workshop-barcelona/pulp-3.jpg)

![PULP-4](/assets/images/articles/risc-v-workshop-barcelona/pulp-4.jpg)

![PULP-5](/assets/images/articles/risc-v-workshop-barcelona/pulp-5.jpg)

### Ariane: An Open-Source 64-bit RISC-V Applicaton Class Processor and latest Improvements, Florian Zaruba, ETH Zurich and Luca Benini, ETH Zurich

- They have IEEE 754

![PULP Ariane 1](/assets/images/articles/risc-v-workshop-barcelona/pulp-ariane-0.jpg)

![PULP Ariane 2](/assets/images/articles/risc-v-workshop-barcelona/pulp-ariane.jpg)

### RISC-V Support for Persistent Memory Systems, Matheus Ogleari, Western Digital

### The Hybrid Threading Processor for Sparse Data Kernels, Tony Brewer, Micron Technology

### How PULP-based Platorms are Helping Security Research, Frank Gurkaynak, ETH Zurich

### RISC-V Virtual Platorms for Early RISC-V Embedded Sofware Development Lee Moore, Imperas and Hugh O'Keefe, Ashling

### RISC-V Workshop Barcelona Conclusion, Rick O’Connor, RISC-V Foundaton

----

作者：宋威

编辑：CNRV编辑部

----

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/cn/80x15.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/cn/">知识共享署名-非商业性使用-相同方式共享 3.0 中国大陆许可协议</a>进行许可。商业转载请联系作者。

ogle
