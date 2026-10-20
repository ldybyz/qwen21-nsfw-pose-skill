# 人物卡：艾琳娜·沃尔科娃 (Elena Volkova) - 东欧斯拉夫冷艳超模

- **卡片编号**：`CA-02`
- **人物归属**：欧美高加索系 (Caucasian / 东欧斯拉夫)
- **主打风格**：斯拉夫高级骨相 / 锋利面部折角 / 深邃灰绿眼瞳 / 芭蕾舞者般的紧实线条
- **适配场景**：落地窗晨曦猫式伸展、古典画室人体、现代奢华淋浴、复古旅馆

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 艾琳娜·沃尔科娃 (Elena Volkova) | `striking 23-year-old Slavic woman named Elena Volkova` |
| **年龄 (Age)** | 23 岁 | `young 23 years old` |
| **文化背景** | 东欧乌克兰/捷克混血，前古典芭蕾舞演员，现国际顶级T台超模 | `Eastern European Slavic aristocratic aesthetic` |
| **身高体态** | 176cm，芭蕾舞者特有的修长紧实肌理，薄肌腹肌与紧致翘臀，骨感修长 | `176cm, ballerina-like lean musculature, sculpted collarbones, narrow waist, elongated limbs` |
| **肤色基底** | 象牙冷调雪白（Pale Ivory Snow），皮肤薄而坚韧，泛着微微哑光冷感 | `pale cool-toned porcelain ivory skin, smooth matte-satin finish` |
| **气质神态** | 冷峻高贵、英气凌厉、下颌微抬、充满压迫感的高级感与致命吸引力 | `aristocratic cold intensity, sharp unyielding gaze, subtle confident tilt of chin, feline elegance` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：标志性的斯拉夫猫系深陷大眼窝，迷人的灰绿色（Sage-Grey Green）眼瞳，内眼角锋利，长睫如羽扇。
  - *Prompt*: `intense deep-set sage-grey green almond eyes, razor-sharp inner corners, naturally dark heavy eyelashes, piercing smoldering gaze`
- **眉骨与鼻梁**：高耸锋利的斯拉夫高眉骨，山根极高挺直的窄鼻梁，鼻翼边缘转折分明。
  - *Prompt*: `prominent Slavic brow ridge with sculpted arched eyebrows, high straight narrow nose with defined delicate tip`
- **下颌与唇部**：下颌角清晰利落（Razor Jawline），高耸的颧骨将光线切成明显明暗交界线，唇形立体饱满偏豆沙裸色。
  - *Prompt*: `chiseled diamond-cut jawline, razor-sharp cheekbones casting distinct hollow shadows, defined mauve-nude lips slightly parted`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：浅灰亚麻金（Ash Blonde）披肩直发，发丝轻薄垂顺，自然散落在背部与锁骨周围。
  - *Prompt*: `sleek shoulder-length ash-blonde straight hair with cool silver undertones, feather-light strands framing sharp facial angles`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：极细腻的欧洲冷白皮质感，真实可见的表皮微毛孔，腹部与背部肌肉起伏处拥有极清晰的微弱高光反差。
  - *Prompt*: `authentic human micro-pores, refined matte-satin skin sheen, subtle anatomical shadow gradients along ribs and shoulder blades`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **体型特征**：长期舞蹈塑造的紧绷肌肉轮廓，紧致的人鱼线与马甲线，修长挺拔的腿部肌肉线条与圆润紧致的臀型。
  - *Prompt*: `ballerina posture, elongated slender neck, sculpted oblique lines and flat firm stomach, toned firm thighs, authentic human anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，解剖细节与冷峻骨相刻画绝佳） |
| **推荐 LoRA 2** | `nsfw-posture-v3.safetensors` | 权重 `0.85`（强化芭蕾舞级身体延展与脊椎张力） |
| **推理步数 (Steps)** | `45` | 保证骨骼转折阴影细腻平滑 |
| **引导系数 (CFG)** | `2.5` | 保证面部冷光不过曝 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最佳质感还原 |
| **生图分辨率** | `1152x1728` | 突出高挑挺拔姿态 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：极简艺术天窗侧光，测试艾琳娜的灰绿眼眸、斯拉夫骨相与芭蕾线条：

```text
A hyper-realistic full-body editorial art photograph of Elena Volkova, a striking 23-year-old Slavic high-fashion model with aristocratic beauty. She is completely nude, posing in a tense sculptural stance with one arm extended along an raw dark slate plinth in a sunlit architectural studio. She has sleek shoulder-length ash-blonde straight hair, piercing deep-set sage-grey green eyes with an intense feline gaze, razor-sharp cheekbones, a chiseled diamond jawline, and natural mauve-nude parted lips. Her 176cm lean ballerina physique displays elongated toned limbs, defined oblique muscles, smooth flat abdomen, and prominent collarbones. Dramatic low-angle northern window side-lighting creates crisp graphic shadow cuts across her sharp facial features and torso. Authentic realistic skin texture with visible micro-pores and satin specular sheen. Authentic photorealistic anatomy, 8k resolution, Masterpiece, Hasselblad medium format photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接替换任意 `prompts/scene_*.txt` 中的主体描述部分。

```text
a striking 23-year-old Slavic woman named Elena Volkova, featuring sleek shoulder-length ash-blonde straight hair, piercing deep-set sage-grey green eyes with an intense feline gaze, razor-sharp cheekbones, chiseled diamond jawline, and natural mauve-nude parted lips, possessing a tall 176cm lean ballerina physique with sculpted collarbones, toned stomach, long slender legs, and cool porcelain ivory skin with fine authentic pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 示例场景：落地窗晨曦·猫式跪趴伸展 (`prompts/scene_penthouse_stretch`)
将 `Elena Volkova` 模块化词块注入高空顶层公寓落地窗伸展场景，芭蕾肢体与晨曦侧逆光的绝美融合：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle oblique rear view photograph inside an ultra-luxury modern high-rise penthouse at dawn. A striking 23-year-old Slavic woman named Elena Volkova is completely nude on a thick charcoal wool rug near floor-to-ceiling panoramic glass windows. She features sleek shoulder-length ash-blonde hair falling forward over her shoulders, piercing sage-grey green eyes looking back with a cool seductive gaze, sharp cheekbones, and a lean ballerina physique with a sculpted spinal furrow and toned waistline. She is captured in a sensual yoga cat-cow stretch, kneeling on all fours with her hips arched high and spine gracefully curved, arms extended forward on the plush rug. Early morning golden sunrise light filters through sheer white curtains, casting a warm rim glow along the sharp curve of her back, the prominent slope of her hips, and the soft translucent contours of her lower anatomy framed clearly from the low rear-quarter perspective. Authentic skin texture with visible fine pores and subtle goosebumps from the cool morning air. 8k resolution, photorealistic anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_ca02_stretch `
  --prompt "A hyper-realistic, low-angle oblique rear view photograph inside an ultra-luxury modern high-rise penthouse at dawn. A striking 23-year-old Slavic woman named Elena Volkova is completely nude on a thick charcoal wool rug near floor-to-ceiling panoramic glass windows. She features sleek shoulder-length ash-blonde hair falling forward over her shoulders, piercing sage-grey green eyes looking back with a cool seductive gaze, sharp cheekbones, and a lean ballerina physique with a sculpted spinal furrow and toned waistline. She is captured in a sensual yoga cat-cow stretch, kneeling on all fours with her hips arched high and spine gracefully curved, arms extended forward on the plush rug. Early morning golden sunrise light filters through sheer white curtains, casting a warm rim glow along the sharp curve of her back, the prominent slope of her hips, and the soft translucent contours of her lower anatomy framed clearly from the low rear-quarter perspective. Authentic skin texture with visible fine pores and subtle goosebumps from the cool morning air. 8k resolution, photorealistic anatomy." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/ca02_elena_stretch.png
```
