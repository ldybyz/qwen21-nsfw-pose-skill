# 人物卡：林语婷 (Lin Yuting) - 江南古典温婉闺秀

- **卡片编号**：`EA-01`
- **人物归属**：东亚系 (East Asian / 华夏江南)
- **主打风格**：古典温婉 / 羊脂白玉肌 / 东方闺阁雅致美学
- **适配场景**：新中式茶室、古典闺房拔步床、烟雨江南水阁、竹林庭院

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 林语婷 (Lin Yuting) | `graceful 23-year-old Chinese woman named Lin Yuting` |
| **年龄 (Age)** | 23 岁 | `young 23 years old` |
| **文化背景** | 中国江南水乡，书香温婉名门闺秀 | `classical Chinese aesthetic heritage` |
| **身高体态** | 166cm，体态骨肉亭匀，肩颈纤细微削，腰肢纤软 | `slender delicate frame, soft natural feminine curves, graceful sloping shoulders` |
| **肤色基底** | 极致通透的冷白偏象牙光泽，细腻如脂玉 | `luminous porcelain pale fair skin, delicate milky translucent tone` |
| **气质神态** | 含蓄内敛，眉目含情，如幽兰初绽，温婉宁静 | `serene gentle expression, subtle shy smile with delicately parted lips, modest yet alluring gaze` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：东方标准杏核眼，内眦微敛，清澈深褐色瞳仁，眼波流转，睫毛纤长根根分明。
  - *Prompt*: `clear almond-shaped dark brown eyes with delicate subtle epicanthic fold, fine naturally long eyelashes, tender gentle gaze`
- **眉型与鼻梁**：远山黛柳叶细眉，鼻梁纤细秀挺，鼻头微翘小巧。
  - *Prompt*: `delicate soft willow-leaf arched eyebrows, slender refined straight nose with small gentle tip`
- **唇型与面颊**：天然樱粉色柔嫩樱桃小唇，饱满微启，下唇略丰盈，双颊透出极淡白里透红血色。
  - *Prompt*: `soft naturally rose-tinted petal-shaped lips slightly parted, smooth jawline with elegant feminine chin, soft blush undertone`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：及腰中分如瀑黑长直发，发丝柔顺富有丝绸光泽，两侧几缕碎发自然散落于锁骨与前胸。
  - *Prompt*: `waist-length silky smooth straight jet-black hair with mirror-like shine, flowing softly over her shoulders and down her spine`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：羊脂玉般极其细腻的真人体表微观纹理，微细毛孔清晰可见，肩颈锁骨与胸前带有自然漫反射微光，无瑕通透。
  - *Prompt*: `authentic human skin texture with microscopic pores, soft glowing subsurface scattering, subtle dewy sheen over collarbones and decolletage, flawless porcelain clarity`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **体型特征**：娇小纤细但不失女性柔美曲线，锁骨轮廓优美，腰肢纤细，小腹平坦微凹，双腿修长匀称。
  - *Prompt*: `delicate collarbones, slender waistline, gentle rounded hips, smooth firm thighs, authentic feminine anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美雕刻东方面部轮廓与真人体态） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（需搭配 CFG 4.0 + 负面词，更偏向生活化私密写真） |
| **推理步数 (Steps)** | `45 - 50` | 保证发丝光泽与羊脂白玉肤感收敛完整 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最佳质感与光影平衡 |
| **生图分辨率** | `1152x1728` (竖版人像) | 完美契合全身构图与面部细节 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 经典稳定种子 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：使用极简自然漫射光，测试林语婷的面部、及腰黑发与纯净玉肤：

```text
A hyper-realistic, medium-full shot studio photograph of Lin Yuting, a graceful 23-year-old Chinese woman with classical oriental beauty. She is completely nude, sitting gracefully on a minimalist light-grey linen mat in front of a warm rice-paper screen. Her body is slightly turned in an elegant three-quarter view, one slender hand resting gently on her thigh, showcasing her delicate collarbones, slender waist, and soft feminine curves. She has waist-length straight silky jet-black hair falling naturally over her back, clear almond-shaped dark brown eyes with a gentle tender gaze, and soft petal-pink parted lips. Warm diffuse natural light casts a soft golden glow on her luminous porcelain fair skin, highlighting authentic micro-skin pores and subtle collarbone specular reflections. Genuine photorealistic anatomy, tranquil aesthetic mood, 8k resolution, Masterpiece Hasselblad portrait.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接替换任意 `prompts/scene_*.txt` 中的主体描述部分（如 `a woman...`）。

```text
a graceful 23-year-old Chinese woman named Lin Yuting, featuring serene delicate oriental facial features, tender dark brown almond eyes, and soft petal-pink parted lips, with waist-length straight silky jet-black hair flowing naturally over her shoulders, possessing a slender feminine frame with delicate collarbones, graceful waist, and luminous porcelain fair skin with subtle authentic pores and dewy sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 示例场景：新中式茶室 (`prompts/scene_chinese_tearoom.txt`)
将 `Lin Yuting` 模块化词块无缝注入新中式茶室场景：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle photograph of a graceful 23-year-old Chinese woman named Lin Yuting inside an elegant minimalist modern tea pavilion. She is completely nude, sitting on a woven tatami floor cushion next to a low black walnut tea table. She features serene delicate oriental facial features, tender dark brown almond eyes, soft petal-pink parted lips, waist-length straight silky jet-black hair flowing naturally over her shoulders, a slender feminine frame with delicate collarbones, and luminous porcelain fair skin with subtle authentic pores. The camera shoots from the floor level looking up at her figure: she is kneeling with her knees gently parted, one hand gracefully resting on the edge of the tea tray near a steaming purple clay teapot, her other hand placed on her thigh. Warm diffuse light shines through a translucent rice-paper wooden lattice screen behind her, casting subtle bamboo shadows and outlining her silhouette. Gentle swirls of tea steam rise into the air. The low angle naturally frames the distinct contours of her lower anatomy in the center between her parted thighs. 8k resolution, cinematic warm atmospheric lighting, photorealistic anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_ea01_tearoom `
  --prompt "A hyper-realistic, low-angle photograph of a graceful 23-year-old Chinese woman named Lin Yuting inside an elegant minimalist modern tea pavilion. She is completely nude, sitting on a woven tatami floor cushion next to a low black walnut tea table. She features serene delicate oriental facial features, tender dark brown almond eyes, soft petal-pink parted lips, waist-length straight silky jet-black hair flowing naturally over her shoulders, a slender feminine frame with delicate collarbones, and luminous porcelain fair skin with subtle authentic pores. The camera shoots from the floor level looking up at her figure: she is kneeling with her knees gently parted, one hand gracefully resting on the edge of the tea tray near a steaming purple clay teapot, her other hand placed on her thigh. Warm diffuse light shines through a translucent rice-paper wooden lattice screen behind her, casting subtle bamboo shadows and outlining her silhouette. Gentle swirls of tea steam rise into the air. The low angle naturally frames the distinct contours of her lower anatomy in the center between her parted thighs. 8k resolution, cinematic warm atmospheric lighting, photorealistic anatomy." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/ea01_lin_yuting_tearoom.png
```
