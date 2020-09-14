## [CH001] CNRV Chisel挑战赛: MuxN

### 题目

给定一个2:1 Mux的BlackBox和一个正整数N (N>1)，用chisel生成一个N:1的Mux。

要求：代码简洁、注释充分、电路最优、chisel的可读性好，生成的verilog可读性也要好。

奖金100元人民币，2020年9月11日周五晚上12点截止。

### 结果

**qinghai**胜出，在电路最优和生成的verilog代码基本相同的情况下，chisel代码即使没有注释依然能够读懂。[Scastie Link](https://scastie.scala-lang.org/ShBdUi08QTir9oY1M0DPuQ)

```scala
import chisel3._
import chisel3.util._
import chisel3.stage.ChiselStage

// z = s ? i1 : i0
class Mux2[T <: Data](gen: T) extends BlackBox {
  val io = IO(new Bundle {
    val i0 = Input(gen)
    val i1 = Input(gen)
    val s = Input(Bool())
    val z = Output(gen)
  })
}

object Mux2 {
  def apply[T <: Data](s: Bool, i1: T, i0: T): T = {
    val c = Module(new Mux2(chiselTypeOf(i0)))
    c.io.s := s
    c.io.i1 := i1
    c.io.i0 := i0
    c.io.z
  }
}

// r = d[s], N: d width, 1<s<N
object MuxN {
  private def iter[T <: Data](d: Vec[T], s: UInt, dw: Int): T = dw match {
    case 1 => d(0)
    case 2 => Mux2(s(0), d(1), d(0))
    case _ =>
      val sw = s.getWidth
      val half = 1 << (sw - 1)
      val sd = d.grouped(half).toSeq
      Mux2(
        s(sw - 1),
        iter(VecInit(sd(1)), s(sw - 2, 0), sd(1).size),
        iter(VecInit(sd(0)), s(sw - 2, 0), sd(0).size)
      )
  }

  def apply[T <: Data](d: Vec[T], s: UInt): T = iter(d, s, d.size)
}

```

另外，**浩哲**的代码也很简单易懂，思想是类似的。[Github Gist](https://gist.github.com/zhutmost/ed2e89a48edbbd925aff8dfd1b05a38b)

以及，**罗剑文** 的repo文档写的很细，给出了若干种实现方式: [Github Repo](https://github.com/luojw-dwr/Toy-Parallel-Mux-Generator)

----

![CNRV Chisel Challenge](/assets/images/challenge/ch-logo.png)
