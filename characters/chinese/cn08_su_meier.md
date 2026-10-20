# 人物卡：[CN-08] 苏魅儿 (Su Mei'er) - 封神倾世·九尾天狐

- **卡片编号**：`CN-08`
- **时代分类**：古典神话志怪 (Classic Chinese Mythology / Investiture of the Gods)
- **原型灵感**：苏妲己（融合温碧霞经典版与娜然电影版《封神》九尾狐天生媚骨、野性纯欲兼备的倾国妖姬神韵）
- **主打风格**：天生媚骨 / 摄魂狐眸 / 娇媚慵懒 / 极致沙漏肉感 / 祸国殃民的性感压迫力
- **适配场景**：中式古典雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)、私汤温泉水滑凝脂 (`prompts/scene_onsen_hotspring.txt`)、桑拿浴室蒸腾微汗 (`prompts/scene_sauna_steam.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 苏魅儿 (Su Mei'er) | `breathtaking seductive 22-year-old nine-tailed fox enchantress named Su Mei'er` |
| **年龄 (Age)** | 外表 22 岁 | `perpetual allure 22 years old` |
| **神话渊源** | 出自《封神演义》千年九尾雪狐转世，艳绝诸夏，一笑倾城，再笑倾国 | `mythological ancient Chinese fox spirit demoness, legendary Daji archetype` |
| **身高体态** | 168cm，极度曼妙惹火的软玉温香体态：水蛇细腰、饱满圆润双峰、极致挺翘蜜桃臀 | `sensuous supple hourglass frame, narrow snake-like waistline, full voluptuous bosom, rounded alluring hips` |
| **肤色基底** | 如羊脂白雪般晶莹滑腻，在烛光下透出微红血色与天然魅惑光泽 | `luminous warm alabaster skin, glowing flush of sensual warmth and delicate translucency` |
| **气质神态** | 天生媚骨入骨三分，眼波如丝勾魂摄魄，似笑非笑间带有危险而致命的诱惑力 | `intoxicating seductive fox-gaze, dangerous sultry charm, languid bedroom eyes, irresistible feminine magnetism` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：极致勾魂的狐狸媚眼，内眦尖锐、眼尾大幅向上微飞，眼周晕染着极淡的天然绯红，眸底闪烁着摄人心魄的金褐色流光。
  - *Prompt*: `captivating upturned fox-shaped dark eyes with sharp inner corners and smoky crimson eyeliner wings, intoxicating amber-flecked pupils, thick sultry eyelashes, dangerously alluring gaze`
- **眉型与鼻梁**：极细挑起宛如弯刀的细长黛眉；琼鼻小巧挺拔，鼻翼精致微翘，透出一丝小狐狸般的灵动与狡黠。
  - *Prompt*: `fine arched high willow eyebrows, delicate straight slender nose with playful dainty tip`
- **唇型与面颊**：饱满水润的深红咬唇妆感花瓣唇，下唇极度饱满丰润，贝齿微咬下唇，双颊泛起情动的绯色潮红。
  - *Prompt*: `luscious deep berry-red plump lips, slightly parted with her white teeth gently biting her lower lip, flushed blushing high cheekbones, seductive sharp chin`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：慵懒披散的蓬松微卷黑曜石长发，如海藻般自然漫散于赤裸后背、锁骨与胸前，几缕青丝随意贴于香肩。
  - *Prompt*: `wildly beautiful cascading raven-black voluminous wavy hair, tousled effortlessly over her bare shoulders and framing her decolletage in glorious disarray`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：细腻如丝绸缎面的真实微观毛孔与天然皮脂光泽，微汗在烛光下如露珠般反光，锁骨与双峰线条高光温润耀眼。
  - *Prompt*: `authentic human skin texture with micro-pores, glistening subtle sheen of perspiration, warm candlelit specular highlights accentuating her collarbones, chest, and hip curve`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：水蛇般极富柔韧弹性的腰肢，饱满挺拔的胸部与圆润肉感的丰臀，大腿线条温润柔美，极具东方肉感美学的杀伤力。
  - *Prompt*: `extraordinary supple hourglass proportions, extremely narrow and flexible waistline, generous bustline, curvaceous rounded hips, smooth firm thighs, genuine female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.85`（搭配 CFG 4.0，极致突显私密寝殿诱惑力与皮肤水光汗珠） |
| **推荐 LoRA 2** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（搭配 CFG 2.5，精准刻画腰臀比与高精细解剖学轮廓） |
| **推理步数 (Steps)** | `45 - 50` | 保证散乱发丝与狐系眼妆细节完美呈现 |
| **引导系数 (CFG)** | `4.0` (TheseAlpacas) / `2.5` (tawsLoRa) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 低调暖色调神秘光影最佳表现 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显水蛇腰身与摄魂魅态 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定极致媚眼五官 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证苏魅儿的勾魂狐眸、咬唇神态与水蛇腰沙漏身材：

```text
A hyper-realistic full-body masterwork studio portrait of Su Mei'er, an intoxicating 22-year-old nine-tailed fox enchantress inspired by Chinese mythology. She is completely nude, posing in a sinuous kneeling arch posture on a luxurious crimson silk cushion against a deep charcoal wall with faint flickering golden candlelight. She has wildly tousled voluminous wavy raven-black hair flowing across her chest, piercing upturned fox-eyes with smoky red accents and an intensely seductive gaze, and deep berry-red parted lips with her teeth gently catching her lower lip. Her frame is a breathtaking hourglass with an ultra-flexible tiny waistline, generous natural bust, and rounded feminine hips. Warm amber dramatic side-lighting sculpts her supple curves, accentuating authentic fine pores, delicate moisture sheen, and rich specular highlights along her arched back, ribs, and thighs. Masterwork, 8k resolution, raw feminine magnetism, Hasselblad 100mm portrait photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
an intoxicating 22-year-old nine-tailed fox enchantress named Su Mei'er with tousled voluminous wavy jet-black hair falling wildly over her shoulders, piercing upturned seductive fox eyes with subtle red winged accents, luscious berry-red parted lips, possessing an intensely curvaceous supple hourglass frame with an ultra-narrow snake waist, full natural bust, rounded hips, and glowing warm alabaster skin with dewy micro-pores and sensual sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：中式古典红木雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)
将 `Su Mei'er` 模块化词块嵌入红幔烛影拔步床，化身寝殿中的绝代妖姬：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle wide shot of an intoxicating 22-year-old nine-tailed fox enchantress named Su Mei'er with tousled voluminous wavy jet-black hair falling wildly over her shoulders, piercing upturned seductive fox eyes with subtle red winged accents, luscious berry-red parted lips, possessing an intensely curvaceous supple hourglass frame with an ultra-narrow snake waist, full natural bust, rounded hips, and glowing warm alabaster skin with dewy micro-pores. She is completely nude, kneeling on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing three-quarters toward the camera, her back arched seductively with one hand resting delicately on the silk bolster behind her, her knees gently spread apart, head tilted with a dangerously enticing smile. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn08_su_meier `
  --prompt "A hyper-realistic, low-angle wide shot of an intoxicating 22-year-old nine-tailed fox enchantress named Su Mei'er with tousled voluminous wavy jet-black hair falling wildly over her shoulders, piercing upturned seductive fox eyes with subtle red winged accents, luscious berry-red parted lips, possessing an intensely curvaceous supple hourglass frame with an ultra-narrow snake waist, full natural bust, rounded hips, and glowing warm alabaster skin with dewy micro-pores. She is completely nude, kneeling on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing three-quarters toward the camera, her back arched seductively with one hand resting delicately on the silk bolster behind her, her knees gently spread apart, head tilted with a dangerously enticing smile. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture." `
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
  --out outputs/characters/cn08_su_meier_canopy.png
```
