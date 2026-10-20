# 人物卡：[CN-10] 甄洛仙 (Zhen Luoxian) - 魏晋绝响·洛神惊鸿

- **卡片编号**：`CN-10`
- **时代分类**：三国魏晋 (Three Kingdoms / Wei-Jin Dynasties)
- **原型灵感**：甄宓 / 洛神（融合蔡少芬经典版《洛神》及曹植《洛神赋》“翩若惊鸿，婉若游龙”神韵）
- **主打风格**：凌波微步 / 罗袜生尘 / 魏晋凌云高髻 / 仙风道骨 / 高洁清冷第一神女
- **适配场景**：幽篁竹林私密水阁 (`prompts/scene_bamboo_courtyard.txt`)、江南水阁临渊 (`prompts/scene_jiangnan_pavilion.txt`)、古典画室人体写生 (`prompts/scene_art_studio.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 甄洛仙 (Zhen Luoxian) | `divine 22-year-old Wei-Jin goddess maiden named Zhen Luoxian` |
| **年龄 (Age)** | 22 岁 | `transcendent 22 years old` |
| **文学与历史渊源** | 三国魏国文昭甄皇后，曹植笔下洛水神女原型，江南有二乔，河北甄宓俏 | `Wei-Jin Dynasties classical royalty, legendary Goddess of the Luo River archetype` |
| **身高体态** | 168cm，翩若惊鸿的身段，修长挺拔天鹅颈，肩若削成腰如约素，骨肉停匀清逸绝尘 | `slender ethereal frame, swan-like graceful neck, razor-sharp delicate shoulders, fluid serpentine dancer posture` |
| **肤色基底** | 质洁如冰霜，明艳若朝霞，通透的冷调象牙雪白肤质，流转着微蓝月华光芒 | `crystalline alabaster fair skin with cool moonlight luminescence, flawless jade-like translucency` |
| **气质神态** | 遗世独立，含睇宜笑，神情高贵圣洁却又带着一丝看破红尘的淡淡哀愁 | `regal divine gaze, subtle aloof grace, transcendent poised expression, melancholic immortal beauty` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：东方绝品修长凤眼，内双含威，瞳孔深邃如墨玉含星，流盼生辉。
  - *Prompt*: `elongated majestic dark phoenix eyes with subtle epicanthic fold, sparkling obsidian pupils, dense natural lashes, breathtaking otherworldly divine gaze`
- **眉型与鼻梁**：修长连娟的魏晋细长翠眉；琼鼻修长笔直，山根隆起，鼻若悬胆。
  - *Prompt*: `finely penciled long arched crescent eyebrows, pristine straight aristocratic nose bridge with refined narrow tip`
- **唇型与面颊**：天然朱丹红唇微微抿起，唇峰清晰锋利，下颌线条如流水般流畅优雅。
  - *Prompt*: `refined crimson rosebud lips with sharply sculpted Cupid's bow lightly closed, pristine oval face, smooth aristocratic bone structure`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：魏晋标志性巍峨飘逸的凌云髻（灵蛇髻），几缕青丝被微风托起若凌波而舞，插有一枚薄翼点翠金凤步摇。
  - *Prompt*: `elaborate Wei-Jin soaring cloud chignon (Lingyun ji) adorned with delicate golden filigree and kingfisher feather hairpins, silky raven hair dancing in soft breeze`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：如寒冰暖玉般散发冷光的真人体表微观毛孔，锁骨如刀削玉琢，在月光下呈现宛如珍珠母贝般的漫射高光。
  - *Prompt*: `authentic human skin texture with microscopic pores, soft pearlescent subsurface scattering, cool moonlit specular sheen sculpted along collarbones and ribs`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：极富仙气与柔韧度的东方神女身材：天鹅颈、平削直角肩、修长柔软的腰线、高挑纤细的玉腿。
  - *Prompt*: `statuesque fairy proportions, elegant long neck, delicate prominent collarbones, extraordinarily supple narrow waist, long toned slender legs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美刻画魏晋清峻骨相与仙神般高贵肉身） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，强化月光清泉下的微观肌肤质感） |
| **推理步数 (Steps)** | `45 - 50` | 保证凌云髻与飘逸发丝光影完全收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 纯净清冷月色光的最佳表现 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显凌波微步的高挑神姿与仙韵 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定魏晋仙子骨相 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证甄洛仙的洛神天姿、凌云高髻与冰肌玉骨：

```text
A hyper-realistic full-body masterwork studio portrait of Zhen Luoxian, a divine 22-year-old Wei-Jin Dynasty goddess maiden inspired by the Goddess of the Luo River. She is completely nude, standing in an elegant weightless contrapposto pose as if walking on water ripples against a minimalist midnight-blue silk wall. She has an elaborate soaring cloud chignon adorned with subtle golden pins, elongated dark phoenix eyes with a regal transcendent gaze, finely arched crescent eyebrows, and sharply defined crimson lips lightly closed. Her frame is tall and slender with a swan-like neck, sharp collarbones, a tiny supple waistline, and extraordinarily long slender legs. Cool silvery-blue celestial moonlight sculps her alabaster skin, revealing authentic microscopic pores, delicate pearlescent sheen, and pristine anatomical shadows. Supreme classical oriental divinity, 8k resolution, Hasselblad 100mm medium format photograph.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a divine 22-year-old Wei-Jin Dynasty goddess maiden named Zhen Luoxian with elaborate soaring cloud chignon, elongated majestic dark phoenix eyes with a transcendent calm gaze, sharply defined crimson lips, possessing an ethereal slender frame with a swan neck, sharp collarbones, supple narrow waistline, and crystalline alabaster fair skin with cool moonlit sheen and authentic fine pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：幽篁竹林私密水阁 (`prompts/scene_bamboo_courtyard.txt`)
将 `Zhen Luoxian` 模块化词块嵌入月下竹影寒泉：

#### 合成完整 Prompt：
```text
A hyper-realistic wide-angle cinematic shot of a divine 22-year-old Wei-Jin Dynasty goddess maiden named Zhen Luoxian with elaborate soaring cloud chignon, elongated majestic dark phoenix eyes with a transcendent calm gaze, sharply defined crimson lips, possessing an ethereal slender frame with a swan neck, sharp collarbones, supple narrow waistline, and crystalline alabaster fair skin with cool moonlit sheen and authentic fine pores. She is completely nude, seated in a flexible kneeling arched posture on a smooth dark river-stone terrace in an ancient moonlit courtyard surrounded by towering emerald bamboo stalks. One slender arm is extended touching a mossy rock, her back gracefully arched to highlight her slender spine and feminine curves. Pale cool moonlight filters through the bamboo leaves, casting intricate dancing dappled shadow patterns across her alabaster skin. Subtle water mist rises from a shallow stone reflecting pool in front of her. The low camera angle captures the soft contours of her lower anatomy naturally illuminated by the ambient moonlit water reflections. 8k resolution, atmospheric mist, photorealistic anatomy, cinematic lighting.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn10_zhen_luoxian `
  --prompt "A hyper-realistic wide-angle cinematic shot of a divine 22-year-old Wei-Jin Dynasty goddess maiden named Zhen Luoxian with elaborate soaring cloud chignon, elongated majestic dark phoenix eyes with a transcendent calm gaze, sharply defined crimson lips, possessing an ethereal slender frame with a swan neck, sharp collarbones, supple narrow waistline, and crystalline alabaster fair skin with cool moonlit sheen and authentic fine pores. She is completely nude, seated in a flexible kneeling arched posture on a smooth dark river-stone terrace in an ancient moonlit courtyard surrounded by towering emerald bamboo stalks. One slender arm is extended touching a mossy rock, her back gracefully arched to highlight her slender spine and feminine curves. Pale cool moonlight filters through the bamboo leaves, casting intricate dancing dappled shadow patterns across her alabaster skin. Subtle water mist rises from a shallow stone reflecting pool in front of her. The low camera angle captures the soft contours of her lower anatomy naturally illuminated by the ambient moonlit water reflections. 8k resolution, atmospheric mist, photorealistic anatomy, cinematic lighting." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn10_zhen_luoxian_bamboo.png
```
