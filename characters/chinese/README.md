# 中式全世代与经典古典人物卡库 (Chinese Dynasties & Classics Character Cards)

本目录（`characters/chinese/`）是专门为 **Qwen-Image 2.1 NSFW / Pose Pipeline** 打造的中式人物卡资产库。涵盖**汉代**、**唐代**、**近代民国**、**现代高级时尚与顶流**，以及**古典名著、武侠、神话小说**等各个历史与文学维度的经典人物复刻原型。

每张人物卡均经过高精度特征解构，包含独立生图测试提示词（Benchmark Prompt）、模块化主体描述词块（Modular Block，可与 `prompts/` 目录中 19 个场景任意拼装）、推荐推理与 LoRA 配置以及即开即用的执行脚本。

---

## 一、中式人物卡总览表 (Overview Table)

| 编号 | 人物名 | 英文名 | 时代/类型分类 | 影视/明星复刻原型灵感 | 风格特征与体态 | 推荐 LoRA 配置 | 推荐场景搭配 | 卡片详情 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **CN-01** | **赵凌燕** | Zhao Lingyan | **汉代宫廷** | 佟丽娅（《母仪天下》赵飞燕） | 掌上轻舞 / 楚腰纤细 / 丹凤微挑 / 汉宫凝脂仙姿 | `femaledVaginus-v1.3` @ 1.0 | 幽篁竹林水阁、汉宫暖阁、古典雕花拔步床 | [`zhao_lingyan.md`](zhao_lingyan.md) |
| **CN-02** | **杨玉瑶** | Yang Yuyao | **盛唐帝国** | 殷桃 / 范冰冰（盛唐杨贵妃） | 盛唐国色 / 丰腴润泽 / 额绘牡丹花钿 / 桃花醉目 | `femaledVaginus-v1.3` @ 1.0 / `thesealpacas` | 私汤温泉暖池、新中式茶室、牡丹金丝软榻 | [`yang_yuyao.md`](yang_yuyao.md) |
| **CN-03** | **白曼清** | Bai Manqing | **近代民国** | 张曼玉（《花样年华》）+ 汤唯（《色戒》） | 老上海名伶 / 手推波浪卷发 / 细长柳叶眉 / 旗袍沙漏曲线 | `thesealpacas-nsfw-v2` @ 0.85 (CFG 4.0) | 旗袍名媛暗光酒廊、复古旅馆、微醺镜前 | [`bai_manqing.md`](bai_manqing.md) |
| **CN-04** | **杜雯** | Du Wen | **现代高级时尚** | 刘雯 + 杜鹃（顶级东方超模） | 东方高级骨相 / 刀刻下颌线 / 极品直角肩 / 179cm 黄金九头身 | `femaledVaginus-v1.3` @ 1.0 | 顶层豪宅全景落地窗、古典画室人体、极简棚拍 | [`du_wen.md`](du_wen.md) |
| **CN-05** | **热依仙** | Reyixian | **现代明艳顶流** | 迪丽热巴（顶级浓颜神颜） | 欧亚异域明艳五官 / 挺拔驼峰琼鼻 / 大鹿眼泪痣 / 人间富贵花 | `thesealpacas-nsfw-v2` @ 0.85 / `taws` @ 0.95 | 奢华游艇日光浴、午夜厨房、全景落地窗 | [`reyixian.md`](reyixian.md) |
| **CN-06** | **林潇湘** | Lin Xiaoxiang | **古典文学名著** | 陈晓旭（87版《红楼梦》林黛玉） | 绛珠仙草 / 似蹙非蹙罥烟眉 / 似喜非喜含情目 / 弱柳扶风娇美 | `femaledVaginus-v1.3` @ 1.0 | 中式古典红木雕花拔步床、潇湘竹影、水阁亭台 | [`lin_xiaoxiang.md`](lin_xiaoxiang.md) |
| **CN-07** | **龙芷清** | Long Zhiqing | **经典武侠名著** | 刘亦菲 / 李若彤（《神雕侠侣》小龙女） | 终南出尘仙剑 / 冰肌玉骨 / 冷若霜雪 / 及臀乌发系白丝绦 | `femaledVaginus-v1.3` @ 1.0 | 江南烟雨水阁、幽篁竹林、飞檐月色 | [`long_zhiqing.md`](long_zhiqing.md) |
| **CN-08** | **苏魅儿** | Su Mei'er | **古典神话志怪** | 温碧霞 / 娜然（《封神演义》苏妲己） | 倾世九尾天狐 / 天生媚骨 / 摄魂狐眸 / 咬唇娇媚 / 水蛇蜂腰 | `thesealpacas-nsfw-v2` @ 0.85 / `taws` @ 1.0 | 古典红木雕花拔步床、私汤温泉水滑、桑拿微汗 | [`su_meier.md`](su_meier.md) |

---

## 二、使用方法与自动化合成 (How to Use)

所有人物卡均经过标准化排版，可配合根目录下的脚本进行直接查看与场景无缝混搭：

### 1. 查看单张人物卡的核心提示词块
```powershell
python scripts/compose_prompt.py --character characters/chinese/zhao_lingyan.md --show-char
```

### 2. 将指定人物快速拼装嵌入任意场景
```powershell
# 将民国名伶白曼清嵌入旗袍酒廊场景：
python scripts/compose_prompt.py `
  --character characters/chinese/bai_manqing.md `
  --scene prompts/scene_qipao_lounge.txt

# 将盛唐贵妃杨玉瑶嵌入私汤温泉场景并直接启动生成：
python scripts/compose_prompt.py `
  --character characters/chinese/yang_yuyao.md `
  --scene prompts/scene_onsen_hotspring.txt `
  --run --out outputs/chinese_yang_hotspring.png
```

### 3. 直接运行独立基准测试 (Standalone Benchmark)
每张卡片的 `## 4` 章节均包含经过调校的独立基准测试提示词，直接拷贝提示词在 WebUI、ComfyUI 或运行 `scripts/qwen_pose_test.py` 即可渲染高保真全身人像。
