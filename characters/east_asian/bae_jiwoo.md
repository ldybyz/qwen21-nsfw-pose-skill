# 人物卡：裴智友 (Bae Ji-woo) - 韩系优雅名媛轻熟御姐

- **卡片编号**：`EA-04`
- **人物归属**：东亚系 (East Asian / 韩系优雅)
- **主打风格**：财阀名媛气场 / 极致水光美肌 / 丰盈海藻大波浪 / S型曼妙身材
- **适配场景**：奢华游艇、普拉提塑形拉伸、落地窗公寓、顶层套房

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 裴智友 (Bae Ji-woo / 배지우) | `glamorous 25-year-old Korean woman named Bae Ji-woo` |
| **年龄 (Age)** | 25 岁 | `25 years old` |
| **文化背景** | 韩国首尔江南区名媛，顶级普拉提私教兼时尚生活博主 | `Korean modern luxury elite aesthetic` |
| **身高体态** | 169cm，凹凸有致的完美S型沙漏轮廓，饱满胸型与纤细腰肢，蜜桃臀线 | `curvaceous 169cm silhouette, defined hourglass figure, narrow waist, sculpted hips and firm toned legs` |
| **肤色基底** | 韩国江南顶级水光微透肌，通透白皙如凝脂，自带天然水润高光 | `luminous glass skin complexion, ultra-hydrated porcelain glow, flawless radiant sheen` |
| **气质神态** | 贵气慵懒、媚而不俗、眼神含水含笑、举手投足优雅从容 | `sophisticated seductive aura, mesmerizing dark eyes with glossy sheen, sultry confident smile, aristocratic poise` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：精致微开扇双眼皮，眼型狭长而妩媚，深邃黑曜石瞳仁，浓密纤长的卷翘睫毛。
  - *Prompt*: `refined almond-shaped dark eyes with delicate double eyelids, alluring wet glossiness, naturally long winged eyelashes`
- **眉型与鼻梁**：柔和微弧度的韩系羽雾野生眉，小巧立体水滴微翘鼻梁，鼻翼极窄精致。
  - *Prompt*: `softly-defined feathered arch eyebrows, slender refined high nose bridge with elegant upturned tip`
- **唇型与面部线条**：丰润的水光嘟嘟唇，天然珊瑚水红色，饱满唇珠微露，下巴尖巧弧度圆润。
  - *Prompt*: `full plump glossy coral-tinted lips with defined Cupid's bow, slightly parted, smooth heart-shaped face contour, delicate feminine jawline`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：蓬松浓密的海藻大波浪卷长发（Glamour S-Curl），披散在胸前与香肩，深摩卡黑棕色泽，发质丰盈丝滑。
  - *Prompt*: `voluminous cascading deep-mocha dark waves falling past her bust, effortless salon-grade blowout volume, rich silky sheen catching warm light`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：极具代表性的韩系水光肌（Glass Skin），锁骨、肩膀与苹果肌上带有一层高光精油般清透水亮薄膜，微细真孔自然分布。
  - *Prompt*: `iconic Korean glass skin texture, glistening dewy hydration highlights along collarbones, cheekbones, and shoulders, authentic micro-pores, ultra-smooth porcelain surface`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **体型特征**：长期普拉提训练造就的紧实曲线，饱满自然的胸部轮廓，11字马甲线与无赘肉平坦小腹，丰润饱满的蜜桃臀。
  - *Prompt*: `sculpted hourglass curves, firm lifted bust, slender waist with subtle 11-line ab definition, perfectly curved hips and smooth long thighs`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（高画质解剖细节与高光皮肤） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.85`（名媛网红私密感与微距自拍风格首选） |
| **推理步数 (Steps)** | `45 - 50` | 确保大波浪发丝质感与水光肌反射完全成型 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 标准基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最佳光影平滑度 |
| **生图分辨率** | `1152x1728` | 完美呈现饱满身材比例与面部高光 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：顶层公寓私密自然光写真，测试裴智友的海藻卷发、水光美肌与S型沙漏身材：

```text
A hyper-realistic full-body luxury fashion portrait of Bae Ji-woo, a gorgeous 25-year-old Korean high-society woman. She is completely nude, posing with effortless elegance on a plush ivory chaise lounge inside a sunlit Seoul penthouse overlooking the Han River. She has voluminous cascading deep-mocha waves falling over her bare shoulders, alluring glossy almond dark eyes, a small refined nose bridge, and plump glossy coral parted lips. Her 169cm athletic silhouette displays an enviable hourglass figure with slender waistline, toned 11-line abs, and shapely feminine hips. Soft morning sunlight streams through the panoramic glass windows, creating radiant dewy reflections across her iconic glass-skin complexion, illuminating delicate collarbone hollows and fine authentic skin pores. Genuine realistic anatomy, sophisticated opulent mood, 8k resolution, Masterpiece Hasselblad medium format photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接替换任意 `prompts/scene_*.txt` 中的主体描述部分。

```text
a glamorous 25-year-old Korean woman named Bae Ji-woo, featuring voluminous cascading deep-mocha waves, seductive glossy almond eyes, refined small nose, and plump glossy coral parted lips, possessing a breathtaking hourglass figure with a slender waist, firm curves, and luminous Korean glass-skin complexion with dewy radiant highlights and authentic micro-pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 示例场景：普拉提塑形·瑜伽垫拉伸 (`prompts/scene_pilates_stretch.txt`)
将 `Bae Ji-woo` 模块化词块注入普拉提健身房拉伸场景，尽显健美名媛的形体张力：

#### 合成完整 Prompt：
```text
A hyper-realistic, ultra-low ground-level wide-angle photograph inside a minimalist luxury pilates studio with polished dark timber floors. A glamorous 25-year-old Korean woman named Bae Ji-woo is completely nude, engaging in a deep post-workout stretch on a dark navy mat. She features voluminous cascading deep-mocha waves partially tied up with wispy strands around her neck, alluring glossy almond eyes, plump parted lips, and an enviable hourglass athletic frame. The camera is positioned on the floor between her heels looking up along her figure: she is lying on her back, performing an intense inner thigh stretch with her knees bent outward and hands gripping her ankles, opening her hips wide. A fine glistening sheen of perspiration covers her iconic Korean glass skin, highlighting her toned 11-line abs, smooth thighs, and the distinct anatomical contours of her lower body centered naturally in the frame. Soft morning diffuse light from large frosted industrial windows. Authentic skin texture with sweat beads and micro-pores. 8k resolution, photorealistic anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_ea04_pilates `
  --prompt "A hyper-realistic, ultra-low ground-level wide-angle photograph inside a minimalist luxury pilates studio with polished dark timber floors. A glamorous 25-year-old Korean woman named Bae Ji-woo is completely nude, engaging in a deep post-workout stretch on a dark navy mat. She features voluminous cascading deep-mocha waves partially tied up with wispy strands around her neck, alluring glossy almond eyes, plump parted lips, and an enviable hourglass athletic frame. The camera is positioned on the floor between her heels looking up along her figure: she is lying on her back, performing an intense inner thigh stretch with her knees bent outward and hands gripping her ankles, opening her hips wide. A fine glistening sheen of perspiration covers her iconic Korean glass skin, highlighting her toned 11-line abs, smooth thighs, and the distinct anatomical contours of her lower body centered naturally in the frame. Soft morning diffuse light from large frosted industrial windows. Authentic skin texture with sweat beads and micro-pores. 8k resolution, photorealistic anatomy." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/ea04_jiwoo_pilates.png
```
