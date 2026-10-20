# 人物卡：[CN-04] 杜雯 (Du Wen) - 现代东方·极简骨相超模

- **卡片编号**：`CN-04`
- **时代分类**：现代高级时尚 (Modern High Fashion)
- **原型灵感**：刘雯 (Liu Wen) + 杜鹃 (Du Juan) 顶级东方超模骨相神韵
- **主打风格**：高级厌世脸 / 刀刻下颌线 / 极品直角肩 / 179cm 黄金九头身 / 克制性冷淡风
- **适配场景**：现代顶层豪宅落地窗 (`prompts/scene_penthouse_stretch.txt`)、古典画室人体写生 (`prompts/scene_art_studio.txt`)、镜前黑白自拍 (`prompts/scene_mirror_selfie.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 杜雯 (Du Wen) | `striking 27-year-old Chinese high-fashion supermodel named Du Wen` |
| **年龄 (Age)** | 27 岁 | `mature refined 27 years old` |
| **职业与身份** | 国际顶尖T台高定超模，东方骨相美学代表人物 | `international haute couture runway supermodel, modern minimalist aesthetic` |
| **身高体态** | 179cm，极致挺拔骨相：直角肩、平胸微曲线、深凹锁骨、极具雕塑张力的马甲线与大长腿 | `tall 179cm statuesque runway frame, razor-sharp square shoulders, high collarbones, lean toned abs, long slender legs` |
| **肤色基底** | 纯净冷调玉色白皮，哑光清透质感，无任何多余瑕疵 | `matte cool-toned porcelain fair skin, clean minimalist luminescence` |
| **气质神态** | 清冷疏离、高级克制、不迎合镜头的从容掌控力，如冰封冷月 | `aloof haute couture gaze, enigmatic indifferent composure, striking minimalist poise` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：标志性东方高级内双/丹凤眼，眼型狭长而凌厉，眼神沉着清透，瞳孔黑亮深邃。
  - *Prompt*: `striking elongated dark monolid-almond eyes with sharp inner corners, calm penetrating high-fashion gaze, natural sparse clean eyelashes`
- **骨相与轮廓**：刀刻般分明的高颧骨与清晰利落的下颌线，无任何赘肉，立体感极强。
  - *Prompt*: `sculptural high cheekbones, razor-sharp clean jawline, noble straight nose bridge with a defined narrow tip`
- **唇部与神态**：天然裸粉色薄唇微抿，神态淡漠沉着，具有顶级时尚大片的非凡张力。
  - *Prompt*: `naturally nude-toned refined lips lightly pressed together, completely relaxed indifferent expression, elegant high forehead`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：极简齐肩中分黑直短发（Blunt Bob），发尾刀切般利落整齐，偶有几缕垂于凌厉锁骨前。
  - *Prompt*: `sleek minimalist shoulder-length blunt-cut black bob with a clean middle part, mirror-shine jet-black straight hair`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：现代高定棚拍级真实微观皮肤，哑光中带有自然光泽，微毛孔均匀细腻，直角肩和锁骨高光如大理石雕塑。
  - *Prompt*: `flawless yet authentic human skin texture with microscopic pores, subtle diffuse matte highlights on prominent collarbones and shoulders, clean anatomical lighting`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：标准超模九头身比：修长颈项、平直开阔的直角肩、平坦紧致腹肌线条、修长笔直的双腿与纤细脚踝。
  - *Prompt*: `statuesque 9-head proportions, high architectural square shoulders, modest refined bustline, flat toned abdomen with faint vertical ab line, ultra-long slender legs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美雕刻骨骼肌肉线条与解剖结构） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，强化超模大片生活化真实私密张力） |
| **推理步数 (Steps)** | `45 - 50` | 保证刀锋般下颌线与发型利落轮廓收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 锐利高动态光影表现 |
| **生图分辨率** | `1152x1728` (竖版全身) | 淋漓尽致展现 179cm 黄金身材比例 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定超模骨相脸 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于在极简高定灰墙前验证杜雯的超模骨相、刀刻下颌线与九头身体态：

```text
A hyper-realistic full-body haute couture editorial photograph of Du Wen, a striking 27-year-old Chinese supermodel. She is completely nude, standing in an assertive minimalist fashion pose against a neutral raw grey concrete wall. She has a sleek blunt-cut shoulder-length black bob, sharp elongated monolid almond eyes with an indifferent piercing gaze, sculptural high cheekbones, razor-sharp jawline, and natural nude lips. Her body is tall at 179cm with architectural square shoulders, deep prominent collarbones, a lean toned torso, and extraordinarily long slender legs. Soft directional fashion softbox lighting sculps her defined muscle tone and bone structure, accentuating authentic skin pores and subtle specular highlights along her spine and ribs. Masterwork, 8k resolution, Vogue editorial aesthetic, Hasselblad H6D-100c medium format.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a striking 27-year-old Chinese high-fashion supermodel named Du Wen with sleek shoulder-length blunt black bob, sharp monolid-almond eyes with an indifferent cool gaze, sculptural high cheekbones and razor jawline, possessing a tall 179cm statuesque frame with architectural square shoulders, prominent collarbones, lean toned abdomen, and matte porcelain skin with authentic fine pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：顶层豪宅全景落地窗 (`prompts/scene_penthouse_stretch.txt`)
将 `Du Wen` 模块化词块嵌入晨曦顶层豪宅落地窗前：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle full-body photograph of a striking 27-year-old Chinese high-fashion supermodel named Du Wen with sleek shoulder-length blunt black bob, sharp monolid-almond eyes with an indifferent cool gaze, sculptural high cheekbones and razor jawline, possessing a tall 179cm statuesque frame with architectural square shoulders, prominent collarbones, lean toned abdomen, and matte porcelain skin with authentic fine pores. She is completely nude, positioned in a graceful yoga stretch on a polished dark hardwood floor in front of a massive floor-to-ceiling glass window of a luxury high-rise penthouse. Her long slender body is arched backward in a deep camel stretch, head tilted gracefully back, hands resting lightly on her heels, accentuating the long arch of her throat, ribcage, toned stomach, and thighs. Golden morning dawn sunlight floods through the panoramic glass, backlighting her silhouette with a brilliant warm rim light while soft ambient interior light sculpts the front of her body. Beyond the glass, the misty city skyline stretches into the sunrise. The low perspective captures her long toned legs and lower anatomy in clear, natural anatomical detail. 8k resolution, architectural lighting, sharp focus, masterwork.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn04_du_wen `
  --prompt "A hyper-realistic, low-angle full-body photograph of a striking 27-year-old Chinese high-fashion supermodel named Du Wen with sleek shoulder-length blunt black bob, sharp monolid-almond eyes with an indifferent cool gaze, sculptural high cheekbones and razor jawline, possessing a tall 179cm statuesque frame with architectural square shoulders, prominent collarbones, lean toned abdomen, and matte porcelain skin with authentic fine pores. She is completely nude, positioned in a graceful yoga stretch on a polished dark hardwood floor in front of a massive floor-to-ceiling glass window of a luxury high-rise penthouse. Her long slender body is arched backward in a deep camel stretch, head tilted gracefully back, hands resting lightly on her heels, accentuating the long arch of her throat, ribcage, toned stomach, and thighs. Golden morning dawn sunlight floods through the panoramic glass, backlighting her silhouette with a brilliant warm rim light while soft ambient interior light sculpts the front of her body. Beyond the glass, the misty city skyline stretches into the sunrise. The low perspective captures her long toned legs and lower anatomy in clear, natural anatomical detail. 8k resolution, architectural lighting, sharp focus, masterwork." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn04_du_wen_penthouse.png
```
