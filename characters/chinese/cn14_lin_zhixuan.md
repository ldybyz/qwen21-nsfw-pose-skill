# 人物卡：[CN-14] 林芷萱 (Lin Zhixuan) - 民国才女·人间四月天

- **卡片编号**：`CN-14`
- **时代分类**：民国黄金年代 (1920s-1930s Republic Era)
- **原型灵感**：林徽因（融合周迅经典电视剧《人间四月天》秀逸清灵、知性书卷第一白月光神韵）
- **主打风格**：人间四月天 / 民国秀逸书卷气 / 纯净双麻花辫 / 清澈大杏眼 / 羊脂白玉纤瘦骨感
- **适配场景**：古典画室人体写生 (`prompts/scene_art_studio.txt`)、新中式茶室 (`prompts/scene_chinese_tearoom.txt`)、镜前微醺自拍 (`prompts/scene_mirror_selfie.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 林芷萱 (Lin Zhixuan) | `poetic intellectual 21-year-old 1930s Chinese literary muse named Lin Zhixuan` |
| **年龄 (Age)** | 21 岁 | `pure youthful 21 years old` |
| **时代背景** | 民国北平与剑桥书香世家，建筑学者与现代诗人，文化界公认的第一白月光 | `1920s-1930s Republican Chinese intellectual elite, architectural scholar muse` |
| **身高体态** | 165cm，亭亭玉立的纤细学者身材，肩颈秀丽，腰肢纤软，体态文雅端庄 | `slender delicate frame, poised upright posture, slender waist, soft feminine curves` |
| **肤色基底** | 如羊脂白玉般纯净洁白，微带淡淡的粉嫩血色，通透宛若朝露 | `translucent alabaster fair skin with subtle rosy undertones, pristine dewy finish` |
| **气质神态** | 灵慧秀逸、谈笑生风；双眸如含晨星，温文尔雅中透出一股独立坚毅的书卷力量 | `radiant intelligent gaze, tender gentle smile, noble scholarly aura, pure innocent poise` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：极其清澈的大杏仁眼，黑白分明，眼神清朗纯澈如清晨微露，长睫纤细自然。
  - *Prompt*: `wide luminous dark brown almond eyes filled with sparkling intellect, fine naturally long eyelashes, clear innocent yet profound gaze`
- **眉型与鼻梁**：天然秀气微扬的远山细黛眉；鼻梁挺直小巧，山根线条优雅自然。
  - *Prompt*: `natural fine soft-arched eyebrows, delicately sculpted straight nose bridge with dainty tip`
- **唇型与面颊**：天然樱粉色柔嫩小唇，唇角常带一丝知性温婉的浅笑；面颊轮廓秀气如鹅卵石。
  - *Prompt*: `tender petal-pink lips naturally curved into a soft thoughtful smile, delicate oval jawline, high noble forehead`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：民国标志性的清纯双麻花长辫垂于胸前两侧，发丝乌黑柔顺，额前几缕细碎刘海自然随风微动。
  - *Prompt*: `neat glossy jet-black hair parted in the middle and braided into two long soft twin braids resting across bare chest, faint wispy bangs`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：晨光漫射下的真实微观皮肤纹理，微毛孔均匀细嫩，锁骨、肋骨与香肩带有自然通透的柔光反射。
  - *Prompt*: `authentic fine human skin texture with microscopic pores, soft natural subsurface scattering, delicate specular sheen on prominent collarbones and shoulders`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：纤秀雅致的大家闺秀身段：秀丽锁骨、紧致平坦的小腹、修长匀称的纤细双腿，天生带着一种书香门第的纯净美感。
  - *Prompt*: `delicate slender maiden proportions, modest natural bust, extraordinarily narrow waist, smooth toned abdomen, long slender legs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，老照片胶片感与私密写真的纯欲碰撞） |
| **推荐 LoRA 2** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（搭配 CFG 2.5，精准还原清瘦真人体态与解剖学轮廓） |
| **推理步数 (Steps)** | `45 - 50` | 保证双麻花发丝质感与清澈眼神收敛完整 |
| **引导系数 (CFG)** | `4.0` (TheseAlpacas) / `2.5` (tawsLoRa) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 柔和晨曦漫射光的最佳组合 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显民国初恋身姿与灵气容颜 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定清纯才女面庞 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证林芷萱的民国才女容颜、双麻花发型与纯白美玉身段：

```text
A hyper-realistic full-body masterwork studio portrait of Lin Zhixuan, a poetic 21-year-old 1930s Chinese literary muse. She is completely nude, posing in a modest, upright sitting posture on a simple vintage wooden stool against a clean warm cream plaster wall bathed in soft morning window light. She has glossy jet-black hair parted in the middle and braided into two neat twin braids resting over her bare chest, wide luminous dark brown almond eyes with an intelligent gentle gaze, finely arched eyebrows, and soft pink lips curved in a subtle smile. Her frame is gracefully slender with delicate prominent collarbones, a tiny waistline, and smooth pale legs. Soft cinematic north-window diffuse sunlight sculpts her porcelain white skin, revealing authentic micro-pores, natural soft subsurface scattering, and dewy highlights along her spine and shoulders. Masterwork, 8k resolution, timeless literary elegance, Hasselblad 80mm portrait photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a poetic intellectual 21-year-old 1930s Chinese literary muse named Lin Zhixuan with glossy jet-black hair in twin braids over her chest, wide luminous intelligent dark almond eyes, soft petal-pink smiling lips, possessing a gracefully slender frame with prominent collarbones, narrow waistline, and translucent alabaster fair skin with authentic fine pores and dewy sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：古典画室人体写生 (`prompts/scene_art_studio.txt`)
将 `Lin Zhixuan` 模块化词块嵌入充满艺术气息的画室写生场景：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle photograph of a poetic intellectual 21-year-old 1930s Chinese literary muse named Lin Zhixuan with glossy jet-black hair in twin braids over her chest, wide luminous intelligent dark almond eyes, soft petal-pink smiling lips, possessing a gracefully slender frame with prominent collarbones, narrow waistline, and translucent alabaster fair skin with authentic fine pores inside a sunlit vintage artist loft studio. She is completely nude, posing as an art model on a weathered wooden pedestal draped with white cotton canvas. The camera is placed at low floor level angled upward: she is sitting in three-quarter profile with one leg extended gracefully forward and the other knee drawn up toward her torso, one arm resting across her knee. Soft morning north-skylight washes over her body, casting delicate natural shadows along her ribcage, waist, and inner thighs, accentuating her authentic anatomical contours. In the background are wooden easels with stretched canvases, oil paint tubes, glass jars, and rustic brick walls. The low angle captures the natural contours of her pelvic region and inner thighs in soft, artistic shadow and gentle specular highlight. 8k resolution, painterly cinematic lighting, genuine human skin texture.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn14_lin_zhixuan `
  --prompt "A hyper-realistic, low-angle photograph of a poetic intellectual 21-year-old 1930s Chinese literary muse named Lin Zhixuan with glossy jet-black hair in twin braids over her chest, wide luminous intelligent dark almond eyes, soft petal-pink smiling lips, possessing a gracefully slender frame with prominent collarbones, narrow waistline, and translucent alabaster fair skin with authentic fine pores inside a sunlit vintage artist loft studio. She is completely nude, posing as an art model on a weathered wooden pedestal draped with white cotton canvas. The camera is placed at low floor level angled upward: she is sitting in three-quarter profile with one leg extended gracefully forward and the other knee drawn up toward her torso, one arm resting across her knee. Soft morning north-skylight washes over her body, casting delicate natural shadows along her ribcage, waist, and inner thighs, accentuating her authentic anatomical contours. In the background are wooden easels with stretched canvases, oil paint tubes, glass jars, and rustic brick walls. The low angle captures the natural contours of her pelvic region and inner thighs in soft, artistic shadow and gentle specular highlight. 8k resolution, painterly cinematic lighting, genuine human skin texture." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn14_lin_zhixuan_studio.png
```
