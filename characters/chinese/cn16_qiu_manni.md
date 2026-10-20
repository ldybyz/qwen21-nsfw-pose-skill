# 人物卡：[CN-16] 邱曼妮 (Qiu Manni) - 90s港风·美艳尤物红衣大波浪

- **卡片编号**：`CN-16`
- **时代分类**：90年代黄金港风 (1990s Golden Age Hong Kong Cinema)
- **原型灵感**：邱淑贞（《赌神2》经典红衣叼扑克牌纯欲尤物）+ 关之琳（绝代港风第一浓颜美人神韵）
- **主打风格**：港风大波浪卷发 / 烈焰红唇 / 猫系灵动圆杏眼 / 小骨架大胸蜂腰蜜桃臀 / 黄金年代电影胶片质感
- **适配场景**：复古汽车旅馆套房 (`prompts/scene_vintage_motel.txt`)、旗袍名媛暗光酒廊 (`prompts/scene_qipao_lounge.txt`)、午夜奢华厨房 (`prompts/scene_midnight_kitchen.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 邱曼妮 (Qiu Manni) | `alluring iconic 24-year-old 1990s Hong Kong cinema bombshell named Qiu Manni` |
| **年龄 (Age)** | 24 岁 | `sultry 24 years old` |
| **时代与身份** | 90年代香港电影黄金时期倾国倾城的银幕女神，风华绝代第一尤物 | `1990s Golden Era Hong Kong movie star, vintage retro glam aesthetic` |
| **身高体态** | 166cm，娇小骨架但曲线极其火辣爆棚：极细水蛇腰、丰盈饱满天然双峰、挺翘蜜桃臀 | `petite bone frame with hyper-curvaceous hourglass proportions, generous natural bust, tiny wasp waist, rounded hips` |
| **肤色基底** | 暖调象牙白，带有90年代柯达电影胶片特有的细腻暖光与微颗粒油画感 | `warm cream porcelain skin with rich vintage film luster and subtle peachy undertone` |
| **气质神态** | 天真娇憨与极致性感无缝切换，猫系狡黠眼波，唇角微挑，又纯又欲颠倒众生 | `playful feline charm, sultry coquettish gaze, intoxicating confident smile` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：标志性猫系大圆杏眼，眼尾微翘，长睫浓密如墨，眸底闪烁着灵动的小野猫般狡黠与性感。
  - *Prompt*: `large expressive feline almond eyes with playful upturned outer corners, thick black mascara lashes, sparkling mischievous yet sultry gaze`
- **眉型与鼻梁**：复古自然的深黑浓郁微弧拱形眉；小巧高挺的欧式水滴琼鼻。
  - *Prompt*: `naturally thick softly-arched dark eyebrows, cute aristocratic straight nose with refined rounded tip`
- **唇型与面颊**：标志性港风烈焰深红哑光丰唇，唇峰分明，贝齿微露；精致的小巴掌脸配微嘟苹果肌。
  - *Prompt*: `iconic bold retro matte crimson red lips slightly parted revealing white teeth, youthful rounded apple cheeks, delicate pointed chin`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：90年代标志性极致蓬松浓密的海藻黑长大波浪卷发，侧分高颅顶，发丝如黑色云雾般翻滚散落于香肩前胸。
  - *Prompt*: `signature 1990s ultra-voluminous cascading wavy black hair with wild soft curls, swept over one shoulder framing her face, glossy jet-black texture`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：老胶片光晕下的真实皮肤质感，微毛孔清晰细腻，锁骨深凹，双峰饱满弧度在钨丝灯下呈现暖金油画光泽。
  - *Prompt*: `authentic human skin texture with microscopic pores, warm tungsten cinematic specular sheen highlighting deep collarbones and voluptuous curves, natural soft skin texture`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：极度抓人眼球的性感沙漏比例：纤细紧致的腹部（小腹微凹平坦）、丰满挺拔的天然胸型、圆润挺翘的臀腿线条。
  - *Prompt*: `explosive feminine hourglass silhouette, narrow flexible waistline, generous plump bosom, curvaceous hips, long smooth legs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.85`（搭配 CFG 4.0，90年代港片复古胶片感与私密尤物张力天花板） |
| **推荐 LoRA 2** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（搭配 CFG 2.5，极致精准刻画丰满肉感与解剖细节） |
| **推理步数 (Steps)** | `45 - 50` | 保证蓬松大波浪卷发与红唇光影完全收敛 |
| **引导系数 (CFG)** | `4.0` (TheseAlpacas 胶片首选) / `2.5` | 依 LoRA 选定 |
| **采样器 / 调度器** | `er_sde` / `beta` | 营造复古电影暖调高对比度 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显港片大女主火辣身段 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定港风大美人五官 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证邱曼妮的90年代港风大波浪、烈焰红唇与小骨架大胸蜂腰身材：

```text
A hyper-realistic full-body cinematic portrait of Qiu Manni, an iconic 24-year-old 1990s Hong Kong movie goddess. She is completely nude, posing in a playful, confident contrapposto posture against a deep crimson velvet backdrop inside a dimly lit retro studio. She has wildly voluminous cascading deep-wave black hair with high volume, large expressive feline dark eyes with a teasing sultry gaze, bold matte crimson red lips slightly parted showing white teeth, and youthful flushed cheeks. Her frame is an explosive hourglass with a tiny waistline, generous natural bust, and rounded hips. Moody dramatic warm tungsten side-lighting sculpts her silhouette, casting rich golden highlights over her authentic skin texture with microscopic pores and soft natural shadows along her spine. 8k resolution, 1990s Hong Kong cinema aesthetic, Kodak 35mm film grain, masterwork photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
an iconic 24-year-old 1990s Hong Kong cinema bombshell named Qiu Manni with ultra-voluminous wild cascading wavy black hair, large expressive feline dark eyes, bold matte crimson red lips slightly parted, possessing an explosive curvaceous hourglass frame with narrow waist, generous natural bust, rounded hips, and warm creamy porcelain skin with authentic micro-pores and golden cinematic sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：复古汽车旅馆套房 (`prompts/scene_vintage_motel.txt`)
将 `Qiu Manni` 模块化词块嵌入充满故事感的复古汽车旅馆：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle photograph of an iconic 24-year-old 1990s Hong Kong cinema bombshell named Qiu Manni with ultra-voluminous wild cascading wavy black hair, large expressive feline dark eyes, bold matte crimson red lips slightly parted, possessing an explosive curvaceous hourglass frame with narrow waist, generous natural bust, rounded hips, and warm creamy porcelain skin with authentic micro-pores and golden cinematic sheen in a retro 1970s roadside motel bedroom. The camera is placed low near the carpet looking upward toward the corner of a low queen bed covered with a faded mustard-yellow floral bedspread. She is completely nude, sitting sideways on the edge of the mattress, leaning back on both palms with her legs bent and casually spread, gazing directly down at the lens with a confident, sleepy half-smile. A warm neon sign from outside the window casts alternating streaks of saturated red and cyan light across her skin, highlighting the curves of her breasts, ribs, and thighs. In the background are wood-paneled walls, an analog rotary phone on the nightstand, and heavy textured curtains. Natural human skin texture with realistic micro-pores, authentic female anatomy. 8k resolution, gritty cinematic vintage film grain.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn16_qiu_manni `
  --prompt "A hyper-realistic, low-angle photograph of an iconic 24-year-old 1990s Hong Kong cinema bombshell named Qiu Manni with ultra-voluminous wild cascading wavy black hair, large expressive feline dark eyes, bold matte crimson red lips slightly parted, possessing an explosive curvaceous hourglass frame with narrow waist, generous natural bust, rounded hips, and warm creamy porcelain skin with authentic micro-pores and golden cinematic sheen in a retro 1970s roadside motel bedroom. The camera is placed low near the carpet looking upward toward the corner of a low queen bed covered with a faded mustard-yellow floral bedspread. She is completely nude, sitting sideways on the edge of the mattress, leaning back on both palms with her legs bent and casually spread, gazing directly down at the lens with a confident, sleepy half-smile. A warm neon sign from outside the window casts alternating streaks of saturated red and cyan light across her skin, highlighting the curves of her breasts, ribs, and thighs. In the background are wood-paneled walls, an analog rotary phone on the nightstand, and heavy textured curtains. Natural human skin texture with realistic micro-pores, authentic female anatomy. 8k resolution, gritty cinematic vintage film grain." `
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
  --out outputs/characters/cn16_qiu_manni_motel.png
```
