## Greenwaves GAP8: RISC-V + AI助力PULP打造小型自主飞行智能无人机

> 新型微处理器助力研究员打造世界最小自主飞行无人机，AI神经网络仅需不到100毫瓦

![Crazyfile 2.0](/assets/images/articles/risc-v-day-shanghai/crazyfile-2.jpg)

来自苏黎世联邦理工及意大利博洛尼大学的工程师表示，他们已经制造出世界上最小的自主式无人机 - 可依靠小型电池执行AI算法。这将极大推动超小型自主导航无人机（4英寸或更小）的发展，有朝一日将搭载环境传感器，及微型摄像机执行安全监测，探查及检查任务。

电池问题一直困扰并制约着着无人机的发展。“如何降低无人机自重，减少无人机电力需求则是我们研究并完善的方向与成果”，PULP实验室研究员表示。如上个月发表的[论文](https://arxiv.org/abs/1805.01831)中所述，他们在一款售价为180美金的超小型四翼无人机[Crazyflie 2.0](https://www.bitcraze.io/crazyflie-2/) 上装配了一款超低功耗摄像头和[GAP8微处理器](https://greenwaves-technologies.com)，并植入了定制的神经网络算法。这些扩展，只为无人机增加了5g的重量，以及1%的额外功耗（94毫瓦）。研究人员表示，电池问题依旧是一个非常大的挑战，如果能够实现30分钟的自主飞行，这将足以支持无人机进行一个中型仓库的检查工作并自主返回充电站。尽管存在很大的差距，但至少增加自主性对电池寿命的影响微乎其微。

PULP团队选择来自[法国GreenWaves Technologies公司的GAP8应用处理器](https://greenwaves-technologies.com)作为无人机的大脑，一款新颖的基于PULP项目的超低功耗并行计算平台。该处理器配备有8+1个基于RISC-V的内核，以及一个高效率的神经网络加速引擎（Hardware Convolutional Engine)。GAP8的主要任务是接收图像，并运行其AI算法DroNet，一个轻量级残差卷积神经网络（CNN）架构。通过该算法预测转向角度和碰撞概率，以实现四旋翼飞行器在各种室内和室外环境中的安全自主飞行。

![GAP8](/assets/images/articles/risc-v-day-shanghai/gap8.png)

该DroNet算法的突破之处在于成功将一个用于大型无人机的轻量级神经卷积算法，在不过多损失精度的同时，压缩并移植入一个更小的处理器。虽然这一压缩将网络处理摄像机图像的能力从每秒20帧降低到12帧，但网络仍然运行快速和准确，足以识别一个障碍，并在不到半秒钟提醒无人机。 “这对于以每秒四米飞行的Crazyflie 2.0无人机已经足够快”Loquercio写道。

在无人机可以飞行之前，团队必须在真实环境中定制，并训练他们的DroNet。他们将在汽车，自行车以及一名徒步旅行者身上安装摄像头拍摄视频。之后由一台功能强大的电脑对这些数据进行学习，并产生可植入GAP8中的模型代码。“任何人都可以使用我们发布的源代码，并重复我们的测试以验证结果”Loquercio写道。

现阶段，DroNet仅能通过左右移动来绕过面前的障碍，而并不具备上下移动的能力，而之后的新版本将克服这一难关。

这项研究表明，复杂的人工智能算法不仅限于大型计算设备，嵌入式超低功耗微处理器也可以胜任这一工作。研究人员表示，他们的突破将不仅适用于无人机，还可适用于其他机器人，以及各种配备有环境传感器，摄像头，及各种传感器的物联网小型移动设备。

Greenwaves将会参加2018年6月30日在上海举办的RISC-V Day Shanghai研讨会，有兴趣的朋友可以来和他们的工程师一起聊聊！

![Greenwaves Agenda RISC-V Day Shanghai Session](/assets/images/articles/risc-v-day-shanghai/greenwaves-session.png)

Links:
- 快公司报道: [This tiny drone with a tiny brain is smart enough to fly itself](https://www.fastcompany.com/40575392/this-tiny-drone-with-a-tiny-brain-is-smart-enough-to-fly-itself)
- 论文: Ultra Low Power Deep-Learning-powered Autonomous Nano Drones, url: [https://arxiv.org/abs/1805.01831](https://arxiv.org/abs/1805.01831)
- [GreenWaves Technologies网站](https://greenwaves-technologies.com) 

编译整理：张垚

责编：雄飞

图片来源：Greenwaves公司和论文

----

<a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/2.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/">知识共享署名-相同方式共享 2.0 通用许可协议</a>进行许可。
