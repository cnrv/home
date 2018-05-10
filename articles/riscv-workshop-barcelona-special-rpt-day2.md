## 2018 RISC-V巴塞罗那 Workshop特别报道 (2)

### Fast Interrupts for RISC-V, Krste Asanovic, University of California, Berkeley

Krste: Fast interrupt
A new task group
handling support for nested preempted interrupts
Current interrupt scheme: two kinds, 1. local interrupts, directly to one hart, determine source throu scause
2 global interrupts, PLIC, inter route between cores, read of memory mapped register return source
vectored interrupts, 4B per interrupts (?)
Problem with the current interrupt scheme:
no preemption except by privilege mode
fixed priority for local interrupts but vectored
vectortable holds jump instruction, can onlly jump -/+ 1MiB
PLIC has variable priorities, but no vector
PLIC need two memory access to claim/complete
Proposals, see photo
Two interrupt handler interfaces, see photo, Krste, both are needed (about saving the context)
Inline interrupt handler, see example in photo, every register is callee saved, save as you go
C ABI has higher context switch cost, see photo
Putting that in hardware does not help much as the memory access speed is the same
Vector options: put function pointers in table (hardware has to fetch pointer and jump to it atomically, difficult)
Add new +/- 2GB offset instruction only visible to new interrupt ISA mode (SiFive)
Now context needs to restore mil, interrupt levels as well.
pack mpp/mil/mie into mcause to reduce the number of CSR
Other issues: see photo
Question: whether to publish software examples? Yes.
Why only one instruction in the table? save space. Many will jump to the same address. no context saving. call need 4 instructions, larger overhead.

### RISC-V DSP (P) Extension Proposal, Chuan-Hua Chang, Andes Technologies and Richard Herveille, RoaLogic BV

Chuanhua Chang, Andes, DSP P extension proposal
2.5 billion Andes embedded SoCs
P is chaired by Chang, ratify packed-SIMD
Based on AndeStar V3 DSP.
Based on generalpurpose registers. 8/16/32 data types
GPR is more efficient than separate register. high performance generic code programming.
Provide data types and istructions can be recognized by compiler
provide instrinic functions for software developers to use the dSP instructions
Provide libraries or middlewares to suers.
64-bit, use pair of registers in RV32, needed for compuilers to generate DSP instructions automatically.
results, see photo
Question: more about compiler support? Seems like data types is the most difficult part.


DSP/SIMD instruction to P extension
custom instruction
non-instruction extension: CSR-based: vectored interrupt, cache management, etc.
N25/NX25 V5 AndesCore
at 28nm HPC, small: 37KG 1GHz large: 159KG 1.15GHz
DiV 15 cycles for SP, 29 cycles for DP, run in background.
misaligned acces is good for software, 100 cycles are needed for exception handler
conclusion remark, see photo

![Andes DSP P-ext](/assets/images/articles/risc-v-workshop-barcelona/andes-1.jpg)

### RISC-V ISA Cryptographic Extensions Proposal Summary, Richard Newell, Microsemi 

Richard Newell, Security group
ucTEE, crypto
have more member than any other group
ucTEE, a system without MMU.
now ucTEE and crypto divided into two groups.
Security standing committee

### Formal Assurance for RISC-V Implementatons, Daniel Zimmerman, Galois and Joseph Kiniry, Galois

Daniel, formal ensurance for RISC-V implementations, DARPA
How can we assure about these definitions?
need to prove two things:1. the system does what suppose to do 2. the system does not do anything else （often overlooked）
How can we know it is RV32I?
answer: formally verify it.
Whether it is feasible? equivalent tools only exist in Verilog/SystemVerilog
In order to do this:
machine readable specification, correctness and security specification of an implementation
a way to measure the conformance
ways to work with summarize, understand and explore of such measurements
How can we choose? rigorous execution.ad hoc test, simulation coverage analysis, bisimulation(multiple specs and compare the behaviour),
verification (formally reasoning), verification coverage analysis, bisimulation as well.
security properties are different! Very difficult to prove. No consensus to prove something.
a domain lanaguage called LANDO to specify: architecture, correnctness and security properties
Workingwith measurement, we must help engineers to understand and explore the effects of designs, and visualize it.
example feature, see photo.
R&D status, see photo
Changelles: accuracy of measuremenet, evolution of security metrics, addition of more commercial tools on the backends for validation, verification and measurement

### Undefned, Unspecifed, Non-deterministc, and Implementaton Defned Behavior in Veri fable Specifcatons, Cliford Wolf, Symbiotc EDA

Clifford: undefined behaviour
undefined behaviour: do not do that case. usually means the whole spec as a whole is void for some programs
undefined values, the result is used as the output of a not specified operations
unsepcified value
implementation defined behaviour/value: sometimes the best choice
specification holes for RISC-V
promote to use implementation defined bahviour
fully specified behaviour is more preferred

### Foundatonal HPC Systems for 2020 and Beyond, Steven Wallach, Micron Technology

Steven: HPC systems
Security within micro-architecture (architecture 2.0), memory centric computing
Summary of RV128: object-ID(64)+byte-offset(64): object-ID, unique identifier, ISA independent, time persistent
direct mapping between RV64 to RV128
secure micro-architecture
encrypted memory, defnese against spectre and meltdown
architecture 3.0? + language based security
Mateo: BSC processor initiative
more than 400 people doing research
background of BSC, see photo
european plan, see photo
HPC needs long vector in RISC-V, limited number of control flow, hierarchical accelerating, MPI+OpenMP, accelerating for ML
BSC is hiring, RTL/microarch, verification, FPGA design

### Keynote: European Processor Initatve & RISC-V, Mateo Valero, Barcelona Supercomputng Center

### Securing High-performance RISC-V Processors from Time Speculaton, Christopher Celio, Esperanto and Jose Renau, Esperanto

![Espertante](/assets/images/articles/risc-v-workshop-barcelona/esperante-1.jpg)

Christor Celio:
We can still build high-performance CPUs without change the ISA
We only need micro-architecture improvements.
Time domain: the performanc of one domain should not affect the performance of another, but time domain is hard to define.
High -level: no trace, able to kill the trace after speculation.
avoid bandwidth effect.
What should RISC-V do? Nothing. Common strategy for tagging? Common tagging architecture, information flow? tagging/capability, more related to platform spec. Right now, adding security without touching anything.

### Use of RISC-V on Pixel Visual Core, Mat Cockrell 

![Google RISC-V RI5CY](/assets/images/articles/risc-v-workshop-barcelona/google-ri5cy.jpg)

Matt: Pixel
Pixel visual core, google design, domain specific core, from scratch. 8 cores. A53
multiple accelerator on the bus.
In the three candidates, they choose RI5CY. (Wei: Google prefer SV than Chisel for the first time publicly)
Some analysis of the RI5CY. see photo
Errors are patched in a couple of days.
Charlie: Andes, Linux-ready RV-GC core
Code size reduction ontop of RVC (CoDense)

### Linux-Ready RV-GC AndesCore with Architecture Extensions, Charlie Su, Andes Technologies

### Processor Trace in a Holistc World, Gajinder Panesar, UltraSoC

Gajinder: UltraSoC
providing visibility of program execution is important
one method of achieving this is via processor banch trace
Definition of the branch trace, see photo
interrupts and exceptions, see photo
For cores retire N instructions, need to replicated N times
For multiple issue cores, also replicate th esmae interface for th eissue times
encode the output
Various trace control at run-time
bits per instruction, average 0.252, encode efficiency, does not include package overhead
processor trace task group
standardize the format and the interface
Question: using branch prediction to compress the data? if decoder matches, yes. future work.

![UltraSoC 1](/assets/images/articles/risc-v-workshop-barcelona/ultrasoc-1.jpg)

![UltraSoC 2](/assets/images/articles/risc-v-workshop-barcelona/ultrasoc-2.jpg)

### RISC-V Meets 22FDX: an Open Source Ultra-low Power Microcontroller Platorm for Advanced FDSOI Technologies, Pasquale Davide Schiavone, ETH Zurich, Sanjay Charagulla, GlobalFoundries

![PULP-1](/assets/images/articles/risc-v-workshop-barcelona/pulp-1.jpg)

![PULP-2](/assets/images/articles/risc-v-workshop-barcelona/pulp-2.jpg)

![PULP-3](/assets/images/articles/risc-v-workshop-barcelona/pulp-3.jpg)

![PULP-4](/assets/images/articles/risc-v-workshop-barcelona/pulp-4.jpg)

![PULP-5](/assets/images/articles/risc-v-workshop-barcelona/pulp-5.jpg)

### Ariane: An Open-Source 64-bit RISC-V Applicaton Class Processor and latest Improvements, Florian Zaruba, ETH Zurich and Luca Benini, ETH Zurich

Davide: PULP-ARIANE
See photos for the ARIANE
They have IEEE 754

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



















