# Maintainer邀请！openEuler RISC-V SIG 正在积极寻求开源软件维护者加入oE/RV社区

openEuler 是诞生于国内的一个非常年轻的 Linux 发行版，目前已经在 x86 和 Arm64 上做到了商业支持。
而在 RISC-V 架构上，目前还没有达到可以随 openEuler 22.03 发布的完善程度，并且对比 Debian、Fedora 等发行版的 RISC-V 支持，还有很大的距离需要赶超。

基于以上情况，负责 RISC-V 架构支持的 openEuler RISC-V SIG 在近期开始使用 ORSP (openEuler RISC-V SIG Proposal) 的方式开始重新组织社区力量开展工作，并借助于中国科学院软件研究所智能软件研究中心新成立的RISC-V操作系统测试团队（TARSIER团队），开始招募大量的RISC-V爱好者进行测试和修包。

但是我们很快就发现，仅仅依靠TARSIER团队的几个员工和几十个实习生是无法在一两个月内完成所有 8000+ 个软件仓库的适配和修复的。在最好的估计下，到2月底可以完成 4218 个软件包的修复和测试，仅仅占 openEuler 整个核心仓库 8368 的包数量的 50% 左右。 **更为棘手的是，由于目前 RISC-V 并不是 openEuler 的 tier-1 平台，仓库门禁没有对新提交代码进行 RISC-V 架构上的CI检查，使得每次新提交代码，都有可能破坏掉 RISC-V 平台上软件包的状态。** 这在其它流行的 Linux 发行版上也有同样的问题，但是由于 openEuler RISC-V 目前的包维护者并不多，问题尤其突出。我们可能需要 **新增加约2000名活跃的RISC-V维护者** 才能够即满足后续扩展仓库超过两万个软件包的维护又不至于太肝。

在正式成为 Tier-1 平台架构之前，需要大量的社区志愿者来帮助 openEuler RISC-V SIG 维护核心 8000+ 软件包。我代表 openEuler RISC-V SIG 向您发出邀请，希望能够一起加入到 RISC-V 软件生态建设中来，为 RISC-V 早日成为跟 x86、Arm64 并驾齐驱的三大架构贡献一点自己的力量。 **RISC-V port maintainers 将作为 openEuler 技术社区的重要组成部分，维护 RISC-V 架构下各类软件包的健康与体面，积极促进 RISC-V 适配的代码可以及时合回 openEuler 主仓库，与分管各个软件包的 SIG maintainers 保持良好的、建设性的沟通。**

成为 RISC-V port maintainer 的流程可以简单分为以下几个步骤：
1. 签署openEuler的个人或企业CLA，即可在所有仓库提交 Patch/PR/MR；
2. 寻找自己熟悉领域的软件包，或者自己感兴趣的软件包，检查其在 openEuler OBS 上的构建状态，如果是 failed、unresolvable 等状态，则可以尝试进行修复。
3. 持续关注并及时修复一个软件包8周以上即可联系 openEuler RISC-V SIG (wuwei_plct on gitee, or lazyparser on github) 要求成为 maintainer。
4. 每个软件包默认需要 2-3 名 maintainers，而一名 maintainer 可以同时维护多个包。

Maintainer 的职责：
1. 每周抽时间关注下 openEuler OBS 上 RISC-V 架构下软件包的构建状态，及时修复或吸引志愿者修复。
2. 及时回复PR，提供建设性的意见。
3. 积极促进 RISC-V 适配的代码可以及时合回 openEuler 主仓库，与分管各个软件包的 SIG maintainers 保持良好的、建设性的沟通。
4. （尽量）参加 openEuler RISC-V SIG 的双周会议或其它专题性讨论会。

如何开始？
- 所有的代码和文档都是公开的，可以从[1]开始，欢迎有问题直接提交 issues。如果不习惯 gitee，同样欢迎在 GitHub[2] 上进行提问和交流。
- 如果您愿意以实习生（需在校生）或兼职的形式加入到 openEuler RISC-V 开发中来，TARSIER团队也非常的欢迎！具体可以参考[3]中的介绍。

[1] https://gitee.com/openeuler/RISC-V
[2] https://github.com/isrc-cas/tarsier-oerv
[3] [RISC-V操作系统团队招聘测试工程师](https://mp.weixin.qq.com/s/inLFS4pI1F74m_oJ2I7xjQ)

附带 ORSP002 的内容：
see: https://gitee.com/openeuler/RISC-V/blob/master/proposal/ORSP002.md

# ORSP002 建立 openEuler RISC-V maintainer community

## Meta info

提议者：吴伟

时间：2022-02-24

## 背景 / Background

目前 openEuler RISC-V 还不是 openEuler 社区官方支持的架构，并且还没有形成一个可以给普通用户每日测试使用的成熟度。openEuler 社区各个仓库 maintainers 的响应时间不同、对 RISC-V 的了解程度、支持程度不同，更重要的是目前 RISC-V 生态中的软件支持需要部分临时绕过或临时修复patch，使得回合周期非常长，长到可能会影响到 openEuler RISC-V 的修包速度。通过对其它发行版（debian、fedora）等的观测，都是需要先作为一个 side project / ports 来进行修包和维护，从效率角度出发，先建立一个完整可测试的基本系统。再花长短不一的时间合回发行版的主线。

## 问题 / Issues

1. 目前 openEuler RISC-V 修包速度远远超过 openEuler 社区 review 速度。过去3个月尝试直接将 RISC-V 的 patch 合回 openEuler 主线，但是如背景中所言，以及赶上2203发版，很快就意识到实际操作上变得不可行。
2. openEuler 目前没有 RISC-V 门禁，任何仓库的新的提交都有可能 break 掉 RISC-V 架构。需要有人长期维护。src-oe 就包含了超过8000个仓库，需要一个更大的维护团队和测试团队。

## 提议 / Proposal

1. 逐步建立 repo watcher 角色，本质上属于 RISC-V 架构上的 shadow maintainer。
2. 每个 repo / pkg 设定1-3个 maintainer、1-3个 tester，确保所有的包都得到最低程度的关爱。
3. maintainer/tester 在2022H1由 openEuler RISC-V SIG 成员（张旭舟、席静、王俊强、吕晓倩、吴伟）确定。2022H2开始考虑在SIG下成立更加社区化的一个 RISC-V (shadow) maintainer (steering) committee (RMC) 进行维护者和测试者的增补和替换。
4. 参考 debian 和 fedora 等发行版的管理，将仓库/包进行分组。例如 Rust 语言、Python 语言、Nodejs/npm 都自然形成了不同的组。
5. 相关权责信息在 gitee/openEuler/RISC-V 仓库中进行维护。
6. RMC 的日常会议在2022H1随 openEuler RISC-V SIG 双周会进行

## 时间线 / Timeline

2022Q1: 完成目前正在修复和完成修复的包的维护者选择和机制/流程创建（吴伟）。

2022Q2: 完成所有4k+包的维护者组织，将支持/修复范围对标到 openEuler 所有软件包。

2022Q3: 完成对 openEuler 所有代码仓库的 RISC-V shadow maintain，主动 CI 监测。

## 资源 / Resources

- openEuler RISC-V SIG 负责方向及路线规划、与 openEuler 各 SIG 进行沟通协调。
- 中国科学院软件研究所 Tarsier 团队投入不少于 600 人月及必要的硬件资源。
