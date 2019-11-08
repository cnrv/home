Spike模拟Linux 5.3教程
===

### 相关工具版本说明

* riscv-gnu-toolchain: [7833a53](https://github.com/riscv/riscv-gnu-toolchain/tree/7833a53f8b0d0edb2bec0bb9a177685ae75570d5)

* riscv-pk: [a3e4ac6](https://github.com/riscv/riscv-pk/tree/a3e4ac61d2b1ff37a22b9193b85d3b94273e80cb)

* riscv-isa-sim: [88a8528](https://github.com/riscv/riscv-isa-sim/tree/88a852836acb4c7166b1aa4102e11354bfd99234)

* linux: [v5.3-rc4](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=d45331b00ddb179e291766617259261c112db872)

* busybox: [busybox-1.26.2](http://busybox.net/downloads/busybox-1.26.2.tar.bz2)

### 环境变量设置

```bash
$ export  TOP=/home/<user>/Riscv           // 整个环境的顶层目录
$ export  RISCV=$TOP/riscv-tools/riscv-tc  // riscv compiler编译器安装目录，可换至其他目录
$ export  PATH=$PATH:$RISCV/bin
```

建议将一下环境变量专门设置到单独的文件中，每次使用时source对应文件。
如想确定变量是否为想要的目录，可以以类似`echo $TOP`的方式查看。

### toolchain安装

按照[riscv-gnu-toolchain](https://github.com/riscv/riscv-gnu-toolchain/tree/7833a53f8b0d0edb2bec0bb9a177685ae75570d5)、[riscv-pk](https://github.com/riscv/riscv-pk/tree/a3e4ac61d2b1ff37a22b9193b85d3b94273e80cb)和[riscv-isa-sim](https://github.com/riscv/riscv-isa-sim/tree/88a852836acb4c7166b1aa4102e11354bfd99234)的步骤安装编译。

截止这一步骤，编译即可执行一个riscv程序，可以编译一个hello world 程序测试Toolchain，使用命令：spike pk hello 。

```bash
echo -e '#include <stdio.h>\n int main(void) { printf("Hello world!\\n"); return 0; }' > hello.c
riscv64-unknown-elf-gcc -o hello hello.c
spike pk hello
```

### Linux Kernel

下载至$TOP，并通过riscv64-unknown-linux-gnu-进行编译。

```bash
make -j16 ARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-gnu-
```

#### Busybox

下载至$TOP并解压：

```bash
curl -L http://busybox.net/downloads/busybox-1.26.2.tar.bz2 >busybox-1.26.2.tar.bz2
tar xvjf busybox-1.26.2.tar.bz2
```

进入busybox目录，使用`make allnoconfig`关闭所有busybox配置选项。再通过`make menuconfig`开启相关选项，包括：

```bash
CONFIG_STATIC=y, listed as “Build BusyBox as astatic binary (no shared libs)” in BusyBox Settings Build Options
CONFIG_FEATURE_INSTALLER=y, listed as“Support –install [-s] toinstall applet links at runtime” in BusyBox Settings General Configuration
CONFIG_CROSS_COMPILER_PREFIX=riscv64-unknown-linux-gnu-,listed as “Cross Compiler prefix” inBusyBox Settings  Build Options
CONFIG_INIT=y, listed as “init” in Init utilities
CONFIG_ASH=y, listed as “ash” in Shells
CONFIG_ASH_JOB_CONTROL=n, listed as “Ash → Job control” inShells
CONFIG_MOUNT=y, listed as “mount” in Linux SystemUtilities
CONFIG_FEATURE_USE_INITTAB=y, listed as “Support reading aninittab file” in Init Utilities
```

配置结束后，采用make_rootfs.sh脚本来编译busybox，构建Root Disk Image，创建initramfs。

**inittab**：

```bash
::sysinit:/bin/busybox mount -t proc proc /proc
::sysinit:/bin/busybox mount -t tmpfs tmpfs /tmp
::sysinit:/bin/busybox --install -s
/dev/console::sysinit:-/bin/ash 
```

**make_rootfs.sh**：
```bash
CDIR=$PWD
if [ -z "$BUSYBOX" ]; then BUSYBOX=$CDIR/busybox-1.26.2; fi


if [ -z "$LINUX" ]; then LINUX=$CDIR/linux; fi

if [ -d "$BUSYBOX" ] && [ -d "$LINUX" ]; then
    echo "build busybox..."
    make -j$(nproc) -C "$BUSYBOX" 2>&1 1>/dev/null
    if [ -d rootfs ]; then rm -fr rootfs; fi
    mkdir rootfs && 
    cd rootfs
    mkdir -p  bin etc dev lib proc sbin sys tmp usr usr/bin usr/lib usr/sbin
    cp "$BUSYBOX"/busybox bin/
    ln -s bin/busybox ./init
    cp $CDIR/inittab etc/inittab
    echo "\
        mknod dev/console c 5 1 && \
        find . | cpio -H newc -o > "$LINUX"/rootfs.cpio\
        " | fakeroot &&
    if [ $? -ne 0 ]; then echo "build busybox failed!"; fi
else
    echo "make sure you have both linux and busybox downloaded."
fi

```

### 配置Linux并编译

进入kernel目录，使用命令`make ARCH=riscv menuconfig`进入图形化界面，配置：
```bash
CONFIG_VT_CONSOLE=n
Initramfs source file 输入Enter键将其更改为“<riscv_linux>/rootfs.cpio”
CONFIG_HVC_RISCV_SBI=y
```

进入Linux目录，编译Kernel，生成vmlinux：
```bash
make -j4 ARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-gnu- vmlinux
```

重新进入riscv-pk目录编译，这步会将vmlinux包装至bbl中。

```bash
cd <riscv-pk>/build
rm -rf *
../configure  --prefix=$RISCV --host=riscv64-unknown-linux-gnu --with-payload=<riscv-linux>/vmlinux
make
make install
```

最后，执行`spike bbl`即可用spike模拟Linux。

### 说明
为何设置`CONFIG_VT_CONSOLE=n`的原因请参考该[链接](https://www.cnblogs.com/brucemengbm/p/6707111.html)。
