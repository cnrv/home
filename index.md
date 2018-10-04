---
layout: default
---

## 关于

本站点希望能够为国内的RISC-V开发者和爱好者提供便利。

----

## RISC-V Day 2018 Shanghai 系列报道

- 2018-06-13: [Greenwaves GAP8: RISC-V + AI助力PULP打造小型自主飞行智能无人机](/articles/crazyfile-gap8)
- 2018-06-25: [为什么你要来上海参加RISC-V Day](/articles/why-come-to-join-risc-v-day-shanghai)

## 特别活动

- 2018-06-23: [RISC-V Day 2018 Shanghai学生参会资助计划（第二轮）](/articles/risc-v-day-2018-shanghai-student-sponorship-v2)
- 2018-06-09: [RISC-V Day 2018 Shanghai学生参会资助计划（第一轮）](/articles/risc-v-day-2018-shanghai-student-sponorship)

## 实时报道

- 2018-05-09: [2018 RISC-V巴塞罗那 Workshop特别报道 (1)](/articles/riscv-workshop-barcelona-special-rpt-day1)
- 2018-05-10: [2018 RISC-V巴塞罗那 Workshop特别报道 (2)](/articles/riscv-workshop-barcelona-special-rpt-day2)

## RISC-V双周简报

国内的RISC-V爱好者利用Github协作的方式，以双周简报的方式为大家带来最新的RISC-V相关咨询，同时在微信公众号和CNRV站点上发布。内容覆盖RISC-V邮件列表、行业新闻、项目进展以及各类点评。也欢迎大家关注CNRV公众号获取最新信息。

- **第0x21弹(2018-09-30): [国内RISC-V上下游企业成立产业联盟](bi-week-rpts/2018-09-30)**
- 第0x20弹(2018-09-16): [华米和嘉楠发布基于RISC-V的自研芯片](bi-week-rpts/2018-09-16)
- 第0x1f弹(2018-09-01): [一晚上写个RISC-V处理器玩玩](bi-week-rpts/2018-09-01)
- 第0x1e弹(2018-08-17): [RISC-V新创企业拟融资上亿元](bi-week-rpts/2018-08-17)
- 第0x1d弹(2018-08-03): [印度首个可运行Linux的RISC-V芯片成功流片](bi-week-rpts/2018-08-03)
- 第0x1c弹(2018-07-20): [上海发布支持RISC-V相关政策](bi-week-rpts/2018-07-20)
- 第0x1b弹(2018-07-08): [RISC-V Day Shanghai精彩回顾](bi-week-rpts/2018-07-06)
- 第0x1a弹(2018-06-22): [RISC-V Day Shanghai即将举行，纪念版T恤不容错过](bi-week-rpts/2018-06-22)
- 第0x19弹(2018-06-08): [RISC-V Day Shanghai议程公布](bi-week-rpts/2018-06-08)
- 第0x18弹(2018-05-25): [RISC-V Day Shanghai等你来玩](bi-week-rpts/2018-05-25)
- 第0x17弹(2018-05-11): [从点子到芯片？](bi-week-rpts/2018-05-11)
- 第0x16弹(2018-04-27): [RISC-V引领敏捷硬件风潮](bi-week-rpts/2018-04-27)
- 第0x15弹(2018-04-13): [第八届Workshop会议议程公布](bi-week-rpts/2018-04-13)
- 第0x14弹(2018-03-30): [宗师获图灵奖实质名归](bi-week-rpts/2018-03-30) [\[繁体\]](bi-week-rpts/2018-03-30.tc)
- 第0x13弹(2018-03-16): [想把事情做简单可不是那么简单的事情](bi-week-rpts/2018-03-16) [\[繁体\]](bi-week-rpts/2018-03-16.tc)
- 第0x12弹(2018-03-02): [看看AI和RISC-V碰撞出的火花](bi-week-rpts/2018-03-02) [\[繁体\]](bi-week-rpts/2018-03-02.tc)
- 第0x11弹(2018-02-15): [跑Linux的CPU一次来俩](bi-week-rpts/2018-02-15) [\[繁体\]](bi-week-rpts/2018-02-15.tc)
- [往期存档](biweekly-archive)

----

## 文章列表

- 2017-10-12: [RISC-V 双周简报问卷调查结果分析](articles/2017-10-12-questionaire)
- 2018-05-05: [给开源架构添点儿柴](articles/cold-boiling-water)

----

## 资源列表

- **[RISC-V 资料搜集页面](resource)**
- **[RISC-V 参考文献页面](papers)**

----

## 如何在国内快速搭建SiFive的Freedom环境

### 下载freedom/rocket-chip/riscv-tools完整压缩包

因为国内用户访问github比较慢，而且clone过后submodule更加慢，以下的压缩包是在clone了[freedom](https://github.com/sifive/freedom)之后，执行`git submoudle update --init --recursive`之后打包的。所以已经以submodule的形式包含了rocket-chip和riscv-tools以及下面的诸多submodules。

网盘中还新增了[freedom-e-sdk](https://github.com/sifive/freedom-e-sdk)和[freedom-u-sdk](https://github.com/sifive/freedom-u-sdk)的完整压缩包。

- [百度网盘freedom/rocket-chip/riscv-tools完整打包文件](https://pan.baidu.com/s/1J9N2VvfY9D6zakh8aMO5rg)
    - GitHash: [397c395](https://github.com/sifive/freedom/commit/397c395b8216c46c3d1b21484d85c6509c3ee7e8)
    - MD5Sum: 63b711236a118df48d035b65b1fa5065
    - 打包时间: 2018-Jun-11
- [百度网盘freedom-e-sdk完整打包文件](https://pan.baidu.com/s/1qYa6fd6)
    - GitHash: [fcbcd44](https://github.com/sifive/freedom-e-sdk/commit/fcbcd440a0556b90bb7f6a739ac567d5f8e93fa2)
    - MD5Sum: 1b5c97dd71918cfaa1c43fb7f38ecade
    - 打包时间: 2017-Aug-20
- [百度网盘freedom-u-sdk完整打包文件](https://pan.baidu.com/s/1i6t6UDB)
    - GitHash: [c31cf7f](https://github.com/sifive/freedom-u-sdk/commit/c31cf7f31d036742b84dd473db4b9fb18abe3c7f)
    - MD5Sum: fd8787c5853097ddb9f6dbc02dc6f781
    - 打包时间: 2018-Feb-06

下载成功之后执行：

~~~
$ tar xzvf freedom.tar.gz
$ cd freedom
$ git submodule update --init --recursive

# 如果需要更新到最新，可以执行
$ git pull origin master
~~~

### 利用国内镜像加速sbt

目前Aliyun提供了Maven的镜像可以用来加速在构建`rocket-chip`或是`freedom`过程中的`sbt`的运行。

可以在Ubuntu上的~/.sbt/repositories中加入以下内容

~~~
[repositories]
  local
  aliyun: http://maven.aliyun.com/nexus/content/groups/public/
  sbt-releases-repo: http://repo.typesafe.com/typesafe/ivy-releases/, [organization]/[module]/(scala_[scalaVersion]/)(sbt_[sbtVersion]/)[revision]/[type]s/[artifact](-[classifier]).[ext]
  sbt-plugins-repo: http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/, [organization]/[module]/(scala_[scalaVersion]/)(sbt_[sbtVersion]/)[revision]/[type]s/[artifact](-[classifier]).[ext]
  central: http://repo1.maven.org/maven2/
~~~

参考： [Scala 的构建工具 SBT 镜像设置](http://www.jianshu.com/p/c8c48b0b3866)

**以上sbt镜像功能还需要充分验证，请各位给出反馈**

### 二进制包

- [百度网盘 riscv32-unknown-gcc-6.1.0](https://pan.baidu.com/s/1kV7QJkj) *provided by 胡振波*

----

## oschina镜像服务

在提供压缩包的同时，我们在[oschina](http://git.oschina.net)上镜像了主要的RISC-V工程。 我们利用国外服务器定期同步oschina上的镜像，方便大家获得最新的更新。
相比压缩包，镜像服务器同步了更多的RISC-V相关GitHub工程，包括freechipsproject, riscv, ucb-bar和lowrisc的所有工程。
镜像服务器的具体使用方法请参考[clone-helpers](https://github.com/cnrv/clone-helpers/blob/master/README.md)工程。

----

**欢迎关注微信公众号CNRV，接收最新最时尚的RISC-V讯息！**

![CNRV微信公众号](https://cnrv.io/assets/images/cnrv_qr.png)
