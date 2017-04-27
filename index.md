---
layout: default
---

## 关于

本站点希望能够为国内的RISC-V开发者和爱好者提供便利。

----

## 最新活动

[SiFive](https://www.sifive.com/)会在6th RISC-V Workshop之后的周六下午2点（5月13日）在张江办一场线下的活动，届时SiFive的主要成员包括RISC-V的主要发明者U.C. Berkeley的Krste Asanović教授和FE310/Hifive1的主要设计者首席工程师Megan Wachs都会到场。感兴趣的朋友请及时关注本页面，正式的活动注册信息会尽快发出。

----

## 资源列表


### freedom/rocket-chip/riscv-tools完整压缩包

因为国内用户访问github比较慢，而且clone过后submodule更加慢，以下的压缩包是在clone了[freedom](https://github.com/sifive/freedom)之后，执行`git submoudle update --init --recursive`之后打包的。所以已经以submodule的形式包含了rocket-chip和riscv-tools以及下面的诸多submodules。

网盘中还新增了[freedom-e-sdk](https://github.com/sifive/freedom-e-sdk)和[freedom-u-sdk](https://github.com/sifive/freedom-u-sdk)的完整压缩包。

- [百度网盘freedom/rocket-chip/riscv-tools完整打包文件](https://pan.baidu.com/s/1eSvIPgA)
- [百度网盘freedom-e-sdk完整打包文件](https://pan.baidu.com/s/1mhGVe1U)
- [百度网盘freedom-u-sdk完整打包文件](https://pan.baidu.com/s/1nvLnaZn)

```
$ tar xzvf freedom.tar.gz
$ cd freedom
$ git submodule update --init --recursive

# 如果需要更新到最新，可以执行
$ git pull origin master
```

----

## FAQ

TBD

