---
layout: default
---

# RISC-V软核大赛获奖者心得

RISC-V基金会官方举办的RISC-V软核大赛在RISC-V Summit上公布。

* 第一名: Charles Papond的VexRiscv: [repo: SpinalHDL/VexRiscvSoftcoreContest2018](https://github.com/SpinalHDL/VexRiscvSoftcoreContest2018)
* 第二名: Antti Lukats的Engine-V: [repo: micro-FPGA/engine-V](https://github.com/micro-FPGA/engine-V)
* 第三名: **Changyi Gu的PulseRain Reindeer: [repo: PulseRain/Reindeer](https://github.com/PulseRain/Reindeer)**
* 最佳创意: Olof Kindgren的SERV: [repo: olofk/serv](https://github.com/olofk/serv)

----

以下是大赛的榜眼*顾长怡*同学的心得和体会。

这次CPU比赛的第一名好像是个瑞士人。他是Spinal HDL 的专家。Spinal HDL我不了解，我觉得可能是和 Chisel
差不多的一类设计语言。他用Spinal HDL 设计了VexRISCV 系列的 CPU core，
https://github.com/SpinalHDL/VexRiscv ， 有的针对Performance 优化，有的针对 Area
优化。他参赛的那个作品好像应该是 Performance 最好的。获得第一，当之无愧。

第二名好像是一个德国人。用的是microcode 设计，所以设计很微小。据他自己说，他的microcode compiler
有很长的历史，从dos 时代 就用 turbo pascal 写了。之前我看到他有个simulator， 是用Delphi
写的。他参赛的那个作品好像应该是 Area 最小的。获得榜眼，当之无愧。

最佳创意奖的获得者自己都很惊讶。他用的是 bitserial 的设计 （不要问我什么叫bitserial ).
理论上应该比第二名area/assets/images/articles/pipeline_2x2.png 更小，不过好像他的时间不够，没有完成全部zephyr  的 porting, 所以他对自己获奖也很惊讶。

那个最后一名的家伙就是我，妄图是strike a balance between performance and area,
然后代替niosII-e 或者 microblaze, 这样不同的FPGA平台都可以用同样的RISC-V核，更加portable.
前面两名的代码好像都是要直接要烧在FLASH 里面。这样在不同的FPGA平台上要有不同的load 方法。我另外加了个hardware
OCD, 直接就可以从串口载入elf文件，也是为了可移植性。

目前的我的设计是 2x2 pipeline，每两个周期处理一个指令。这样也是为了让close timing
更方便一些。这样CPU就可以和rest of the circuit 运行在同一个频率上。同时我也用的 von neumann 结构，这样
对软件的要求也少一些。（第一名好像是harvard 结构）

总的感觉，我觉得这次比赛时间太紧，又要完成很多要求，比如zephyr porting 就要花不少的时间。所以很多人可能没有时间，就让我这个家伙忝列衣冠了。

下一步，我打算完善对 compress 指令的支持，如果可能，再提高一下performance. 献丑啦

![2x2 pipeline](/assets/images/articles/pipeline_2x2.png)

----

PulseRain Technology 总部位于美国加州圣地亚哥市。该公司专注于FPGA IP Core 和
嵌入式系统的设计，其创始人顾长怡先生有丰富的软硬件设计经验，并著有专著《Building Embedded Systems, Programmable Hardware》。该公司与中国与非网旗下的思得普信息科技有限公司在“小脚丫FPGA”项目上也有深入的合作。最近该公司的PulseRain Reindeer 软核在 2018 RISC-V Soft CPU 大赛中勇闯决赛并荣获季军。

![Building Embedded Systems, Programmable Hardware](/assets/images/articles/book-148421918X.jpg)

另外，上面提到著作拙作《Building Embedded Systems, Programmable Hardware》是他在2016出版的一本书，其在亚马逊的链接是[https://amzn.com/148421918X](https://www.amazon.com/Building-Embedded-Systems-Programmable-Hardware/dp/148421918X)。顾先生同时也希望这本书能在国内出版。

----

最后，特别奖获得者Olof Kindgren @OlofKindgren 在Twitter上也展示了它bitserial CPU的解码部分，你能看懂吗？

> I want to write a bit about SERV, but as that will likely never happen, I thought I could at least share how the immediates are decoded as an example of one fun part of doing bitserial and saving resources. Consider it also an open challenge to make it more optimized :)

![Olof BitSerial Decoder](/assets/images/articles/serv_bitserial.jpg)
