# 延长一周！由 RISC-V 国际基金会组织的暑期实习项目正在开放申请

RISC-V 国际基金会组织的 RISC-V 暑期实习项目，延长一周，感兴趣的同学可以抓紧申请：

### MLIR Convolution Vectorization

[RISC-V Mentorship: MLIR Convolution Vectorization](https://mentorship.lfx.linuxfoundation.org/project/f994928b-8998-4cd3-b66e-c576aa99c9d5)

The RISC-V Mentorship Program enables one or more 12-week internship-style projects per session, funded by RISC-V, to match mentors/project leaders together with mentees/interns . Mentees are guided through a series of milestones by one or more project mentors, with whom the mentees meet on a weekly basis.

Convolution is the core operation of deep learning models and computer vision applications. MLIR supports various convolution operations. Our project is to vectorize them for the RISC-V backend. There are several methods to implement convolution vectorization, such as optimizing nested loops, implementing vectorization algorithm, converting to GEMM, etc. This project needs to choose a vectorization method and implement a conversion pass for the convolution operations. As for the vector semantic support, MLIR has the “Vector” dialect for the general vector abstraction, and it also allows the backend-specific vector dialect, such as the “x86vector” dialect, “arm_neon” dialect, and “arm_neon” dialect. Like these dialects, the project also needs to propose an “RVV” dialect and work with existing dialects and tools.

Deliverables:
- An MLIR “RVV” Dialect. (Operations in the dialect can support the convolution vectorization)
- A conversion pass to vectorize convolution operations in “Linalg” dialect with “RVV” dialect enabled.
- A conversion pass to lower the operations in “RVV” dialect to “LLVM IR” dialect.
- Unit tests for “RVV” dialect and conversion passes.

### 给 V8 添加 RV32G 后端

[RISC-V Mentorship: Porting V8 to RISC-V R32G](https://mentorship.lfx.linuxfoundation.org/project/2021e650-c533-4671-afed-bf87c089af09)

The RISC-V Mentorship Program enables one or more 12-week internship-style projects per session, funded by RISC-V, to match mentors/project leaders together with mentees/interns . Mentees are guided through a series of milestones by one or more project mentors, with whom the mentees meet on a weekly basis.

This program pairs one mentee with an experienced mentor to deliver a V8 JavaScript engine port for a 32-bit RISC-V core.

The V8 JavaScript engine for RISCV64G has been upstreamed to Chromium recently. As a basic component for the Chromium web browser and node.js, it would enlarge RISCV’s application scenario. Although RV32G V8 port would be quite similar to RV64G V8 port , it is still in the TODO list. Porting and enable the RV32G on V8 will bring the embedded RISCV software ecosystem more applications, make RISC-V embed processors more competitive.

Deliverables (bullet list of components and the changes expected):
- Turbofan backend implementation
- Embedded simulator implementation
- Corresponding unit tests implementation
- Regression tests pass

Acceptance criteria (bullet list with measurable results defined):
- RV32G cross-compiled and simulator build on both debug and release configuration should be passed
- A helloworld demo should run successfully on both the embedded simulator and a real or emulated hardware (i.e. a real board or QEMU emulation).
- 97% of the regression test should pass

### 给 V8 的 RISC-V 后端添加 V 扩展

[RISC-V Mentorship: Adding Vector Extension to V8/RV64G port](https://mentorship.lfx.linuxfoundation.org/project/ba333574-1ce7-4fc7-9c56-901337672273)

The RISC-V Mentorship Program enables one or more 12-week internship-style projects per session, funded by RISC-V, to match mentors/project leaders together with mentees/interns . Mentees are guided through a series of milestones by one or more project mentors, with whom the mentees meet on a weekly basis.

The WebAssembly SIMD ISA is fully supported in the main-stream architecture backend in the V8 JavaScript engine. However, as the RV64G V8 has just been upstreamed and the RISC-V Vector extension is still under the final ratify, the WebAssembly SIMD support for RISC-V with Vector extension has remained to be implemented. In this work, the “liftoff” compiler for WebAssembly, the register allocation for the standalone vector register files, and the assembler of the vector instructions should be coded. Mapping the WebAssembly’s 128bit SIMD instructions to the 128bit wide RISC-V Vector instructions could greatly accelerate those data and computation intensive WebAssembly applications.

Deliverables:
- instruction selection for the RISC-V Vector instructions in the liftoff compiler
- vector register description and allocation in the Turbofan backend
- assembler and disassembler of the RISC-V Vector instructions
- implement the RISC-V Vector instructions in the embedded simulator
- corresponding unit tests implementation
- regression tests pass


### Porting Spidermonkey to RISC-V
[RISC-V Mentorship: Porting Spidermonkey to RISC-V](https://mentorship.lfx.linuxfoundation.org/project/fb9e1ba6-d6ed-40b5-82b5-ee1089ef050a)

The RISC-V Mentorship Program enables one or more 12-week internship-style projects per session, funded by RISC-V, to match mentors/project leaders together with mentees/interns . Mentees are guided through a series of milestones by one or more project mentors, with whom the mentees meet on a weekly basis.

Spidermonkey is the JavaScript Engine inside Firefox. It has JIT compilers for generating native binary codes on the fly. This project aims to porting Spidermonkey to RV64GC platform.

Basic knowledge of compilers and language virtual machines are needed.

Deliverables:
- Cross-compile Spidermonkey to RV64GC Linux (Fedora) platform.
- Patches that let Spidermonkey running on RV64GC Linux under interpreter mode.
- Porting the baseline compilers so that Spidermonkey can enable at least one JIT compiler on RV64GC platform
- Submit all patches to upstream for code review (merging into upstream is encouraged but not required)

Acceptance criteria:
- Pass the regression tests in the Spidermonkey.
- Get performance data by running SunSpider, Octane and Kraken benchmarks on the RISC-V machine (RV64GC) or software simulator (QEMU).
