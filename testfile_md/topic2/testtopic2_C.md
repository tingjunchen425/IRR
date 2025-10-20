CRISPR基因編輯技術在罕見疾病治療的最新進展

1. 主要基因編輯技術原理

CRISPR/Cas9 系統是目前最常用的基因編輯工具，由向導RNA (sgRNA) 精準匹配目標DNA序列，並由Cas9核酸

酶在該位置產生雙股斷裂（DSB），使細胞啟動修復機制而實現基因修正

1

2

。最新衍生技術包括碱基編輯

(base editing) 和引導式編輯  (prime editing)。碱基編輯利用被改造為失活或單鏈切割的Cas9 結合去氨基酶，

使DNA中單個鹼基直接轉換，例如細胞色素碱基編輯器 (CBE) 可將C→T，腺嘌呤碱基編輯器 (ABE) 可將A→G，

而不產生雙鏈斷裂

3

4

。引導式編輯則在Cas9 nickase 基礎上融合反轉錄酶，通過特製的pegRNA引入各類

單鹼基替換、小片段插入或缺失突變，可修改所有12種鹼基轉換和小片段變化

3

5

。與傳統CRISPR/Cas9

相比，碱基編輯和引導式編輯因不需製造DSB而降低細胞毒性與脫靶風險，同時可實現更精確的點突變修正

3

。

2. 罕見疾病的臨床試驗案例

近年已有多項CRISPR 基因編輯用於罕見遺傳病的臨床試驗：

-

 遺傳性失明（LCA第10型）：Editas的EDIT-101療法針對CEP290基因突變治療Leber先天性黑蒙症。在

BRILLIANCE臨床試驗中，對14例患者單眼注射後，有79%受試者視力出現可量化的改善，且無嚴重毒副作用報

告

6

7

。這是首個證實體內CRISPR治療可改善視力的罕見病例。

-  罕見代謝病（CPS1缺乏症）：費城兒童醫院與賓大團隊開發了定製化CRISPR基因編輯療法。2025年2月，一

名嬰兒（KJ）接受此肝細胞定向的碱基編輯治療 。治療後數月觀察顯示，患者病情穩定、生長良好，能正

8

常增加蛋白質攝入，且對常見兒科感染的氨血症反應減少 。這一案例標誌著首例將個體化CRISPR療法應用

9

於單一罕見病例，並證明技術在臨床安全可行

8

9

。

-  肝臟遺傳病（α1-抗胰蛋白酶缺乏）：Beam   Therapeutics的BEAM-302是一種體內腺苷酸脫氨酶型碱基編輯

療法，用於矯正α1-抗胰蛋白酶基因Z-突變（AATD）。2025年3月發佈的1/2期數據顯示，BEAM-302實現了首

例臨床上的致病突變矯正，患者血清AAT水平增加，證明碱基編輯可在人體內長期表達治療蛋白 。該療法已

10

獲FDA罕見病快速通道認定。

- 免疫缺陷病（慢性肉芽腫症, CGD）：多個平台正在開發CRISPR治療CGD。Ensoma公司開發的EN-374為體內

定向造血幹細胞療法，已獲FDA核准I/II期臨床試驗，用於治療CYBB基因突變造成的X-聯鎖CGD

11

12

。

Prime   Medicine的PM359為體外提取HSC再編輯療法，矯正最常見的p47^phox(CGD)缺陷基因。首例患者接受

單劑療法後，15天和30天時中性粒細胞NADPH氧化酶活性分別恢復至58%和66%，遠超過估計的臨床受益閾值

20%；治療耐受性良好，未報告與PM359相關的嚴重不良事件

13

14

。 

此外，儘管鐮狀細胞貧血和β地中海貧血並非罕見病，2023年底首個CRISPR療法Casgevy已獲FDA批准用於這

兩種血紅蛋白病 ，證明了CRISPR技術的臨床可行性。上開例證明CRISPR編輯技術在多種單基因罕見病中已

2

進入臨床試驗階段，儘管大多處於Ⅰ/Ⅱ期，已有初步安全和療效成果被報告。

3. 臨床應用的安全性議題

CRISPR基因編輯的安全性是臨床應用的關鍵挑戰。脫靶效應指CRISPR/Cas9在與目標序列類似的基因位點意外

切割，引發非預期變異，可能導致功能紊亂或致癌風險。文獻指出，早期Cas9常呈現≥50%的脫靶頻率 。

15

為降低此風險，研發了各種高保真Cas9變體（如SpCas9-HF1、HiFiCas9）和Cas9   nickase（僅割單股）等，

可大幅減少非目標切割而保持編輯效率 。同時，設計更佳的sgRNA和算法也可優化特異性。碱基編輯器理

16

論上不產生DSB，但研究顯示CBE可能產生一定數量的非目標單核苷酸突變（OT   SNVs），而ABE的脫靶率較低

4

。因此，編輯前後需利用高通量基因組測序嚴密檢測潛在脫靶。 

1

免疫反應也是重要考量。人體普遍對常用Cas9來源菌株（如鏈球菌SpCas9、葡萄球菌SaCas9）存在既有免疫

應答 ；編輯時引入這些外源蛋白可能被免疫系統識別，引發排斥或炎症。目前尋找免疫“冷門”Cas9亞型

17

（如CjCas9）和使用非病毒遞送系統等方式可部分避免此問題 。此外，基因編輯的遞送方法本身也可能引

17

發免疫反應：2023年報告一例CRISPR治療的死亡病例中，使用AAV6載體遞送編輯組分造成患者肺部急性呼吸

窘迫綜合症（ARDS）而亡，病理解釋為嚴重的先天免疫炎症反應 。這警示載體安全性不可忽視，臨床試驗

18

中必須謹慎監控免疫指標。 

長期效應目前尚不明朗。由於臨床數據多為短期觀察，尚需多年跟蹤才能了解基因編輯對患者健康及後代的真

正影響。研究者強調，尤其若未來發展到生殖系應用，可能須跨越數代才能觀察潛在的副作用 。因此，臨

19

床試驗設計常包含長期追踪計畫，以評估如腫瘤風險、染色體結構變異或其它意外基因效應的延遲後果。

4. 社會與倫理討論：生殖系編輯對未來世代的影響

基因編輯可作用於體細胞或生殖細胞/早期胚胎，如左圖所示（體細胞編輯不傳給下一代），右圖示生殖系編輯

（在配子或胚胎內修改基因，可遺傳） 。生殖系基因編輯一旦應用在人體受精卵或配子上，基因變更將傳

19

到所有後代，對整個家系及人類族群帶來不可逆的影響，引發重大倫理爭議

19

20

。學界廣泛共識認為，目前

生殖系編輯技術還不安全，臨床應用尚早。例如ASGCT等機構指出，生殖系基因治療可能導致多代未知風險，

患者本人及其後代的潛在損益在世代跨度內難以全面評估 。具體風險包括：編輯可能不完全而產生馬賽克

19

現象（部分細胞未被編輯），導致遺傳病可能依然出現；或者脫靶效應如果發生在胚胎階段，將遍及多個器官

系統，難以糾正

20

21

。

倫理上，批評者擔心，若允許生殖系編輯，可能開啟「優生學」的潘朵拉盒：父母或社會可能用基因編輯去除

（或增強）特定基因，對健康、殘疾或特質作選擇，從而擴展「正常」與「病患」的定義，引發歧視和社會不

平等 。支持者則認為，對攜帶嚴重遺傳病基因的家庭而言，生殖系編輯可能避免疾病傳承，但這需要嚴格

22

規範和多方監督。目前多國（美國、歐盟成員國、中國、日本等）明文禁止基於生殖目的的人類胚胎基因編輯

23

19

。總之，專家一致主張，除非科技極度成熟且符合公眾價值觀，否則應禁止或暫緩臨床應用，並進行廣

泛的社會對話與倫理審議

23

22

。

5. 各國法規政策現狀與差異

各地對CRISPR基因編輯的法規重點不盡相同：

-  美國：聯邦法律禁止使用政府資金進行人類生殖系基因治療研究 。FDA負責監管臨床試驗申請，所有基因

24

編輯療法（包括體細胞）須經其批准才能進入臨床。目前美國已批准CASGEVY等CRISPR體細胞基因療法（治療

鐮狀細胞病和地中海貧血），但對人類胚胎的生殖系編輯臨床應用嚴格限制

24

25

。NIH政策亦明文不資助任

何胚胎基因編輯研究。

-

 中國：早在2003年《人類輔助生殖技術規範》中即禁止為妊娠目的對配子或胚胎進行基因操作 。賀建奎

26

2018年的實驗事件後，中國政府加強監管，《刑法修正案(十一)》(2021年)明確將植入基因編輯胚胎列為犯罪行
為。此外，科技部等部門陸續發布多項指導原則和規範（約十餘部法律法規），確保嚴格禁止未經批准的臨床

人胚編輯

26

27

。體細胞基因編輯（例如對癌症、血液病人的治療）則在審批下可進行臨床研究。

-  歐盟：歐盟於2014年通過的《臨床試驗法規》禁止任何基因治療臨床試驗對人類產生可遺傳的基因改變 。

28

歐盟成員國大多遵循《歐洲人權與生物醫學公約》（Oviedo公約，1997年），該公約禁止任何意圖引發後代基

因改變的療法 。因此歐盟基本上禁止以治療為目的的人體胚胎基因編輯臨床研究，但學術性的體外研究在

29

嚴格監管下仍有空間進行。

- 日本：日本規範相對寬鬆。2018年草案指南允許對人胚胎在體外進行基因編輯研究（需經文科省審批及機構倫

理委員會通過），但嚴禁將編輯過的胚胎用於妊娠生育 。違規行為並未被刑法直接處罰，但研究單位需承

30

擔學術與社會責任。目前日本尚未有專門法律針對基因編輯，主要依賴上述行政指南和既有倫理監管。 

2

各國政策顯示：對體細胞基因編輯普遍持支持或謹慎推動態度，致力於以臨床試驗和監管框架保障患者安全；

而對生殖系基因編輯則採取高度謹慎或禁令態度，強調倫理界線與長期社會影響。未來國際間亦在討論統一標

準，例如WHO呼籲加強跨國治理、各國學者呼籲國際協調等，以平衡科技發展與社會價值

31

25

。

參考資料： 本報告資料來源於最新科學期刊、官方新聞及科學機構發布，其中包括自然、NEJM、NIH、ASGCT

等權威報導

1

6

13

15

17

19

29

。上述數據與分析反映截至2025年的研究與政策進展。 

1

What is CRISPR/Cas9? - PMC 

https://pmc.ncbi.nlm.nih.gov/articles/PMC4975809/

2

8

9

World's First Patient Treated with Personalized CRISPR Gene Editing Therapy at Children’s

Hospital of Philadelphia | Children's Hospital of Philadelphia

https://www.chop.edu/news/worlds-first-patient-treated-personalized-crispr-gene-editing-therapy-childrens-hospital

3

CRISPR-Cas9 DNA Base-Editing and Prime-Editing - PubMed

https://pubmed.ncbi.nlm.nih.gov/32872311/

4

5

15

16

17

CRISPR Gene Therapy: Applications, Limitations, and Implications for the Future - PMC

https://pmc.ncbi.nlm.nih.gov/articles/PMC7427626/

6

7

Participants of pioneering CRISPR gene editing trial see vision improve | National Eye Institute

https://www.nei.nih.gov/about/news-and-events/news/participants-pioneering-crispr-gene-editing-trial-see-vision-improve

10

11

12

News: The Latest Clinical Trial Updates from CRISPR Medicine News - CRISPR Medicine

https://crisprmedicinenews.com/news/the-latest-clinical-trial-updates-from-crispr-medicine-news/

13

14

News: First-Ever Prime-Editing Therapy Shows Safety and Efficacy in Patient With Chronic

Granulomatous Disease - CRISPR Medicine

https://crisprmedicinenews.com/news/first-ever-prime-editing-therapy-shows-safety-and-efficacy-in-patient-with-chronic-

granulomatous-dis/

18

CRISPR Clinical Trials: A 2024 Update - Innovative Genomics Institute (IGI)

https://innovativegenomics.org/news/crispr-clinical-trials-2024/

19

20

21

23

Ethical Issues: Germline Gene Editing | ASGCT - American Society of Gene & Cell Therapy |

https://patienteducation.asgct.org/patient-journey/ethical-issues-germline-gene-editing

22

28

29

European Union: Germline / Embryonic - Global Gene Editing Regulation Tracker

https://crispr-gene-editing-regs-tracker.geneticliteracyproject.org/eu-germline-embryonic/

24

25

United States: Germline / Embryonic - Global Gene Editing Regulation Tracker

https://crispr-gene-editing-regs-tracker.geneticliteracyproject.org/united-states-embryonic-germline-gene-editing/

26

27

At genome editing summit, experts say China rules fall short | STAT

https://www.statnews.com/2023/03/06/genome-editing-summit-experts-worry-rule-changes-in-china-fall-short/

30

Japan: Germline / Embryonic - Global Gene Editing Regulation Tracker

https://crispr-gene-editing-regs-tracker.geneticliteracyproject.org/japan-germline-embryonic/

31

Health Ethics & Governance 

https://www.who.int/teams/health-ethics-governance/emerging-technologies/human-genome-editing

3

