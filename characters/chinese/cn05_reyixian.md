# 人物卡：[CN-05] 热依仙 (Reyixian) - 现代顶流·明艳绝代浓颜

- **卡片编号**：`CN-05`
- **时代分类**：现代明艳顶流 (Modern Glamour Peak)
- **原型灵感**：迪丽热巴 (Dilraba) 顶级浓颜明艳神颜神韵
- **主打风格**：异域神颜 / 欧亚深邃大五官 / 高挺驼峰琼鼻 / 人间富贵花 / 极致腰臀比尤物
- **适配场景**：奢华游艇日光浴 (`prompts/scene_yacht_sunbathing.txt`)、午夜奢华厨房 (`prompts/scene_midnight_kitchen.txt`)、落地窗晨曦伸展 (`prompts/scene_penthouse_stretch.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 热依仙 (Reyixian) | `stunning 24-year-old Chinese celebrity actress named Reyixian` |
| **年龄 (Age)** | 24 岁 | `radiant 24 years old` |
| **职业与身份** | 现代华语顶流天花板女演员，以立体浓颜与红毯艳绝全场著称 | `top celebrity movie star, glamorous modern Chinese icon` |
| **身高体态** | 169cm，凹凸有致的极致S型身材：饱满酥胸、盈盈细腰、饱满挺翘蜜桃臀 | `slender yet intensely voluptuous hourglass silhouette, narrow waist, rounded full hips, long shapely legs` |
| **肤色基底** | 如羊脂白雪般冷白无暇，红润透光，极具视觉冲击力 | `dazzling alabaster snow-white fair skin, luminous dewy glow` |
| **气质神态** | 明艳夺目、天生尤物、狐系灵动眼神，兼具少女的纯净与熟女的极致妩媚 | `mesmerizing intense glamour, expressive doe-eyed allure, radiant confident smile` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：极其深邃的欧式平行大双眼皮，潋滟桃花鹿眼，睫毛浓密如扇，眼角泪痣更添艳色。
  - *Prompt*: `deeply set huge expressive dark brown almond eyes with dramatic double eyelids, long curled thick eyelashes, tiny alluring beauty mark below her left eye corner, sparkling passionate gaze`
- **鼻型与立体度**：立体高挺的驼峰玉鼻，山根高拔，鼻尖微翘精致，面部纵深折叠度极高。
  - *Prompt*: `tall aristocratic straight nose bridge with a subtle elegant dorsal hump, perfectly contoured refined nasal tip`
- **唇型与面颊**：饱满的花瓣肉感唇，上唇唇珠明显，天然蜜桃红润；面颊饱满紧致，轮廓明艳无死角。
  - *Prompt*: `full plump rose-pink lips with glossy sheen, slightly parted showcasing white straight teeth, flawless v-shaped jawline, radiant sculpted cheeks`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：丰盈蓬松的海藻大波浪黑色长卷发，侧分披散于肩颈与胸前，发丝丝滑光泽跃动。
  - *Prompt*: `luxurious voluminous cascading deep-wave jet-black long hair, swept over one shoulder, catching soft cinematic specular highlights`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：如剥壳水煮蛋般晶莹剔透，高清镜头下保留着真实的微观毛孔与皮肤绒毛感，锁骨与双峰带有水润光泽。
  - *Prompt*: `authentic high-definition human skin with micro-pores and delicate peach fuzz, dewy moisture sheen over collarbones and decolletage, natural subsurface scattering`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：极度夸张的腰臀比（WHR 约 0.68）：纤细紧致的腹部无一丝赘肉，饱满挺拔的胸部与圆润高翘的臀线，双腿白皙修长。
  - *Prompt*: `breathtaking hourglass curves, narrow tight waistline with soft natural navel, full voluptuous bust, rounded shapely hips, long smooth thighs, genuine feminine anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.85`（搭配 CFG 4.0，顶级明星私密写真质感与立体大五官表现） |
| **推荐 LoRA 2** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `0.95`（搭配 CFG 2.5，极致精准的解剖学与水润真实皮肤） |
| **推理步数 (Steps)** | `45 - 50` | 保证大波浪长发发丝细节与立体五官完全收敛 |
| **引导系数 (CFG)** | `4.0` (TheseAlpacas) / `2.5` (tawsLoRa) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最佳质感与柔光漫射组合 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显饱满体态与红毯级绝艳容颜 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定浓颜神态与高挺鼻梁 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证热依仙的欧亚浓颜神颜、高挺驼峰琼鼻与极致沙漏身材：

```text
A hyper-realistic full-body fashion studio photograph of Reyixian, a stunning 24-year-old Chinese celebrity star with breathtaking exotic facial features. She is completely nude, posing in an alluring standing contrapposto posture against a clean warm cream plaster studio wall. She has cascading voluminous deep-wave black hair falling over her shoulders, huge deeply-set almond dark eyes with a tiny beauty mark under her eye, a tall aristocratic straight nose with a subtle dorsal hump, and luscious plump rose lips slightly parted. Her silhouette is an intensely curvaceous hourglass with a tiny waist, generous natural bust, and rounded feminine hips. Soft cinematic warm beauty-dish lighting sculpts her facial contours and curves, revealing microscopic pores, natural subsurface scattering, and subtle specular glow along her collarbones and hips. Masterwork, 8k resolution, Hasselblad 100mm portrait photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a stunning 24-year-old Chinese celebrity actress named Reyixian with voluminous cascading wavy black hair, huge expressive dark doe eyes with a tiny beauty mark, tall aristocratic straight nose with subtle dorsal hump, luscious plump lips slightly parted, possessing a breathtaking hourglass frame with narrow waist, full feminine curves, and glowing alabaster white skin with authentic micro-pores and dewy sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：奢华游艇日光浴甲板 (`prompts/scene_yacht_sunbathing.txt`)
将 `Reyixian` 模块化词块嵌入落日余晖下的奢华游艇甲板：

#### 合成完整 Prompt：
```text
A hyper-realistic, overhead high-angle photograph of a stunning 24-year-old Chinese celebrity actress named Reyixian with voluminous cascading wavy black hair, huge expressive dark doe eyes with a tiny beauty mark, tall aristocratic straight nose with subtle dorsal hump, luscious plump lips slightly parted, possessing a breathtaking hourglass frame with narrow waist, full feminine curves, and glowing alabaster white skin with authentic micro-pores and dewy sheen. She is completely nude, lying on her back on an ivory-white sun lounger on the teak deck of a luxury superyacht floating on turquoise Mediterranean waters. Her body is stretched luxuriously under the warm sun, one arm resting over her forehead casting a soft shadow across her closed eyes, while the other hand rests beside her hip. Her legs are slightly bent and parted, soaking up the sea breeze. Glistening droplets of seawater and tanning oil shimmer across her collarbones, flat abdomen, and thighs. Golden afternoon sunlight creates rich highlights and deep shadows across the teak decking. The high angle looks down across the length of her body, framing her complete figure and lower anatomy in clear, natural detail. 8k resolution, sun-drenched coastal atmosphere, crisp water textures.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn05_reyixian `
  --prompt "A hyper-realistic, overhead high-angle photograph of a stunning 24-year-old Chinese celebrity actress named Reyixian with voluminous cascading wavy black hair, huge expressive dark doe eyes with a tiny beauty mark, tall aristocratic straight nose with subtle dorsal hump, luscious plump lips slightly parted, possessing a breathtaking hourglass frame with narrow waist, full feminine curves, and glowing alabaster white skin with authentic micro-pores and dewy sheen. She is completely nude, lying on her back on an ivory-white sun lounger on the teak deck of a luxury superyacht floating on turquoise Mediterranean waters. Her body is stretched luxuriously under the warm sun, one arm resting over her forehead casting a soft shadow across her closed eyes, while the other hand rests beside her hip. Her legs are slightly bent and parted, soaking up the sea breeze. Glistening droplets of seawater and tanning oil shimmer across her collarbones, flat abdomen, and thighs. Golden afternoon sunlight creates rich highlights and deep shadows across the teak decking. The high angle looks down across the length of her body, framing her complete figure and lower anatomy in clear, natural detail. 8k resolution, sun-drenched coastal atmosphere, crisp water textures." `
  --seed 80964 `
  --steps 45 `
  --cfg 4.0 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "thesealpacas-nsfw-v2.safetensors" `
  --lora-strength 0.85 `
  --negative "blurry, deformed, bad anatomy, bad hands, plastic skin, oversaturated" `
  --out outputs/characters/cn05_reyixian_yacht.png
```
