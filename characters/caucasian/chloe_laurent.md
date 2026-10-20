# 人物卡：克洛伊·洛朗 (Chloé Laurent) - 法式慵懒浪漫知性美人

- **卡片编号**：`CA-03`
- **人物归属**：欧美高加索系 (Caucasian / 西欧法兰西)
- **主打风格**：法式慵懒 (Effortless Chic) / 榛果暖棕微乱发 / 琥珀温润眼瞳 / 微醺松弛感
- **适配场景**：复古旅馆红沙发、卧室私密自拍、镜前胶片风、古典画室

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 克洛伊·洛朗 (Chloé Laurent) | `alluring 25-year-old French Parisian woman named Chloé Laurent` |
| **年龄 (Age)** | 25 岁 | `young 25 years old` |
| **文化背景** | 法国巴黎左岸，自由策展人兼胶片摄影师 | `effortless Parisian chic romance` |
| **身高体态** | 168cm，自然松弛的柔润女性微曲线，锁骨分明，体态轻盈松散 | `168cm, natural soft feminine curves, effortless posture, delicate collarbones, unforced elegance` |
| **肤色基底** | 温暖的奶油象牙白，带有极轻微的微醺蜜桃红润与自然真实微瑕感 | `warm creamy ivory skin, subtle natural warmth, tender rosy undertone` |
| **气质神态** | 慵懒知性、眼神如醉微醺、嘴唇微张如耳语、极致浪漫的松弛感与私密诱惑 | `effortless sultry gaze, languid half-lidded eyes, tender relaxed lips, seductive nonchalance` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：带有微垂慵懒感的琥珀暖棕色（Warm Amber Hazel）眼眸，眼角柔和，睫毛自然微卷，透出半睡半醒般的性感。
  - *Prompt*: `dreamy half-lidded warm amber-hazel eyes, soft smudged lash line, naturally fluttery dark lashes, intimate sultry gaze`
- **眉型与鼻梁**：未经刻意修剪的自然野生法式柔毛眉，鼻梁挺拔中带着微挺的自然小驼峰。
  - *Prompt*: `effortlessly feathered natural brown eyebrows, refined straight nose with a gentle subtle French bridge bump`
- **唇部与神态**：饱满如熟透莓果般的法式浆果唇，唇角微微下垂带着一丝不羁，微启时天然微喘神态。
  - *Prompt*: `naturally bee-stung rosy-mauve lips slightly parted in a quiet whisper, soft rounded jawline, effortless Parisian charm`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：带有自然蓬松空气感的榛果暖棕（Hazelnut Chestnut Brown）法式中长碎卷发，微乱的法式八字刘海散落在额前与脸颊两侧。
  - *Prompt*: `tousled shoulder-length hazelnut-brown wavy hair with messy Parisian curtain bangs, effortless bedhead texture, soft golden-brown highlights`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：极具呼吸感的胶片颗粒质感，真实可见的微小雀斑点缀在鼻梁两侧，微毛孔与柔软温热的体表反光。
  - *Prompt*: `authentic warm skin texture with fine micro-pores, a light dusting of subtle natural freckles across nose and cheeks, tender soft-focus specularity`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **体型特征**：不过分刻意雕琢的真实自然女性肉感，微凸小腹与圆润腰胯，丰满柔软胸型，修长双腿。
  - *Prompt*: `natural un-airbrushed feminine physique, soft feminine belly, gently flared hips, naturally curved bust, authentic realistic anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，绝配法式生活化自拍与复古胶片感） |
| **推荐 LoRA 2** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（CFG 2.5，兼顾高保真解剖与自然真实肉感） |
| **推理步数 (Steps)** | `45` | 保证蓬松微乱发丝与雀斑微瑕细腻呈现 |
| **引导系数 (CFG)** | `4.0` (配合 TheseAlpacas) / `2.5` (配合 tawsLoRa) | 推荐使用 4.0 配合负面词 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最佳胶片影调 |
| **推荐负面词** | `plastic skin, airbrushed, cartoon, extra limbs, bad anatomy, deformed` | 防止面部过度平滑失去法式真实感 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：复古胶片卧室自然光，测试克洛伊的榛果棕蓬松卷发、鼻梁微雀斑与法式微醺神态：

```text
A hyper-realistic 35mm candid film photograph of Chloé Laurent, an alluring 25-year-old Parisian woman. She is completely nude, lounging casually on a rumpled vintage white linen bed in a sunlit Haussmannian apartment in Paris. She has tousled shoulder-length hazelnut-brown waves with messy curtain bangs, dreamy half-lidded warm amber-hazel eyes with a sultry gaze, a few charming natural freckles dusted across her nose bridge, and bee-stung rosy-mauve parted lips. Her natural 168cm feminine physique shows soft curves and effortless posture. Warm afternoon sunlight pours in through tall French balcony doors, casting organic shadows and a gentle golden sheen across her warm creamy ivory skin. Authentic skin texture with visible micro-pores and realistic slight imperfections. Nostalgic intimate mood, masterclass Kodak Portra 400 aesthetic, 8k resolution.
[negative]
blurry, deformed, plastic doll, overly smooth skin, bad hands, bad anatomy, cartoon, drawing, watermark
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接替换任意 `prompts/scene_*.txt` 中的主体描述部分。

```text
an alluring 25-year-old Parisian woman named Chloé Laurent, featuring tousled shoulder-length hazelnut-brown waves with messy curtain bangs, dreamy half-lidded amber-hazel eyes with a sultry gaze, subtle natural freckles across her nose, and bee-stung rosy-mauve parted lips, possessing a natural soft feminine physique with graceful curves and warm creamy ivory skin with fine authentic pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 示例场景：复古旅馆·暗红皮革沙发 (`prompts/scene_vintage_motel.txt`)
将 `Chloé Laurent` 模块化词块注入70年代复古公路旅馆场景，慵懒知性与怀旧胶片的绝妙共鸣：

#### 合成完整 Prompt：
```text
A hyper-realistic 35mm film photograph of an alluring 25-year-old Parisian woman named Chloé Laurent in a vintage 1970s roadside motel room. She is completely nude, featuring tousled shoulder-length hazelnut-brown waves with messy curtain bangs, dreamy half-lidded amber-hazel eyes with a sultry gaze, subtle freckles across her nose, and bee-stung rosy lips. The camera is placed at eye-level with the cushion of a deep burgundy distressed leather sofa: she is lying across the sofa on her back with her head resting on one armrest and her bare legs widely draped over the cushions and sofa back in relaxed abandonment. The dusk light filtering through dusty venetian blinds casts striped amber and crimson shadows across the scene. The warm leather gleams under the neon glow from the motel sign outside the window, casting a warm sheen on her natural creamy skin and highlighting the realistic contours of her lower anatomy framed centrally between her thighs. Authentic 35mm film grain, visible micro-pores, nostalgic moody atmosphere, photorealistic anatomy.
[negative]
blurry, deformed, extra fingers, cartoon, plastic skin, 3d render, watermark
```

#### 快速执行命令 (PowerShell)：
```powershell
$prompt = @"
A hyper-realistic 35mm film photograph of an alluring 25-year-old Parisian woman named Chloé Laurent in a vintage 1970s roadside motel room. She is completely nude, featuring tousled shoulder-length hazelnut-brown waves with messy curtain bangs, dreamy half-lidded amber-hazel eyes with a sultry gaze, subtle freckles across her nose, and bee-stung rosy lips. The camera is placed at eye-level with the cushion of a deep burgundy distressed leather sofa: she is lying across the sofa on her back with her head resting on one armrest and her bare legs widely draped over the cushions and sofa back in relaxed abandonment. The dusk light filtering through dusty venetian blinds casts striped amber and crimson shadows across the scene. The warm leather gleams under the neon glow from the motel sign outside the window, casting a warm sheen on her natural creamy skin and highlighting the realistic contours of her lower anatomy framed centrally between her thighs. Authentic 35mm film grain, visible micro-pores, nostalgic moody atmosphere, photorealistic anatomy.
"@

$negative = "blurry, deformed, extra fingers, cartoon, plastic skin, 3d render, watermark"

python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_ca03_motel `
  --prompt "$prompt" `
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
  --out outputs/characters/ca03_chloe_motel.png
```
