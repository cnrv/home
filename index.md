---
layout: default
---

## 关于

本站点希望能够为国内的RISC-V开发者和爱好者提供便利。

----

## RISC-V双周简报

- 2017-08-17: [感觉RV就要引爆了！小编手已断!](bi-week-rpts/2017-08-17)
- 2017-08-03: [光有Chisel还不够，又来一个SpinalHDL，Scala我真心看不懂啊！](bi-week-rpts/2017-08-03)
- 2017-07-20: [进主线这事儿能走后门吗?](bi-week-rpts/2017-07-20)
- 2017-07-06: [ARM~ARM~你不要怕~](bi-week-rpts/2017-07-06)
- 2017-06-21: [你们心心念念的RV32E终于来了~](bi-week-rpts/2017-06-21)

----

## 资源列表

### [RISC-V 资料搜集页面](resource.md)

### freedom/rocket-chip/riscv-tools完整压缩包

因为国内用户访问github比较慢，而且clone过后submodule更加慢，以下的压缩包是在clone了[freedom](https://github.com/sifive/freedom)之后，执行`git submoudle update --init --recursive`之后打包的。所以已经以submodule的形式包含了rocket-chip和riscv-tools以及下面的诸多submodules。

网盘中还新增了[freedom-e-sdk](https://github.com/sifive/freedom-e-sdk)和[freedom-u-sdk](https://github.com/sifive/freedom-u-sdk)的完整压缩包。

- [百度网盘freedom/rocket-chip/riscv-tools完整打包文件](https://pan.baidu.com/s/1eSvIPgA)
- [百度网盘freedom-e-sdk完整打包文件](https://pan.baidu.com/s/1mhGVe1U)
- [百度网盘freedom-u-sdk完整打包文件](https://pan.baidu.com/s/1nvLnaZn)

~~~
$ tar xzvf freedom.tar.gz
$ cd freedom
$ git submodule update --init --recursive

# 如果需要更新到最新，可以执行
$ git pull origin master
~~~

### oschina镜像服务

在提供压缩包的同时，我们在[oschina](http://git.oschina.net)上镜像了主要的RISC-V工程。 我们利用国外服务器定期同步oschina上的镜像，方便大家获得最新的更新。
相比压缩包，镜像服务器同步了更多的RISC-V相关GitHub工程，包括freechipsproject, riscv, ucb-bar和lowrisc的所有工程。
镜像服务器的具体使用方法请参考[clone-helpers](https://github.com/cnrv/clone-helpers/blob/master/README.md)工程。

