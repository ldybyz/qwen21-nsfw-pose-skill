# 人物卡：[CN-03] 白曼清 (Bai Manqing) - 民国海派·旗袍风情名伶

- **卡片编号**：`CN-03`
- **时代分类**：近代民国 (1930s Republic of China / Old Shanghai)
- **原型灵感**：张曼玉（《花样年华》苏丽珍旗袍神韵）+ 汤唯（《色戒》王佳芝六角脸高级韵味）
- **主打风格**：老上海海派名媛 / 复古手推波浪卷 / 细眉红唇 / 旗袍架子S曲线 / 电影王家卫微醺抽离感
- **适配场景**：旗袍名媛暗光酒廊 (`prompts/scene_qipao_lounge.txt`)、复古旅馆卧室 (`prompts/scene_vintage_motel.txt`)、镜前微醺自拍 (`prompts/scene_mirror_selfie.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 白曼清 (Bai Manqing) | `enigmatic glamorous 26-year-old 1930s Shanghai socialite named Bai Manqing` |
| **年龄 (Age)** | 26 岁 | `alluring 26 years old` |
| **时代与身份** | 1930年代民国上海滩名媛与电影名伶，十里洋场绝代佳人 | `1930s Republican Old Shanghai vintage cinematic aesthetic` |
| **身高体态** | 170cm，天生旗袍衣架子：高挑纤长天鹅颈、骨肉停匀S型沙漏轮廓、纤腰翘臀 | `tall slender 170cm frame, long elegant swan neck, pronounced feminine hourglass curves, graceful arched back` |
| **肤色基底** | 暖调象牙白，带有老式胶片滤镜下的温润光晕与细腻纹理 | `warm ivory skin with smooth velvety cinematic glow, natural subtle undertones` |
| **气质神态** | 微醺、慵懒、清冷疏离中透着刺骨的风情，眼波流转带有一丝烟视媚行的故事感 | `melancholic sultry gaze, enigmatic subtle half-smile, smoke-kissed vintage allure` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：眼尾略长、微微上挑的东方丹凤眼，睫毛纤长如墨，眼底带着淡淡的倦意与迷离泪光。
  - *Prompt*: `elongated sultry dark almond-phoenix eyes with subtle smoky vintage eyeliner, long dark mascara eyelashes, melancholic yet intensely captivating gaze`
- **眉型与鼻梁**：极具30年代海派特征的细长柳叶远山眉；鼻梁挺直小巧，山根线条优美流畅。
  - *Prompt*: `fine delicate pencil-thin arched vintage eyebrows, straight aristocratic slender nose bridge`
- **唇型与神态**：复古哑光深红/枫糖红复古唇，唇角微扬带有一丝若即若离的嘲讽与诱惑，嘴角缀有一颗极小浅淡美人痣。
  - *Prompt*: `deep matte retro crimson red lips slightly parted, defined Cupid's bow, tiny subtle beauty mark near the corner of her lower lip, high refined cheekbones`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：1930年代标志性的民国手推波浪贴鬓卷发（Vintage Finger Waves），盘于脑后成精致发髻，几缕微卷发丝散落在雪白耳际。
  - *Prompt*: `sculpted 1930s retro finger-wave bob hairstyle framing her face with glossy undulating waves, gathered into a low neat vintage chignon, jet-black glossy hair`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：如丝绒般温润的真实体表微毛孔质感，锁骨深凹如刀刻，胸前与腰腹带有老胶片光影下的柔和光晕，无假面塑料感。
  - *Prompt*: `authentic textured human skin with visible microscopic pores, soft velvety subsurface scattering, warm cinematic specular sheen highlighting her collarbones, ribs, and curved hips`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：典型的东方旗袍黄金比例：极具张力的纤细蜂腰、圆润丰满的臀部曲线、修长笔直的东方小腿、手腕处佩戴一只碧绿翡翠玉镯。
  - *Prompt*: `classic oriental hourglass silhouette, ultra-slender waist, curvaceous rounded hips, long slender toned legs, prominent collarbones, a single translucent emerald jade bangle on her slender wrist, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.85`（搭配 CFG 4.0，老上海胶片氛围与私密复古质感天花板） |
| **推荐 LoRA 2** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `0.9`（搭配 CFG 2.5，兼顾旗袍脱卸后精准真实的私密解剖） |
| **推理步数 (Steps)** | `45 - 50` | 保证手推波浪发丝质感与胶片暖调收敛完全 |
| **引导系数 (CFG)** | `4.0` (推荐配 TheseAlpacas 胶片感) 或 `2.5` | 依 LoRA 选定 |
| **采样器 / 调度器** | `er_sde` / `beta` | 营造电影级低调光影（Low-key Lighting） |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显天鹅颈与S型侧身曲线 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定经典王家卫色调 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证白曼清的民国手推波浪发、细眉红唇与胶片光影下的天鹅颈与身材曲线：

```text
A hyper-realistic full-body cinematic portrait of Bai Manqing, an enigmatic 26-year-old 1930s Shanghai socialite. She is completely nude, posing in a sultry contrapposto side-profile stance against a textured aged velvet emerald wallpaper. She has glossy sculpted 1930s finger-wave hair, delicate fine arched eyebrows, captivating smoky almond eyes with a melancholic gaze, deep matte crimson red lips slightly parted, and an emerald jade bangle on her wrist. Her frame is tall and slender with a long swan neck, prominent collarbones, a tiny waistline, and curvaceous rounded hips. Moody dramatic amber side-lighting from a vintage art-deco tungsten lamp sculpts her silhouette, casting warm highlights over her authentic skin texture with microscopic pores and soft natural shadows along her spine. 8k resolution, Wong Kar-wai film aesthetic, Kodak 35mm grain, masterwork photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
an enigmatic 26-year-old 1930s Shanghai socialite named Bai Manqing with sculpted retro finger-wave hair, fine delicate arched eyebrows, smoky melancholic almond eyes, deep matte crimson lips slightly parted, a translucent emerald jade bangle on her wrist, possessing a slender hourglass frame with a long swan neck, tiny waist, curvaceous hips, and warm velvety ivory skin with authentic micro-pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：旗袍名媛暗光酒廊 (`prompts/scene_qipao_lounge.txt`)
将 `Bai Manqing` 模块化词块嵌入昏暗红丝绒老上海酒廊：

#### 合成完整 Prompt：
```text
A hyper-realistic, medium full-body photograph of an enigmatic 26-year-old 1930s Shanghai socialite named Bai Manqing with sculpted retro finger-wave hair, fine delicate arched eyebrows, smoky melancholic almond eyes, deep matte crimson lips slightly parted, a translucent emerald jade bangle on her wrist, possessing a slender hourglass frame with a long swan neck, tiny waist, curvaceous hips, and warm velvety ivory skin with authentic micro-pores. She is completely nude, sitting sideways on a deep-crimson velvet armchair inside a dimly lit, smoky private speakeasy lounge. One long leg is crossed over the other, her torso turned slightly towards the viewer while her hand rests on the polished mahogany armrest next to an antique cocktail glass. In the dark background, warm amber light glints off art-deco brass wall fixtures, textured emerald-green wallpaper, and heavy velvet drapery. A single dramatic spotlight cuts through the light haze, catching the curves of her shoulders, bare breasts, and thighs. The angle captures the detailed anatomy of her thighs and pelvic region in shadow and warm specular glow. 8k resolution, cinematic moody lighting, rich vintage film colors.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn03_bai_manqing `
  --prompt "A hyper-realistic, medium full-body photograph of an enigmatic 26-year-old 1930s Shanghai socialite named Bai Manqing with sculpted retro finger-wave hair, fine delicate arched eyebrows, smoky melancholic almond eyes, deep matte crimson lips slightly parted, a translucent emerald jade bangle on her wrist, possessing a slender hourglass frame with a long swan neck, tiny waist, curvaceous hips, and warm velvety ivory skin with authentic micro-pores. She is completely nude, sitting sideways on a deep-crimson velvet armchair inside a dimly lit, smoky private speakeasy lounge. One long leg is crossed over the other, her torso turned slightly towards the viewer while her hand rests on the polished mahogany armrest next to an antique cocktail glass. In the dark background, warm amber light glints off art-deco brass wall fixtures, textured emerald-green wallpaper, and heavy velvet drapery. A single dramatic spotlight cuts through the light haze, catching the curves of her shoulders, bare breasts, and thighs. The angle captures the detailed anatomy of her thighs and pelvic region in shadow and warm specular glow. 8k resolution, cinematic moody lighting, rich vintage film colors." `
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
  --out outputs/characters/cn03_bai_manqing_lounge.png
```
