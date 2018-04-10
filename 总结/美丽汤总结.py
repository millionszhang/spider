from bs4 import BeautifulSoup

txt = """
<div class="info-panel">
						<h2><a name="selectDetail" class="js_triggerGray js_fanglist_title" gahref="results_click_order_2" key="sh4335124" target="_blank" href="/zufang/shz4335124.html" title="番禺大厦，看房有钥匙，地铁沿线，1室0厅">番禺大厦，看房有钥匙，地铁沿线，1室0厅</a>

						</h2>
						<div class="col-1">
							<div class="where">
								<a class="laisuzhou" href="/xiaoqu/5011000017244.html"><span class="nameEllipsis" title="番禺大厦">番禺大厦</span></a>&nbsp;&nbsp;
								<span>1室0厅&nbsp;&nbsp;</span>
								<span>38平&nbsp;&nbsp;</span>
							</div>
							<div class="other">
								<div class="con">
									<a href="/zufang/changning/">长宁</a>
									<a href="/zufang/xinhualu/">新华路</a>

									<span>| </span>
									低区/29层


									<span>| </span>朝南

								</div>
							</div>
							<div class="chanquan">
								<div class="left agency">
									<div class="view-label left">


										<span class="fang-subway"></span>
										<span class="fang-subway-ex"><span>距离10号线交通大学站742米</span></span>



										<span class="anytime"></span>
										<span class="anytime-ex"><span>随时看房</span></span>



									</div>
								</div>
							</div>
						</div>
						<div class="col-3">
							<div class="price">
								<span class="num">5500</span>元/月

							</div>
							<div class="price-pre">2017.11.29
							上架</div>
						</div>
						<div class="col-2">
							<div class="square"><div>
								<span class="num">7</span>人
							</div>
							<div class="col-look">看过此房</div>
						</div>
					</div>
					</div>
				</li>
"""
soup = BeautifulSoup(txt, 'lxml')
t1 = soup.find('a')  # 提取h2标签下的中文内容
c1 = t1.get('href')
c2 = t1.get('title')
t2 = soup.find('div', class_='where')  # 提取div标签下的内容
t3 = soup.find('div', class_='where').find('a')  # 提取div标签a标签的内容下的内容
t4 = t2.find_all('span')[0].text  # 提取span的内容
t5 = t2.find_all('span')[1].text
t6 = t2.find_all('span')[2].text
print(c1, c2, t3, t4, t5, t6)


