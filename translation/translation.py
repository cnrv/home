#-*- coding: UTF-8 -*- 
import uniout
import codecs
import collections
import sys



with codecs.open(sys.argv[1],encoding='utf-8') as f:
	with codecs.open(sys.argv[2],"w",encoding='utf-8') as g:
		content=f.read()

		replace_dic={ u'緩存':u' cache ', u'操作':u' operation ', u'直接':u' explicit ', u'內核':u' kernel ', u'預取':u' prefetch ', u'翻譯':u' translation ', u'芯片':u'晶片',u'進程':u' process ', u'分支預測器':u' branch predictor ', u'比特':u'bit', u'哈希表':u' hash table ', u'斷點':u' breakpoint ', u'調試器':u' debugger ', u'內核空間':u' kernel space ', u'頁表':u' page table ',u'亂序流水線':u' OoO ', u'原子':u' atomic ', u'訪問':u' access ', u'地址':u' address ', u'非對齊':u' unaligned ', u'基址':u' base address ', u'總線':u'bus ', u'用戶態':u' U mode', u'系統態':u' S mode',u'西部數據':u'WD',u'西部資料':u'WD', u'巴塞羅那':u'Barcelona' , u'超算中心': u'BSC-CNS(Barcelona Supercomputing Center', u'數據':u'資料', u'采':u'採', u'福布斯':u'Forbes', u'官文':u'官方新聞', u'工作組':'workgroup',u'內存訪問':u'memory access' , u'關系':u'關係',u'擴展':u'extension', u'安全':u'Security', u'仿真': u'Simulation',u'物理設計':u'physical design',u'內存模型':u'memory model',u'體系結構':u'Architecture' ,u'葉子節點':u'leaf node ',u'標志位':u'flag', u'硬件控制':u'HW control',u'內存頁表':u'page table ', u'硬件':u'硬體',u'軟件':u'軟體', u'模塊':u'module ',u'帶寬':'bandwidth', u'項':'entry', u'軟件緩存':u'software cache '}
		for i in replace_dic:
			print i
			print replace_dic[i]
			content=content.replace(i, replace_dic[i])
		g.write(content)

