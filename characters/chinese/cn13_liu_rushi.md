# 人物卡：[CN-13] 柳如诗 (Liu Rushi) - 明末秦淮·绝代名妓

- **卡片编号**：`CN-13`
- **时代分类**：明末清初秦淮 (Ming-Qing Transition / Qinhuai River)
- **原型灵感**：柳如是（融合万茜电影《柳如是》巾帼风骨、儒士青衫与红尘罗衫半解风情万种神韵）
- **主打风格**：秦淮八艳之首 / 女冠儒生与绝世名伶的反差美 / 纤指抚琴 / 傲骨柔情 / 画舫风月
- **适配场景**：中式古典红木雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)、新中式茶室 (`prompts/scene_chinese_tearoom.txt`)、江南水阁临渊 (`prompts/scene_jiangnan_pavilion.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 柳如诗 (Liu Rushi) | `charismatic alluring 24-year-old late Ming courtesan-scholar named Liu Rushi` |
| **年龄 (Age)** | 24 岁 | `mature captivating 24 years old` |
| **历史渊源** | 秦淮八艳之冠，诗书画印绝伦，兼具士大夫风骨与风月名伶极致媚态 | `Qinhuai River pleasure quarters, Ming Dynasty high courtesan literati` |
| **身高体态** | 167cm，极富女性韵味的曼妙曲线，骨架清秀但肉身软玉温香，肩颈优美 | `curvaceous feminine frame, supple soft waistline, generous natural curves, elegant sloping shoulders` |
| **肤色基底** | 暖调象牙白，带有画舫水气滋养的润泽水光与极淡脂粉光晕 | `warm ivory skin with dewy moisture sheen and delicate translucent luster` |
| **气质神态** | 半是风流儒雅、半是红尘尤物；眼神清傲冷冽中透出能融化冰霜的万种风情 | `proud haughty gaze mingled with deep sensual allure, subtle mysterious half-smile` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：眼尾略向上微飞的东方内双桃花眼，长睫微敛，眼眸深邃含烟，似笑非笑。
  - *Prompt*: `sultry elongated dark brown almond-phoenix eyes with subtle smoky winged eyeliner, misty intoxicating gaze, dense curled eyelashes`
- **眉型与鼻梁**：英气中透着娇媚的斜飞青黛柳叶眉；鼻梁高挺秀雅，鼻翼小巧。
  - *Prompt*: `fine elegant willow eyebrows with a slight heroic arch, slender aristocratic straight nose bridge`
- **唇型与面颊**：熟透水蜜桃般红润微启的饱满朱唇，唇珠微翘，下颌线条利落带有一丝骨相的高傲。
  - *Prompt*: `plump naturally vermilion-red lips slightly parted in a faint alluring smile, high defined cheekbones, refined noble jawline`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：明代名伶随性半散的堕马髻，一支翠玉响铃步摇斜插发间，几缕乌黑亮泽的碎发随意搭在雪白赤裸锁骨上。
  - *Prompt*: `cascading soft jet-black hair styled in a loose Ming Dynasty lazy chignon (Duoma ji) with dangling antique emerald jade pins, strands drifting over bare chest`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：细腻如上好宣纸又带温润脂膏质感的真人体表微观毛孔，锁骨与双峰线条在画舫灯笼暖光下呈现柔和金红漫射。
  - *Prompt*: `authentic textured human skin with microscopic pores, warm lantern-lit specular sheen over collarbones and natural feminine curves, natural softness`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：极具视觉冲击力的古典曼妙身段：抚琴抚琴的纤纤玉指、盈盈一握的柔韧蜂腰、圆润丰满的臀腿轮廓。
  - *Prompt*: `sensual hourglass proportions, slender delicate musician fingers, narrow flexible waistline, rounded feminine hips, long smooth thighs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.85`（搭配 CFG 4.0，绝妙呈现明代画舫私密风情与水光皮肤） |
| **推荐 LoRA 2** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（搭配 CFG 2.5，精准刻画肉身解剖与骨骼美学） |
| **推理步数 (Steps)** | `45 - 50` | 保证堕马髻微乱发丝与秦淮烛影质感完全收敛 |
| **引导系数 (CFG)** | `4.0` (TheseAlpacas) / `2.5` (tawsLoRa) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 柔美暖色调烛影的最佳表现 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显名伶身姿与风情万种的眼神 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定傲骨妖娆五官 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证柳如诗的秦淮名伶神颜、半散堕马髻与傲骨柔情身段：

```text
A hyper-realistic full-body masterwork studio portrait of Liu Rushi, a charismatic 24-year-old late Ming Dynasty courtesan-scholar. She is completely nude, reclining languidly across a deep rosewood bench draped in dark burgundy silk against a carved timber screen. She has loose flowing raven hair half-pinned in an elegant lazy chignon with jade hairpins, elongated dark almond eyes with a smoky misty gaze, fine arched eyebrows, and plump vermilion lips parted in a knowing smile. Her frame is voluptuously slender with delicate musician hands, sharp prominent collarbones, a tiny flexible waistline, and curvaceous rounded hips. Warm glowing lantern light casts rich amber reflections across her smooth ivory skin, highlighting microscopic pores, subtle natural moisture, and soft anatomical shadows along her ribs and thighs. Masterwork, 8k resolution, Qinhuai romantic aesthetic, Hasselblad 100mm portrait photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a charismatic alluring 24-year-old late Ming courtesan-scholar named Liu Rushi with loose jet-black hair in a lazy chignon with jade pins, sultry smoky dark almond eyes, plump vermilion lips slightly parted, possessing a curvaceous hourglass frame with slender musician hands, sharp collarbones, narrow flexible waist, rounded hips, and warm ivory skin with dewy micro-pores and soft amber sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：中式古典红木雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)
将 `Liu Rushi` 模块化词块嵌入红楼画舫拔步床：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle wide shot of a charismatic alluring 24-year-old late Ming courtesan-scholar named Liu Rushi with loose jet-black hair in a lazy chignon with jade pins, sultry smoky dark almond eyes, plump vermilion lips slightly parted, possessing a curvaceous hourglass frame with slender musician hands, sharp collarbones, narrow flexible waist, rounded hips, and warm ivory skin with dewy micro-pores and soft amber sheen. She is completely nude, sitting on her knees on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing three-quarters toward the camera, her body subtly arched with one hand resting delicately on the silk bolster behind her, her knees gently spread apart. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn13_liu_rushi `
  --prompt "A hyper-realistic, low-angle wide shot of a charismatic alluring 24-year-old late Ming courtesan-scholar named Liu Rushi with loose jet-black hair in a lazy chignon with jade pins, sultry smoky dark almond eyes, plump vermilion lips slightly parted, possessing a curvaceous hourglass frame with slender musician hands, sharp collarbones, narrow flexible waist, rounded hips, and warm ivory skin with dewy micro-pores and soft amber sheen. She is completely nude, sitting on her knees on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing three-quarters toward the camera, her body subtly arched with one hand resting delicately on the silk bolster behind her, her knees gently spread apart. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture." `
  --seed 80964 `
  --steps 45 `
  --cfg 4.0 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "thesealpacas-nsfw-v2.safetensors" `
  --lora-strength 0.85 `
  --negative "blurry, deformed, bad anatomy, bad hands, plastic skin, cartoon" `
  --out outputs/characters/cn13_liu_rushi_canopy.png
```
