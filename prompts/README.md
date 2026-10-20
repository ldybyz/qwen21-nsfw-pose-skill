# Prompts 提示词与场景说明文档

本目录包含了用于 **Qwen-Image 2.1 NSFW / Pose Pipeline**（Route ① T2I）的场景提示词与配套参数配置。

每个场景均由一对文件组成：
- `*.txt`：高密度英文提示词（遵循 7 段式解构：视角、主体、分肢姿态、光影场景、皮肤质感、关键解剖、画质后缀；部分包含 `[negative]` 区域）。
- `*.params.json`：推荐的推理步数（Steps）、CFG、采样器（Sampler/Scheduler）、分辨率、推荐 LoRA 及其权重。

---

## 一、场景总览表

| 场景编号 | 场景分类 | 场景名称 | 提示词文件 (`.txt`) | 参数配置文件 (`.params.json`) | 姿态梯级 | 推荐 LoRA | 推荐参数速查 |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **01** | **作者基准** | **奢华淋浴间三人** | [`taws_v13_shower.txt`](taws_v13_shower.txt) | [`taws_v13_shower.params.json`](taws_v13_shower.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 50 steps, CFG 2.5, er_sde/beta |
| **02** | **作者基准** | **SPA俯卧按摩** | [`taws_v13_massage.txt`](taws_v13_massage.txt) | [`taws_v13_massage.params.json`](taws_v13_massage.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 30 steps, CFG 2.5, er_sde/beta |
| **03** | **作者基准** | **卧室床单私密自拍** | [`thesealpacas_v2_selfie.txt`](thesealpacas_v2_selfie.txt) | [`thesealpacas_v2_selfie.params.json`](thesealpacas_v2_selfie.params.json) | L2/L3 | `thesealpacas-nsfw-v2` @ 0.8 | 50 steps, CFG 4.0, 含负面词 |
| **04** | **现代多元** | **私汤温泉·石阶半浸** | [`scene_onsen_hotspring.txt`](scene_onsen_hotspring.txt) | [`scene_onsen_hotspring.params.json`](scene_onsen_hotspring.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 50 steps, CFG 2.5, er_sde/beta |
| **05** | **现代多元** | **落地窗晨曦·猫式跪趴伸展** | [`scene_penthouse_stretch.txt`](scene_penthouse_stretch.txt) | [`scene_penthouse_stretch.params.json`](scene_penthouse_stretch.params.json) | L2 | `femaledVaginus-v1.3` / `posture-v3` | 40 steps, CFG 2.5, er_sde/beta |
| **06** | **现代多元** | **潮汐礁石·落日暮光** | [`scene_sunset_beach_rock.txt`](scene_sunset_beach_rock.txt) | [`scene_sunset_beach_rock.params.json`](scene_sunset_beach_rock.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 50 steps, CFG 2.5, er_sde/beta |
| **07** | **现代多元** | **镜前私密·拍立得胶片风** | [`scene_mirror_selfie.txt`](scene_mirror_selfie.txt) | [`scene_mirror_selfie.params.json`](scene_mirror_selfie.params.json) | L2/L3 | `thesealpacas-nsfw-v2` @ 0.8 | 45 steps, CFG 4.0, 含负面词 |
| **08** | **现代多元** | **普拉提塑形·瑜伽垫开腿拉伸** | [`scene_pilates_stretch.txt`](scene_pilates_stretch.txt) | [`scene_pilates_stretch.params.json`](scene_pilates_stretch.params.json) | L2/L3 | `posture-v3` @ 0.85 / `femaledVaginus` | 40 steps, CFG 2.5, er_sde/beta |
| **09** | **现代多元** | **赛博霓虹·雨夜阳台** | [`scene_cyber_balcony.txt`](scene_cyber_balcony.txt) | [`scene_cyber_balcony.params.json`](scene_cyber_balcony.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 50 steps, CFG 2.5, er_sde/beta |
| **10** | **现代多元** | **复古旅馆·暗红皮革沙发** | [`scene_vintage_motel.txt`](scene_vintage_motel.txt) | [`scene_vintage_motel.params.json`](scene_vintage_motel.params.json) | L2 | `thesealpacas-nsfw-v2` @ 0.8 | 45 steps, CFG 4.0, 含负面词 |
| **11** | **现代多元** | **奢华游艇·地中海日光浴** | [`scene_yacht_sunbathing.txt`](scene_yacht_sunbathing.txt) | [`scene_yacht_sunbathing.params.json`](scene_yacht_sunbathing.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 50 steps, CFG 2.5, er_sde/beta |
| **12** | **现代多元** | **古典画室·天窗自然光模特** | [`scene_art_studio.txt`](scene_art_studio.txt) | [`scene_art_studio.params.json`](scene_art_studio.params.json) | L1/L2 | `nsfw-posture-v3` @ 0.85 | 45 steps, CFG 2.5, er_sde/beta |
| **13** | **现代多元** | **深夜厨房·冰箱冷光偷食** | [`scene_midnight_kitchen.txt`](scene_midnight_kitchen.txt) | [`scene_midnight_kitchen.params.json`](scene_midnight_kitchen.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 45 steps, CFG 2.5, er_sde/beta |
| **14** | **现代多元** | **芬兰桑拿·原木蒸汽汗蒸** | [`scene_sauna_steam.txt`](scene_sauna_steam.txt) | [`scene_sauna_steam.params.json`](scene_sauna_steam.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 45 steps, CFG 2.5, er_sde/beta |
| **15** | **中式美学** | **新中式茶室·屏风茶烟** | [`scene_chinese_tearoom.txt`](scene_chinese_tearoom.txt) | [`scene_chinese_tearoom.params.json`](scene_chinese_tearoom.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 45 steps, CFG 2.5, er_sde/beta |
| **16** | **中式美学** | **古典闺房·雕花拔步床** | [`scene_chinese_canopy_bed.txt`](scene_chinese_canopy_bed.txt) | [`scene_chinese_canopy_bed.params.json`](scene_chinese_canopy_bed.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 50 steps, CFG 2.5, er_sde/beta |
| **17** | **中式美学** | **烟雨江南·水阁美人靠** | [`scene_jiangnan_pavilion.txt`](scene_jiangnan_pavilion.txt) | [`scene_jiangnan_pavilion.params.json`](scene_jiangnan_pavilion.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 45 steps, CFG 2.5, er_sde/beta |
| **18** | **中式美学** | **民国风华·丝绸旗袍微解** | [`scene_qipao_lounge.txt`](scene_qipao_lounge.txt) | [`scene_qipao_lounge.params.json`](scene_qipao_lounge.params.json) | L2/L3 | `thesealpacas-nsfw-v2` @ 0.8 | 45 steps, CFG 4.0, 含负面词 |
| **19** | **中式美学** | **竹林庭院·汉白玉莲池** | [`scene_bamboo_courtyard.txt`](scene_bamboo_courtyard.txt) | [`scene_bamboo_courtyard.params.json`](scene_bamboo_courtyard.params.json) | L2 | `femaledVaginus-v1.3` @ 1.0 | 50 steps, CFG 2.5, er_sde/beta |

---

## 二、场景详细说明与使用规范

### 1. 作者基准用例 (Author Cases)

#### 01. 奢华淋浴间三人 (`taws_v13_shower`)
- **使用文件**：[`taws_v13_shower.txt`](taws_v13_shower.txt) + [`taws_v13_shower.params.json`](taws_v13_shower.params.json)
- **场景特征**：玻璃淋浴房、三人同框（红发/脏辫棕发/白金金发）、水流直下、高光精油与肥皂泡沫堆叠。
- **构图与视角**：极低仰角，自然站立微开腿。
- **推荐场景**：验证管道完整性、复现 Civitai 原作者公布的第一基准。

#### 02. SPA俯卧按摩 (`taws_v13_massage`)
- **使用文件**：[`taws_v13_massage.txt`](taws_v13_massage.txt) + [`taws_v13_massage.params.json`](taws_v13_massage.params.json)
- **场景特征**：柔和微暗的暖调 SPA 房、俯卧在按摩床上、双足在前、背部曲线向景深延伸、全身精油高光反光。
- **构图与视角**：脚底延伸视角的超低贴地后仰角。
- **推荐场景**：快速出图测试（30步快速收敛，无需50步即可成型）。

#### 03. 卧室床单私密自拍 (`thesealpacas_v2_selfie`)
- **使用文件**：[`thesealpacas_v2_selfie.txt`](thesealpacas_v2_selfie.txt) + [`thesealpacas_v2_selfie.params.json`](thesealpacas_v2_selfie.params.json)
- **场景特征**：白床单、床头暖光台灯、前置摄像头噪点颗粒质感、生活化私密自拍（含有 `[negative]` 负面段落）。
- **构图与视角**：仰卧俯拍大特写。
- **注意**：该 LoRA（TheseAlpacas）需搭配稍高 CFG（4.0）并传入负面词以防伪影。

---

### 2. 现代与多元场景 (Modern & Diverse Scenes)

#### 04. 私汤温泉·石阶半浸 (`scene_onsen_hotspring`)
- **使用文件**：[`scene_onsen_hotspring.txt`](scene_onsen_hotspring.txt) + [`scene_onsen_hotspring.params.json`](scene_onsen_hotspring.params.json)
- **场景特征**：户外私人温泉、暮色黄昏、雪松木与竹林背景、火山石阶、微热泉水水汽、水光倒影与鹅皮颗粒感。
- **构图与视角**：紧贴水面的低视角微仰拍，双膝微开跪坐，双手后撑。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

#### 05. 落地窗晨曦·猫式跪趴伸展 (`scene_penthouse_stretch`)
- **使用文件**：[`scene_penthouse_stretch.txt`](scene_penthouse_stretch.txt) + [`scene_penthouse_stretch.params.json`](scene_penthouse_stretch.params.json)
- **场景特征**：高层顶层公寓、落地窗白纱帘、清晨金色侧逆光（轮廓光/微透光）、厚灰地毯、腰脊曲线伸展。
- **构图与视角**：斜后方中低视角，跪趴挺胯拱背（猫牛式伸展），手臂前伸。
- **推荐 LoRA**：`femaledVaginus-v1.3` 或 `nsfw-posture-v3.safetensors`。

#### 06. 潮汐礁石·落日暮光 (`scene_sunset_beach_rock`)
- **使用文件**：[`scene_sunset_beach_rock.txt`](scene_sunset_beach_rock.txt) + [`scene_sunset_beach_rock.params.json`](scene_sunset_beach_rock.params.json)
- **场景特征**：偏远海滩海蚀礁石、落日余晖（洋红与琥珀色晚霞）、退潮浪沫、湿润沙砾颗粒贴附皮肤。
- **构图与视角**：贴近湿沙地面的低仰拍，单腿弯曲踩沙、单腿放松舒展斜倚。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

#### 07. 镜前私密·拍立得胶片风 (`scene_mirror_selfie`)
- **使用文件**：[`scene_mirror_selfie.txt`](scene_mirror_selfie.txt) + [`scene_mirror_selfie.params.json`](scene_mirror_selfie.params.json)
- **场景特征**：独立步入式衣帽间、全长全身镜、顶置射灯投射阴影、手机遮面俯角、轻微妊娠纹/皮肤真实瑕疵、真实噪点。
- **构图与视角**：镜前低蹲大开膝、双手持机俯拍镜中反射。
- **推荐 LoRA**：`thesealpacas-nsfw-v2.safetensors` @ 0.8（配负面词与 CFG 4.0）。

#### 08. 普拉提塑形·瑜伽垫开腿拉伸 (`scene_pilates_stretch`)
- **使用文件**：[`scene_pilates_stretch.txt`](scene_pilates_stretch.txt) + [`scene_pilates_stretch.params.json`](scene_pilates_stretch.params.json)
- **场景特征**：极简木地板瑜伽馆、工业风磨砂大窗柔和漫射光、深色瑜伽垫、运动后细密汗珠光泽与紧致肌肉线条。
- **构图与视角**：脚跟之间的超低地面广角，仰卧大开腿抓踝（快乐婴儿式/蝴蝶式拉伸）。
- **推荐 LoRA**：`nsfw-posture-v3.safetensors`（突出姿态张力）或 `femaledVaginus-v1.3`。

#### 09. 赛博霓虹·雨夜阳台 (`scene_cyber_balcony`)
- **使用文件**：[`scene_cyber_balcony.txt`](scene_cyber_balcony.txt) + [`scene_cyber_balcony.params.json`](scene_cyber_balcony.params.json)
- **场景特征**：高层摩天大楼雨夜露台、青色与品红双色霓虹反光、地面积水倒影、雨丝水汽薄雾、远景都市摩天楼虚焦。
- **构图与视角**：贴地超低视角仰拍，赤身倚靠玻璃栏杆，单腿微屈，霓虹双色边缘轮廓光。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

#### 10. 复古旅馆·暗红皮革沙发 (`scene_vintage_motel`)
- **使用文件**：[`scene_vintage_motel.txt`](scene_vintage_motel.txt) + [`scene_vintage_motel.params.json`](scene_vintage_motel.params.json)
- **场景特征**：70年代复古公路旅馆、深红老式皮革沙发光泽与折痕、百叶窗透入的暗红霓虹余晖、35毫米复古胶片颗粒。
- **构图与视角**：沙发座垫水平低机位，仰卧横跨沙发，双腿大开搭在扶手与椅背上。
- **推荐 LoRA**：`thesealpacas-nsfw-v2.safetensors` @ 0.8（配负面词与 CFG 4.0）。

#### 11. 奢华游艇·地中海日光浴 (`scene_yacht_sunbathing`)
- **使用文件**：[`scene_yacht_sunbathing.txt`](scene_yacht_sunbathing.txt) + [`scene_yacht_sunbathing.params.json`](scene_yacht_sunbathing.params.json)
- **场景特征**：地中海蔚蓝碧海、豪华游艇柚木甲板、正午强烈直射硬阳光感、全身厚涂防晒油镜面反光。
- **构图与视角**：顺着甲板视线的低角度仰视，条纹沙滩巾上平躺单膝抬起，单手遮阳。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

#### 12. 古典画室·天窗自然光人体模特 (`scene_art_studio`)
- **使用文件**：[`scene_art_studio.txt`](scene_art_studio.txt) + [`scene_art_studio.params.json`](scene_art_studio.params.json)
- **场景特征**：古典画家阁楼画室、倾斜大面积工业采光天窗、柔和古典明暗对比（Chiaroscuro）、木质画架与石膏像雕塑散落。
- **构图与视角**：低视角仰望，坐在老旧木圆凳上，单脚踩横撑、单膝高提贴胸抱胫的古典雕塑坐姿。
- **推荐 LoRA**：`nsfw-posture-v3.safetensors` @ 0.85 或 `femaledVaginus-v1.3`。

#### 13. 深夜厨房·冰箱冷光偷食 (`scene_midnight_kitchen`)
- **使用文件**：[`scene_midnight_kitchen.txt`](scene_midnight_kitchen.txt) + [`scene_midnight_kitchen.params.json`](scene_midnight_kitchen.params.json)
- **场景特征**：凌晨两点全黑现代公寓、仅开启的冰箱透出强冷白LED光束、极强明暗对比（Chiaroscuro）、地面深色石板反光。
- **构图与视角**：地面极低仰拍，赤足微蹲探身入冰箱拿取水瓶，冷光勾勒右侧身材与臀腿曲线。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

#### 14. 芬兰桑拿·原木蒸汽汗蒸 (`scene_sauna_steam`)
- **使用文件**：[`scene_sauna_steam.txt`](scene_sauna_steam.txt) + [`scene_sauna_steam.params.json`](scene_sauna_steam.params.json)
- **场景特征**：传统芬兰雪松木桑拿房、暖黄板下暗藏暖光灯、热石腾起白雾蒸汽、全身暴汗流淌、皮肤潮红温润。
- **构图与视角**：中低角度仰拍，第二层木凳坐姿，双手后撑，双膝大开自然放松。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

---

### 3. 东方美学与中式女性场景 (Oriental & Chinese Aesthetic)

#### 15. 新中式茶室·屏风茶烟 (`scene_chinese_tearoom`)
- **使用文件**：[`scene_chinese_tearoom.txt`](scene_chinese_tearoom.txt) + [`scene_chinese_tearoom.params.json`](scene_chinese_tearoom.params.json)
- **场景特征**：禅意极简茶室、半透宣纸木格屏风、紫砂茶台与升腾茶雾、乌黑直发与羊脂白玉肤质反衬。
- **构图与视角**：榻榻米地面低视角仰拍，双膝微开跪坐，一手扶木案，一手搭在大腿，屏风透光轮廓。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

#### 16. 古典闺房·雕花拔步床 (`scene_chinese_canopy_bed`)
- **使用文件**：[`scene_chinese_canopy_bed.txt`](scene_chinese_canopy_bed.txt) + [`scene_chinese_canopy_bed.params.json`](scene_chinese_canopy_bed.params.json)
- **场景特征**：明清雕花红木拔步大床、大红真丝缎褥与绣花缎枕、薄红纱幔轻挑、铜香炉袅袅轻烟。
- **构图与视角**：床垫边缘水平低角度仰拍，斜倚红缎枕，单手挑纱幔，双腿自然敞开舒展。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

#### 17. 烟雨江南·水阁美人靠 (`scene_jiangnan_pavilion`)
- **使用文件**：[`scene_jiangnan_pavilion.txt`](scene_jiangnan_pavilion.txt) + [`scene_jiangnan_pavilion.params.json`](scene_jiangnan_pavilion.params.json)
- **场景特征**：水乡临河木雕花窗、飞来椅（美人靠）坐栏、窗外青瓦白墙与江南细雨、潮湿水汽与青黛色调、翡翠发簪。
- **构图与视角**：跨坐倚靠美人靠，单腿垂下单膝提抱，回眸望向窗外水巷，低仰角捕捉背臀与腿部线条。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

#### 18. 民国风华·丝绸旗袍微解 (`scene_qipao_lounge`)
- **使用文件**：[`scene_qipao_lounge.txt`](scene_qipao_lounge.txt) + [`scene_qipao_lounge.params.json`](scene_qipao_lounge.params.json)
- **场景特征**：1930年代老上海老洋房、暗绿丝绒贵妃榻、翠绿真丝金线刺绣旗袍侧边扣全解推开、老留声机与复古手摇发浪。
- **构图与视角**：地毯高度低机位，斜躺在贵妃榻，腿部微开搭在丝绒软垫，真丝与白皙肌肤强烈质感反差。
- **推荐 LoRA**：`thesealpacas-nsfw-v2.safetensors` @ 0.8（配负面词与 CFG 4.0）。

#### 19. 竹林庭院·汉白玉莲池 (`scene_bamboo_courtyard`)
- **使用文件**：[`scene_bamboo_courtyard.txt`](scene_bamboo_courtyard.txt) + [`scene_bamboo_courtyard.params.json`](scene_bamboo_courtyard.params.json)
- **场景特征**：清幽竹林庭院、汉白玉雕花莲花水池、清澈水面漂浮粉色荷花瓣、晨光穿透竹叶的有机斑驳光影。
- **构图与视角**：贴近水面极低仰角，跪伏向前探看池水，黑长湿发垂落入水，竹影光斑洒落在后背与微张双腿间。
- **推荐 LoRA**：`qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` @ 1.0。

---

## 三、快速运行命令示例

### 1. 标准中式场景运行（如古典拔步床场景）

```bash
python scripts/qwen_pose_test.py \
  --mode t2i \
  --name scene_chinese_bed \
  --prompt "$(cat prompts/scene_chinese_canopy_bed.txt)" \
  --seed 80964 \
  --steps 50 \
  --cfg 2.5 \
  --sampler er_sde \
  --scheduler beta \
  --width 1152 \
  --height 1728 \
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" \
  --lora-strength 1.0 \
  --out outputs/scene_chinese_bed.png
```

### 2. 带负面词的民国旗袍场景（PowerShell 拆分执行）

```powershell
$content = Get-Content prompts/scene_qipao_lounge.txt -Raw
$parts = $content -split '\[negative\]'
$positive = $parts[0].Trim()
$negative = $parts[1].Trim()

python scripts/qwen_pose_test.py `
  --mode t2i `
  --name scene_qipao_lounge `
  --prompt "$positive" `
  --negative "$negative" `
  --seed 124880844757561 `
  --steps 45 `
  --cfg 4.0 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "thesealpacas-nsfw-v2.safetensors" `
  --lora-strength 0.8 `
  --out outputs/scene_qipao_lounge.png
```
