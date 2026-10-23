# 中式全世代与经典古典人物卡库 (Chinese Dynasties & Classics Character Cards)

本目录（`characters/chinese/`）是专门为 **Qwen-Image 2.1 NSFW / Pose Pipeline** 打造的中式人物卡资产库。全系列采用 `CN-01` 至 `CN-18` 规范编号体系，文件名与标题全局统一编号，涵盖**先秦春秋、两汉、三国魏晋、大唐武周、两宋雅韵、晚明秦淮、近代民国、现代时尚/顶流，以及经典小说演义神怪**等全历史与文学维度的经典人物复刻原型。

每张人物卡均经过高精度特征解构，包含独立生图测试提示词（Benchmark Prompt）、模块化主体描述词块（Modular Block，可与 `prompts/` 目录中 19 个场景任意拼装）、推荐推理与 LoRA 配置以及即开即用的执行脚本。

---

## 一、中式人物卡全系总览表 (Overview Table: CN-01 ~ CN-18)

| 编号 | 人物名 | 英文名 | 时代/类型分类 | 影视/明星复刻原型灵感 | 风格特征与体态 | 推荐 LoRA 配置 | 推荐场景搭配 | 卡片详情链接 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **CN-01** | **赵凌燕** | Zhao Lingyan | **汉代宫廷** | 佟丽娅（《母仪天下》赵飞燕） | 汉代垂鬟分髾高盘髻 / 掌上轻舞 / 楚腰纤细 / 丹凤微挑 / 汉宫凝脂仙姿 | `femaledVaginus-v1.3` @ 1.0 | 幽篁竹林水阁、汉宫暖阁、拔步床 | [`cn01_zhao_lingyan.md`](cn01_zhao_lingyan.md) |
| **CN-02** | **杨玉瑶** | Yang Yuyao | **盛唐帝国** | 殷桃 / 范冰冰（盛唐杨贵妃） | 盛唐国色 / 丰腴润泽 / 额绘牡丹花钿 / 桃花醉目 / 雍容华贵 | `femaledVaginus-v1.3` @ 1.0 / `thesealpacas` | 私汤温泉暖池、新中式茶室、牡丹金丝软榻 | [`cn02_yang_yuyao.md`](cn02_yang_yuyao.md) |
| **CN-03** | **白曼清** | Bai Manqing | **近代民国** | 张曼玉（《花样年华》）+ 汤唯（《色戒》） | 老上海名伶 / 手推波浪卷发 / 细长柳叶眉 / 旗袍沙漏曲线 / 翡翠玉镯 | `thesealpacas-nsfw-v2` @ 0.85 (CFG 4.0) | 旗袍名媛暗光酒廊、复古旅馆、微醺镜前 | [`cn03_bai_manqing.md`](cn03_bai_manqing.md) |
| **CN-04** | **杜雯** | Du Wen | **现代高级时尚** | 刘雯 + 杜鹃（顶级东方超模） | 东方高级骨相 / 刀刻下颌线 / 极品直角肩 / 179cm 黄金九头身 / 极简御姐 | `femaledVaginus-v1.3` @ 1.0 | 顶层豪宅全景落地窗、古典画室人体、极简棚拍 | [`cn04_du_wen.md`](cn04_du_wen.md) |
| **CN-05** | **热依仙** | Reyixian | **现代明艳顶流** | 迪丽热巴（顶级浓颜神颜） | 欧亚异域明艳五官 / 挺拔驼峰琼鼻 / 大鹿眼泪痣 / 人间富贵花尤物 | `thesealpacas-nsfw-v2` @ 0.85 / `taws` @ 0.95 | 奢华游艇日光浴、午夜厨房、全景落地窗 | [`cn05_reyixian.md`](cn05_reyixian.md) |
| **CN-06** | **林潇湘** | Lin Xiaoxiang | **古典文学名著** | 陈晓旭（87版《红楼梦》林黛玉） | 绛珠仙草 / 似蹙非蹙罥烟眉 / 似喜非喜含情目 / 弱柳扶风娇美病态骨感 | `femaledVaginus-v1.3` @ 1.0 | 红木雕花拔步床、潇湘馆竹影、水阁亭台 | [`cn06_lin_xiaoxiang.md`](cn06_lin_xiaoxiang.md) |
| **CN-07** | **龙芷清** | Long Zhiqing | **经典武侠名著** | 刘亦菲 / 李若彤（《神雕侠侣》小龙女） | 终南出尘仙剑 / 冰肌玉骨 / 冷若霜雪 / 及臀乌发系白丝绦 / 纯白仙姿 | `femaledVaginus-v1.3` @ 1.0 | 江南烟雨水阁、幽篁竹林、飞檐月色 | [`cn07_long_zhiqing.md`](cn07_long_zhiqing.md) |
| **CN-08** | **苏魅儿** | Su Mei'er | **古典神话志怪** | 温碧霞 / 娜然（《封神演义》苏妲己） | 倾世九尾天狐 / 天生媚骨 / 摄魂狐眸 / 咬唇娇媚 / 水蛇蜂腰尤物 | `thesealpacas-nsfw-v2` @ 0.85 / `taws` @ 1.0 | 古典红木雕花拔步床、私汤温泉水滑、桑拿微汗 | [`cn08_su_meier.md`](cn08_su_meier.md) |
| **CN-09** | **施浣纱** | Shi Huansha | **春秋战国** | 蒋勤勤（《西施》第一水灵神颜） | 沉鱼落雁 / 苎萝浣纱 / 天然去雕饰 / 捧心西子微蹙 / 清纯江南白月光 | `femaledVaginus-v1.3` @ 1.0 | 江南烟雨水阁、幽篁竹林溪边、禅意茶室 | [`cn09_shi_huansha.md`](cn09_shi_huansha.md) |
| **CN-10** | **甄洛仙** | Zhen Luoxian | **三国魏晋** | 蔡少芬（《洛神》甄宓古典仙韵） | 凌波微步 / 罗袜生尘 / 魏晋凌云高髻 / 仙风玉骨 / 冰霜高洁神女 | `femaledVaginus-v1.3` @ 1.0 | 幽篁竹林水阁、荷塘月色、画室人体 | [`cn10_zhen_luoxian.md`](cn10_zhen_luoxian.md) |
| **CN-11** | **武明空** | Wu Mingkong | **大周盛唐** | 刘晓庆 / 贾静雯（一代女皇武则天） | 一代女帝 / 至尊红颜 / 凤目含威 / 九龙凤冠脱落后霸气与成熟肉感 | `femaledVaginus-v1.3` @ 1.0 / `thesealpacas` | 雕花拔步龙榻、私汤温泉、龙凤金丝暖阁 | [`cn11_wu_mingkong.md`](cn11_wu_mingkong.md) |
| **CN-12** | **李清照** | Li Qingzhao | **两宋雅韵** | 周迅（青年灵秀）+ 刘诗诗（宋风清雅） | 宋式极简美学 / 宋式白玉冠梳 / 误入藕花深处微醺少女感 / 知性文人风骨 | `femaledVaginus-v1.3` @ 1.0 | 新中式茶室、水墨书斋、江南水阁 | [`cn12_li_qingzhao.md`](cn12_li_qingzhao.md) |
| **CN-13** | **柳如诗** | Liu Rushi | **明末清初** | 万茜（电影《柳如是》绝代名妓） | 秦淮八艳之首 / 儒士巾帼与风流名伶极致反差 / 纤指抚琴 / 堕马髻 | `thesealpacas-nsfw-v2` @ 0.85 | 秦淮画舫拔步床、禅意茶室、江南水阁 | [`cn13_liu_rushi.md`](cn13_liu_rushi.md) |
| **CN-14** | **林芷萱** | Lin Zhixuan | **民国黄金年代** | 周迅（《人间四月天》林徽因） | 人间四月天 / 民国秀逸书卷气 / 纯净双麻花辫 / 清澈大杏眼 / 羊脂白玉骨感 | `thesealpacas-nsfw-v2` @ 0.8 | 古典画室写生、新中式茶室、微醺镜前 | [`cn14_lin_zhixuan.md`](cn14_lin_zhixuan.md) |
| **CN-15** | **柳天仙** | Liu Tianxian | **现代神颜顶流** | 刘亦菲（现代私服/红毯天仙攻神颜） | 东方极品驼峰玉鼻 / 鹅蛋脸 / 冷白皮牛奶发光肌 / 纯欲出尘千金感天花板 | `thesealpacas-nsfw-v2` @ 0.85 / `taws` @ 0.95 | 私汤温泉暖池、豪宅全景落地窗、赛博阳台 | [`cn15_liu_tianxian.md`](cn15_liu_tianxian.md) |
| **CN-16** | **邱曼妮** | Qiu Manni | **90s黄金港风** | 邱淑贞（《赌神2》红衣）+ 关之琳 | 港风大波浪卷发 / 烈焰红唇 / 猫系灵动圆杏眼 / 小骨架大胸蜂腰蜜桃臀尤物 | `thesealpacas-nsfw-v2` @ 0.85 | 复古汽车旅馆、暗光酒廊、深夜厨房 | [`cn16_qiu_manni.md`](cn16_qiu_manni.md) |
| **CN-17** | **姬无双** | Ji Wushuang | **仙侠修仙小说** | 张雨绮（《妖猫传》春琴）+ 白鹿仙侠 | 红衣似火 / 赤足系金铃 / 额心朱砂魔纹 / 杀伐果断又媚骨天成 / 绝色魔尊 | `femaledVaginus-v1.3` @ 1.0 | 红幔雕花拔步床、幽篁竹林水阁、月下亭台 | [`cn17_ji_wushuang.md`](cn17_ji_wushuang.md) |
| **CN-18** | **任楚楚** | Ren Chuchu | **金庸经典武侠** | 许晴（《笑傲江湖》圣姑任盈盈） | 绿竹巷抚琴圣姑 / 两腮动人甜美小梨涡 / 亦正亦邪傲娇美 / 娇羞含情目 | `femaledVaginus-v1.3` @ 1.0 | 绿竹巷幽篁水阁、新中式茶室、江南水阁 | [`cn18_ren_chuchu.md`](cn18_ren_chuchu.md) |
| **CN-19** | **苏青荷** | Su Qinghe | **新中式典雅名媛** | 江南世家冷艳名媛与茶道大师 | 及腰瀑布黑直发 / 丹凤杏眼 / 羊脂冷白皮 / 极度柔韧水蛇腰 | `femaledVaginus-v1.3` / `VNCCS` | 3D姿态精准写真、禅意茶室、古典雕花床 | [`cn19_su_qinghe.md`](cn19_su_qinghe.md) |

---

## 二、使用方法与自动化合成 (How to Use)

所有人物卡均经过标准化排版，可配合根目录下的脚本进行直接查看与场景无缝混搭：

### 1. 查看单张人物卡的核心提示词块
```powershell
python scripts/compose_prompt.py --character characters/chinese/cn01_zhao_lingyan.md --show-char
```

### 2. 将指定人物快速拼装嵌入任意场景
```powershell
# 将民国名伶白曼清嵌入旗袍酒廊场景：
python scripts/compose_prompt.py `
  --character characters/chinese/cn03_bai_manqing.md `
  --scene prompts/scene_qipao_lounge.txt

# 将盛唐贵妃杨玉瑶嵌入私汤温泉场景并直接启动生成：
python scripts/compose_prompt.py `
  --character characters/chinese/cn02_yang_yuyao.md `
  --scene prompts/scene_onsen_hotspring.txt `
  --run --out outputs/chinese_yang_hotspring.png

# 将仙侠魔女姬无双嵌入月夜竹林场景：
python scripts/compose_prompt.py `
  --character characters/chinese/cn17_ji_wushuang.md `
  --scene prompts/scene_bamboo_courtyard.txt
```

### 3. 直接运行独立基准测试 (Standalone Benchmark)
每张卡片的 `## 4` 章节均包含经过调校的独立基准测试提示词，直接拷贝提示词在 WebUI、ComfyUI 或运行 `scripts/qwen_pose_test.py` 即可渲染高保真全身人像。
