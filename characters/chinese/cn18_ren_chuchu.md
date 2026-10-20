# 人物卡：[CN-18] 任楚楚 (Ren Chuchu) - 金庸武侠·绿竹傲娇圣姑

- **卡片编号**：`CN-18`
- **时代分类**：经典金庸武侠 (Classic Jin Yong Wuxia Fiction)
- **原型灵感**：金庸《笑傲江湖》日月神教圣姑任盈盈（融合许晴版经典任盈盈两腮迷人小梨涡、端庄秀丽与傲娇娇蛮并存的绝妙神韵）
- **主打风格**：绿竹巷抚琴圣姑 / 两腮动人甜美小梨涡 / 亦正亦邪傲娇美 / 娇羞含情目 / 秀外慧中极品柔荑
- **适配场景**：幽篁竹林私密水阁 (`prompts/scene_bamboo_courtyard.txt`)、新中式茶室 (`prompts/scene_chinese_tearoom.txt`)、江南水阁临渊 (`prompts/scene_jiangnan_pavilion.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 任楚楚 (Ren Chuchu) | `enchanting spirited 20-year-old Wuxia Holy Maiden named Ren Chuchu` |
| **年龄 (Age)** | 20 岁（风华韶华） | `blooming youth 20 years old` |
| **小说渊源** | 出自金庸名著《笑傲江湖》，魔教圣姑隐居洛阳绿竹巷，琴萧双绝，号令群雄 | `classical Jin Yong Wuxia, Sun Moon Holy Maiden archetype` |
| **身高体态** | 166cm，苗条婀娜、骨肉匀称的侠女体态：盈盈一握的柔软纤腰、秀美端正的削肩、匀称双腿 | `slender lithe maiden frame, graceful sloping shoulders, extraordinarily supple waistline, gentle rounded feminine curves` |
| **肤色基底** | 如羊脂白玉般温润细腻，带着少女特有的自然粉红血色与通透水光 | `translucent warm porcelain fair skin with healthy soft peach-rose bloom` |
| **气质神态** | 端庄端丽中透出一股魔教圣姑的刁蛮傲娇；笑时两腮显出极具杀伤力的迷人小梨涡，娇羞动人 | `tender bashful expression, signature charming cheek dimples when smiling, proud spirited gaze` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：水汪汪的极品含情大杏眼，眼眸清澈明亮如深山古潭，既有少女的娇羞怯弱，又有统领江湖的从容英气。
  - *Prompt*: `luminous expressive dark brown almond eyes with tender bashful gaze, soft curved eyelids, naturally fine long eyelashes`
- **面颊与标志性梨涡**：笑靥如花，双颊在轻笑或娇嗔时各有一处凹陷明显的精致迷人小梨涡，极具亲和力与辨识度。
  - *Prompt*: `signature deep charming dimples appearing prominently on both rosy cheeks when smiling, soft round feminine cheeks, delicate chin`
- **眉型与鼻唇**：秀气修长的青黛细柳叶眉；小巧微翘的琼脂秀鼻；娇艳欲滴的水蜜桃粉唇微嘟。
  - *Prompt*: `fine delicate arched willow eyebrows, straight dainty nose with a cute tip, naturally plump peach-pink lips slightly pouting in playful shyness`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：古典江南侠女双环半挽垂云髻，插以一柄通透翠竹玉簪，其余黑曜石直长发如流泉般垂于腰际。
  - *Prompt*: `waist-length silky smooth straight jet-black hair, half-pinned in an elegant double-loop maiden bun with a carved emerald jade hairpin, glossy soft texture`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：竹林青翠漫射光下的真实微观皮肤，微细毛孔均匀细嫩，锁骨深凹秀美，平坦小腹与柔韧腰肢带有健康的真皮光泽。
  - *Prompt*: `authentic human skin texture with microscopic pores, soft natural subsurface scattering, delicate specular highlight along collarbones and supple waist`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：典型的东方少女黄金比例：弹琴弄萧的修长削葱玉指、轻盈柔韧的柳腰、紧致平坦的小腹与匀称修长的美腿。
  - *Prompt*: `lithe graceful maiden silhouette, slender musician hands, tiny supple waistline, smooth toned abdomen, firm rounded hips, slender thighs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美刻画少女柔美骨骼与真实私密结构） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，强化竹林水光与娇羞写真的氛围感） |
| **推理步数 (Steps)** | `45 - 50` | 保证标志性梨涡与清澈眼神完全收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 柔美清透自然光的最佳平衡 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显侠女灵动身姿与面庞甜美梨涡 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定标志性梨涡与五官神态 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证任楚楚的标志性双颊梨涡、娇羞神态与绿竹圣姑身段：

```text
A hyper-realistic full-body masterwork studio portrait of Ren Chuchu, an enchanting 20-year-old Wuxia Holy Maiden inspired by Jin Yong's Xiao Ao Jiang Hu. She is completely nude, sitting gracefully on a woven bamboo reed mat next to an antique Chinese zither (guqin) against a minimalist dark slate-grey wall with green bamboo leaf shadows. She has waist-length silky jet-black hair with a jade hairpin, luminous dark brown almond eyes with a shy affectionate gaze, cute peach-pink pouting lips, and deep charming dimples visible on both her blushing cheeks. Her body is slender and supple with delicate prominent collarbones, a tiny flexible waistline, and slender musician hands. Soft diffuse daylight illuminates her warm porcelain skin, revealing authentic microscopic pores, natural soft subsurface scattering, and dewy highlights along her spine and thighs. Masterwork, 8k resolution, timeless romantic Wuxia elegance, Hasselblad 80mm portrait photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
an enchanting spirited 20-year-old Wuxia Holy Maiden named Ren Chuchu with waist-length straight silky jet-black hair and jade hairpin, luminous affectionate dark almond eyes, cute peach-pink lips, signature deep charming cheek dimples when smiling, possessing a lithe supple frame with slender musician hands, tiny waist, and warm translucent porcelain skin with authentic fine pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：幽篁竹林私密水阁 (`prompts/scene_bamboo_courtyard.txt`)
将 `Ren Chuchu` 模块化词块嵌入绿竹巷月夜竹影水阁：

#### 合成完整 Prompt：
```text
A hyper-realistic wide-angle cinematic shot of an enchanting spirited 20-year-old Wuxia Holy Maiden named Ren Chuchu with waist-length straight silky jet-black hair and jade hairpin, luminous affectionate dark almond eyes, cute peach-pink lips, signature deep charming cheek dimples when smiling, possessing a lithe supple frame with slender musician hands, tiny waist, and warm translucent porcelain skin with authentic fine pores. She is completely nude, seated in a flexible kneeling arched posture on a smooth dark river-stone terrace in an ancient moonlit courtyard surrounded by towering emerald bamboo stalks. One slender arm is extended touching a mossy rock, her back gracefully arched to highlight her slender spine and feminine curves. Pale cool moonlight filters through the bamboo leaves, casting intricate dancing dappled shadow patterns across her alabaster skin. Subtle water mist rises from a shallow stone reflecting pool in front of her. The low camera angle captures the soft contours of her lower anatomy naturally illuminated by the ambient moonlit water reflections. 8k resolution, atmospheric mist, photorealistic anatomy, cinematic lighting.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn18_ren_chuchu `
  --prompt "A hyper-realistic wide-angle cinematic shot of an enchanting spirited 20-year-old Wuxia Holy Maiden named Ren Chuchu with waist-length straight silky jet-black hair and jade hairpin, luminous affectionate dark almond eyes, cute peach-pink lips, signature deep charming cheek dimples when smiling, possessing a lithe supple frame with slender musician hands, tiny waist, and warm translucent porcelain skin with authentic fine pores. She is completely nude, seated in a flexible kneeling arched posture on a smooth dark river-stone terrace in an ancient moonlit courtyard surrounded by towering emerald bamboo stalks. One slender arm is extended touching a mossy rock, her back gracefully arched to highlight her slender spine and feminine curves. Pale cool moonlight filters through the bamboo leaves, casting intricate dancing dappled shadow patterns across her alabaster skin. Subtle water mist rises from a shallow stone reflecting pool in front of her. The low camera angle captures the soft contours of her lower anatomy naturally illuminated by the ambient moonlit water reflections. 8k resolution, atmospheric mist, photorealistic anatomy, cinematic lighting." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn18_ren_chuchu_bamboo.png
```
