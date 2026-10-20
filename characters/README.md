# Characters 人物卡系统指南与分类目录

本目录是 **Qwen-Image 2.1 NSFW / Pose Pipeline** 的标准化人物卡（Character Cards）资产库。

人物卡旨在解决 AI 出图过程中“面部漂移”、“人设不稳定”、“难以跨场景迁移”等痛点。每张人物卡均采用结构化 Markdown 规范，包含**核心设定**、**外貌细节解构**、**独立生图提示词**、**模块化主体提示词块（可无缝嵌入 `prompts/` 中的 19 个场景）**、**推荐推理与 LoRA 参数**以及**实战运行命令**。

---

## 一、人物卡总览表

### 1. 中式全世代与经典古典系 (Chinese Dynasties & Classics) - 目录：[`chinese/`](chinese/)

> 详见专属目录索引：[`characters/chinese/README.md`](chinese/README.md)

| 编号 | 人物中文名 | 英文代号 | 时代/类型分类 | 原型灵感复刻 | 发型发质与容貌体态 | 推荐 LoRA | 推荐场景搭配 | 卡片链接 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **CN-01** | **赵凌燕** | Zhao Lingyan | **汉代宫廷** | 佟丽娅（《母仪天下》赵飞燕） | 汉代垂鬟分髾高盘髻 / 掌上轻舞 / 楚腰纤细 / 丹凤眼 | `femaledVaginus-v1.3` @ 1.0 | 幽篁竹林水阁、汉宫暖阁、拔步床 | [`zhao_lingyan.md`](chinese/zhao_lingyan.md) |
| **CN-02** | **杨玉瑶** | Yang Yuyao | **盛唐帝国** | 殷桃 / 范冰冰（盛唐杨贵妃） | 唐代高耸巍峨高髻 / 额绘金红牡丹花钿 / 丰腴润泽沙漏曲线 | `femaledVaginus-v1.3` @ 1.0 | 私汤温泉暖池、新中式茶室、金丝软榻 | [`yang_yuyao.md`](chinese/yang_yuyao.md) |
| **CN-03** | **白曼清** | Bai Manqing | **近代民国** | 张曼玉（《花样年华》）+ 汤唯（《色戒》） | 30年代海派手推波浪卷 / 细眉红唇 / 旗袍衣架子S曲线 | `thesealpacas-nsfw-v2` @ 0.85 | 旗袍暗光酒廊、复古旅馆、镜前自拍 | [`bai_manqing.md`](chinese/bai_manqing.md) |
| **CN-04** | **杜雯** | Du Wen | **现代高级时尚** | 刘雯 + 杜鹃（顶级东方超模） | 齐肩极简刀切黑直发 / 骨相高级 / 刀刻下颌线 / 直角肩九头身 | `femaledVaginus-v1.3` @ 1.0 | 顶层豪宅落地窗、画室人体、极简棚拍 | [`du_wen.md`](chinese/du_wen.md) |
| **CN-05** | **热依仙** | Reyixian | **现代明艳顶流** | 迪丽热巴（顶级浓颜神颜） | 丰盈海藻黑长卷发 / 欧亚异域明艳大五官 / 驼峰琼鼻 / 腰臀比尤物 | `thesealpacas-nsfw-v2` @ 0.85 | 奢华游艇日光浴、午夜厨房、全景落地窗 | [`reyixian.md`](chinese/reyixian.md) |
| **CN-06** | **林潇湘** | Lin Xiaoxiang | **古典文学名著** | 陈晓旭（87版《红楼梦》林黛玉） | 凌虚流云半绾髻饰白玉簪 / 罥烟眉含情目 / 弱柳扶风娇美病态骨感 | `femaledVaginus-v1.3` @ 1.0 | 红木雕花拔步床、潇湘馆竹影、水阁 | [`lin_xiaoxiang.md`](chinese/lin_xiaoxiang.md) |
| **CN-07** | **龙芷清** | Long Zhiqing | **经典武侠名著** | 刘亦菲 / 李若彤（小龙女神仙姐姐） | 及臀乌发系纯白丝绦 / 不食人间烟火 / 冰肌玉骨 / 冷若霜雪 | `femaledVaginus-v1.3` @ 1.0 | 江南烟雨水阁、幽篁竹林、飞檐月色 | [`long_zhiqing.md`](chinese/long_zhiqing.md) |
| **CN-08** | **苏魅儿** | Su Mei'er | **古典神话志怪** | 温碧霞 / 娜然（《封神演义》苏妲己） | 慵懒披散海藻波浪卷 / 摄魂狐眸微挑 / 咬唇娇媚 / 水蛇蜂腰 | `thesealpacas-nsfw-v2` @ 0.85 | 古典红木雕花拔步床、私汤温泉、桑拿微汗 | [`su_meier.md`](chinese/su_meier.md) |

---

### 2. 东亚泛系 (East Asian) - 目录：[`east_asian/`](east_asian/)

| 编号 | 人物中文名 | 英文代号 | 人设立绘风格 | 年龄/体型 | 发型与发色 | 推荐 LoRA | 推荐场景搭配 | 卡片链接 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **EA-01** | **林语婷** | Lin Yuting | 汉风古韵 / 江南温婉雅致 | 23岁 / 纤细柔美 / 骨肉亭匀 | 及腰直亮乌黑长发 | `femaledVaginus-v1.3` @ 1.0 | 新中式茶室、古典闺房、水阁 | [`lin_yuting.md`](east_asian/lin_yuting.md) |
| **EA-02** | **陈悦** | Chen Yue | 都市超模 / 清冷高级御姐 | 26岁 / 175cm 细高挑高骨相 | 侧分利落齐肩黑短发 | `thesealpacas-nsfw-v2` @ 0.8 | 落地窗晨曦、镜前自拍、深夜厨房 | [`chen_yue.md`](east_asian/chen_yue.md) |
| **EA-03** | **加藤樱** | Sakura Kato | 日系透明感 / 元气纯欲少女 | 20岁 / 娇小玲珑 / 蜜桃曲线 | 微卷亚麻栗棕中长发 | `femaledVaginus-v1.3` @ 1.0 | 私汤温泉、复古旅馆、日系榻榻米 | [`sakura_kato.md`](east_asian/sakura_kato.md) |
| **EA-04** | **裴智友** | Bae Ji-woo | 韩系轻熟 / 财阀名媛风情 | 25岁 / S型曼妙身材 / 水光美肌 | 蓬松海藻微卷黑曜长发 | `femaledVaginus-v1.3` / `thesealpacas` | 奢华游艇、赛博阳台、普拉提馆 | [`bae_jiwoo.md`](east_asian/bae_jiwoo.md) |

---

### 3. 欧美与高加索系 (Caucasian) - 目录：[`caucasian/`](caucasian/)

| 编号 | 人物中文名 | 英文代号 | 人设立绘风格 | 年龄/体型 | 发型与发色 | 推荐 LoRA | 推荐场景搭配 | 卡片链接 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **CA-01** | **芙蕾雅·林德** | Freya Lind | 北欧精灵 / 极光白金仙气 | 24岁 / 178cm 挺拔雕塑线条 | 极光白金如瀑波浪长发 | `femaledVaginus-v1.3` @ 1.0 | 芬兰桑拿、潮汐礁石、画室人体 | [`freya_lind.md`](caucasian/freya_lind.md) |
| **CA-02** | **艾琳娜·沃尔科娃** | Elena Volkova | 斯拉夫冷艳 / 锋利高级轮廓 | 23岁 / 紧致修长腹肌线条 | 浅灰亚麻金直发披肩 | `femaledVaginus-v1.3` @ 1.0 | 落地窗伸展、古典画室、奢华淋浴 | [`elena_volkova.md`](caucasian/elena_volkova.md) |
| **CA-03** | **克洛伊·洛朗** | Chloé Laurent | 法式复古 / 慵懒知性浪漫 | 25岁 / 自然微曲线 / 优雅松弛 | 慵懒蓬松榛果暖棕微卷发 | `thesealpacas-nsfw-v2` @ 0.8 | 复古旅馆、卧室私密自拍、镜前胶片 | [`chloe_laurent.md`](caucasian/chloe_laurent.md) |
| **CA-04** | **阿莱西亚·罗曼诺** | Alessia Romano | 地中海风情 / 阳光沙漏丰满 | 26岁 / 极具张力的火辣曲线 | 浓密深棕大波浪侧分长发 | `thesealpacas` / `femaledVaginus` | 奢华游艇、落日礁石、SPA按摩 | [`alessia_romano.md`](caucasian/alessia_romano.md) |

---

## 二、人物卡的核心结构规范

每份人物卡均严格包含以下 **6 大核心板块**：

1. **核心档案设定 (Core Profile)**：包含中文名、英文名、编号、年龄、身高、体型分类、肤色基底与人物气质标签。
2. **视觉特征解构 (Visual Breakdown)**：
   - 面部五官与眼神神态（眼睛颜色、眼型、鼻梁、唇部形态、情绪特征）
   - 发型发质与颜色（发长、质感、光泽、垂坠度）
   - 肤质纹理与微观高光（微毛孔、漫反射、锁骨与体表光影）
   - 身材比例与解剖特征（肩颈线、腰臀比、腹部与肢体紧实度）
3. **推荐推理参数与 LoRA 适配表 (Inference & LoRAs)**：标注步数、CFG、尺寸、Seed、采样器和最适配的 NSFW LoRA 权重。
4. **独立基准测试提示词 (Standalone Benchmark Prompt)**：可直接执行的独立 Portrait / Full-body 提示词，用于直接测试人物面部和身体一致性。
5. **模块化主体提示词块 (Modular Insertion Block)**：已剔除背景和视角词的纯人物描述块，可**无缝替换** `prompts/` 目录下任意场景的主体描述。
6. **场景拼装与实战运行示例 (Scene Blending)**：演示如何与 `prompts/scene_*.txt` 中的背景光影和姿态做“人物+场景”合成，并提供一键执行命令。

---

## 三、如何将人物卡与场景提示词 (`prompts/`) 拼装

在 `prompts/` 目录中，场景提示词均遵循 **7 段式解构**：
```
[1. 视角与镜头] + [2. 主体与人设] + [3. 肢体姿态与手势] + [4. 环境空间与光影] + [5. 皮肤与微观反光] + [6. 解剖学细节] + [7. 画质与摄影后缀]
```

### 快速替换三步法：

1. 打开目标场景提示词（例如 [`prompts/scene_chinese_tearoom.txt`](../prompts/scene_chinese_tearoom.txt)）。
2. 将其中的 **主体描述段落** 替换为该人物卡中的 **模块化主体描述词块 (Modular Block)**。
3. 检查并保留原场景的**视角**、**姿态**和**环境光影**，即刻完成定制化生图！

也可以使用本仓库自带的合成辅助脚本：
```bash
python scripts/compose_prompt.py \
  --character characters/east_asian/lin_yuting.md \
  --scene prompts/scene_chinese_tearoom.txt \
  --out outputs/yuting_tearoom.png
```

---

## 四、自定义扩展新人物

若需添加新的人物卡，可直接复制 [`characters/TEMPLATE.md`](TEMPLATE.md)，按照结构填写即可快速扩充新的人种与角色库。
