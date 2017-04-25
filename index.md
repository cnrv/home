---
layout: default
---

## 关于

本站点希望能够为国内的RISC-V开发者和爱好者提供便利。

----

## 资源列表


### freedom/rocket-chip/riscv-tools 完整压缩包

因为国内用户访问github比较慢，而且clone过后submodule更加慢，以下的压缩包是在clone了[freedom](https://github.com/sifive/freedom)之后，执行`git submoudle update --init --recursive`之后打包的。所以已经以submodule的形式包含了rocket-chip和riscv-tools以及下面的诸多submodules。

[百度网盘](https://pan.baidu.com/s/1jImhqdw)


```
$ tar xzvf freedom.tar.gz
$ cd freedom
$ git submodule update --init

# 如果需要更新到最新，可以执行
$ git pull origin master
```

----

## FAQ

TBD

