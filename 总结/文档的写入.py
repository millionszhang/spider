# -*- coding: utf-8 -*-
#对excel文档的写入
import csv
out = open('lianjia.csv', 'a', newline='', encoding='utf-8')#excel 文档的名字类型
filednames = ['小区', '标题', '链接', '价格','户型','面积']  #excel文档的每个竖行的标题
csv_write = csv.writer(out, dialect='excel')
csv_write.writerow(filednames)#建议将以上代码添加到文档填写代码之上
t4="富力桃园(公寓)"
info1 = "崧泽华城秀景苑，空气清新，温馨一室，地铁沿线"
info2 = "http://sh.lianjia.com/zufang/shz4365141.html"
info3 = "2500元/月"
t5 = "1室1厅"
t6 = "距离17号线汇金路站700米"
stu1 = (t4, info1, info2, info3, t5, t6)#文档填写代码
csv_write.writerow(stu1)#内容写入

#对word文档的写入

