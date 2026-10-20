# 人物卡：阿莱西亚·罗曼诺 (Alessia Romano) - 地中海艳阳火辣沙漏女神

- **卡片编号**：`CA-04`
- **人物归属**：欧美高加索系 (Caucasian / 南欧地中海意大利)
- **主打风格**：地中海风情 / 暖金蜜糖小麦肌 / 浓密深棕大卷发 / 丰满性感沙漏身材
- **适配场景**：奢华游艇地中海日光浴、落日海蚀礁石、SPA俯卧按摩、芬兰桑拿

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 阿莱西亚·罗曼诺 (Alessia Romano) | `voluptuous 26-year-old Italian Mediterranean woman named Alessia Romano` |
| **年龄 (Age)** | 26 岁 | `26 years old` |
| **文化背景** | 意大利西西里岛与阿马尔菲海岸，兼具古典热情与现代高级性感 | `Southern Italian Mediterranean coastal aesthetic` |
| **身高体态** | 172cm，极具张力与视觉冲击力的丰满沙漏体态（Hourglass Physique），纤细腰肢与丰臀长腿 | `172cm, curvaceous hourglass figure, full feminine curves, narrow waist, generous hips, sculpted long legs` |
| **肤色基底** | 沐浴地中海艳阳的暖金色蜜糖小麦皮（Sun-Kissed Honey Olive），健康紧实，天生发光 | `sun-kissed warm golden honey-tan skin, rich olive undertone, radiant healthy glow` |
| **气质神态** | 热情明艳、自信野性、眼神热烈如火、笑意妩媚又充满女王气场 | `fiery passionate presence, magnetic dark hazel eyes, confident sultry smile, unapologetic sensuality` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：深邃热烈的大杏仁眼，浓郁暖琥珀深褐色瞳仁，浓密深黑卷翘睫毛，目光灼灼自带诱惑。
  - *Prompt*: `large expressive warm dark-hazel almond eyes, naturally dense dark lashes, bold smoldering passionate gaze`
- **眉型与鼻骨**：浓密英气的意大利高弓野生眉，高挺笔直的古典罗马鼻梁，五官极具骨量与立体度。
  - *Prompt*: `bold naturally feathered arched dark eyebrows, high straight classical Roman nose bridge with defined profile`
- **唇型与下颌**：丰厚性感的焦糖裸棕色饱满厚唇，唇峰立体，线条清晰分明，下巴微微扬起。
  - *Prompt*: `full plump pouty lips in warm caramel-nude with distinct Cupid's bow, defined sunlit jawline, strong sensual facial bone structure`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：浓密蓬松如海浪般的深巧克力浓棕大波浪卷长发（Espresso Brown Waves），随海风自然披散，野性浪漫。
  - *Prompt*: `voluminous cascading rich espresso-brown wavy curls with sun-bleached golden tips, windblown Mediterranean texture`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：日光浴后泛着镜面精油反光的微汗蜜糖肌，锁骨与大腿边缘金光粼粼，微小毛孔与微小晒斑自然真实。
  - *Prompt*: `radiant sun-kissed honey skin texture with fine realistic pores, glistening monoi oil sheen catching direct sunlight, golden specular highlights along decolletage and hips`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **体型特征**：经典的南欧丰满沙漏轮廓，饱满圆润的胸部轮廓，极致腰臀比，紧致无赘肉小腹与充满肉欲美感的丰腴大腿。
  - *Prompt*: `dramatic hourglass proportions, full natural bust, cinched waist, wide rounded feminine hips, firm curvaceous thighs, authentic anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美表现高光精油与丰满骨骼轮廓） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，绝配日光浴与海滩写实质感） |
| **推理步数 (Steps)** | `45 - 50` | 保证蜜糖肤色与油光反光平滑无噪斑 |
| **引导系数 (CFG)** | `2.5` | 避免日光高反差处过曝 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最佳暖调色彩渲染 |
| **生图分辨率** | `1152x1728` | 完美呈现性感沙漏全身线条 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：地中海悬崖阳光露台，测试阿莱西亚的深棕卷发、蜜糖暖肤与极具冲击力的沙漏曲线：

```text
A hyper-realistic full-body summer photograph of Alessia Romano, a gorgeous 26-year-old Italian Mediterranean woman with breathtaking sensuality. She is completely nude, posing confidently against a sun-warmed whitewashed stone balustrade overlooking the turquoise waters of the Amalfi Coast. She has voluminous cascading espresso-brown wavy curls catching warm sunlight, bold dark arched eyebrows, expressive warm hazel-brown eyes with a passionate sultry gaze, and full plump caramel-nude parted lips. Her 172cm hourglass physique features a full bust, a narrow waist, and generous curved hips. Brilliant midday Mediterranean sunlight washes over her warm golden honey-tan skin, highlighting an authentic light layer of shimmering tanning oil with realistic specular reflections on her collarbones, flat abdomen, and shapely thighs. Authentic human skin texture with micro-pores, masterwork cinematic warm color grading, 8k resolution, Hasselblad 80mm photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接替换任意 `prompts/scene_*.txt` 中的主体描述部分。

```text
a voluptuous 26-year-old Italian Mediterranean woman named Alessia Romano, featuring voluminous cascading espresso-brown wavy hair, expressive warm hazel-brown eyes with a smoldering passionate gaze, high classical Roman nose, and full plump caramel-nude lips, possessing a dramatic hourglass physique with full feminine curves, narrow waist, generous hips, and sun-kissed golden honey-tan skin with authentic fine pores and glistening sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 示例场景：奢华游艇·地中海日光浴 (`prompts/scene_yacht_sunbathing.txt`)
将 `Alessia Romano` 模块化词块注入地中海游艇场景，热烈阳光与沙漏身材的天作之合：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle eye-level photograph of a voluptuous 26-year-old Italian Mediterranean woman named Alessia Romano sunbathing completely nude on the teak deck of a luxury yacht in the middle of the Mediterranean sea. She features voluminous cascading espresso-brown waves with golden sunlit highlights, warm dark-hazel eyes with a bold gaze, full plump lips, and a dramatic hourglass physique. She lies stretched out on a striped nautical towel with one knee bent and raised, one arm resting over her forehead to block the blinding sun. The intense direct midday Mediterranean sun bathes the scene, catching mirror-like highlights from the thick tanning oil generously applied all over her warm golden honey-tan skin, accentuating the contours of her collarbones, narrow waist, and the distinct anatomical details of her lower anatomy framed along the low deck view between her parted legs. In the background, calm azure deep blue ocean extends to the crisp horizon line. Authentic micro-pores and oil droplets, 8k resolution, photorealistic anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_ca04_yacht `
  --prompt "A hyper-realistic, low-angle eye-level photograph of a voluptuous 26-year-old Italian Mediterranean woman named Alessia Romano sunbathing completely nude on the teak deck of a luxury yacht in the middle of the Mediterranean sea. She features voluminous cascading espresso-brown waves with golden sunlit highlights, warm dark-hazel eyes with a bold gaze, full plump lips, and a dramatic hourglass physique. She lies stretched out on a striped nautical towel with one knee bent and raised, one arm resting over her forehead to block the blinding sun. The intense direct midday Mediterranean sun bathes the scene, catching mirror-like highlights from the thick tanning oil generously applied all over her warm golden honey-tan skin, accentuating the contours of her collarbones, narrow waist, and the distinct anatomical details of her lower anatomy framed along the low deck view between her parted legs. In the background, calm azure deep blue ocean extends to the crisp horizon line. Authentic micro-pores and oil droplets, 8k resolution, photorealistic anatomy." `
  --seed 80964 `
  --steps 50 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/ca04_alessia_yacht.png
```
