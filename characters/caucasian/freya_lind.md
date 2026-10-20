# 人物卡：芙蕾雅·林德 (Freya Lind) - 北欧极光白金仙气仙女

- **卡片编号**：`CA-01`
- **人物归属**：欧美高加索系 (Caucasian / 北欧斯堪的纳维亚)
- **主打风格**：极光白金长发 / 冰透冷白皮 / 冰蓝色深邃眼瞳 / 雕塑级挺拔骨相
- **适配场景**：芬兰桑拿、潮汐海蚀礁石、古典画室人体、奢华游艇

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 芙蕾雅·林德 (Freya Lind) | `ethereal 24-year-old Scandinavian woman named Freya Lind` |
| **年龄 (Age)** | 24 岁 | `young 24 years old` |
| **文化背景** | 瑞典斯德哥尔摩，现代北欧雕塑模特与极简主义艺术家 | `Nordic Scandinavian aesthetic heritage` |
| **身高体态** | 178cm，挺拔优雅的维京雕塑身姿，纤长天鹅颈与直角肩，无瑕黄金分割线条 | `tall 178cm, statuesque Nordic physique, long swan neck, athletic square shoulders, sculpted long limbs` |
| **肤色基底** | 冰雪般极净的冷白透光皮（Alabaster Pale），薄皮下透出极淡天然青蓝色微血管反光 | `ultra-fair alabaster pale skin, cool translucent undertone, pristine porcelain tone` |
| **气质神态** | 空灵不食人间烟火、仙气冷漠、眼神如极地浮冰般清澈澄净 | `ethereal otherworldly gaze, glacial serenity, subtle mysterious half-smile, Nordic fairy elegance` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：澄澈幽邃的冰蓝色（Ice-Blue）大双眼皮，虹膜如极地冰川，细密修长的淡白金色睫毛。
  - *Prompt*: `piercing glacial ice-blue eyes with luminous crystalline irises, platinum-blonde delicate eyelashes, distant ethereal gaze`
- **眉型与鼻骨**：浅金灰自然羽状弓眉，希腊雕塑般高挺平直的窄鼻梁。
  - *Prompt*: `naturally arched platinum-ash eyebrows, high straight aristocratic Greek nose bridge with sharp refined profile`
- **唇型与轮廓**：饱满柔嫩的淡樱粉色双唇，天然微翘的丘比特之弓，面部骨相立体清晰，下颌缘线条紧致如刀刻。
  - *Prompt*: `soft naturally frosted pale-pink lips slightly parted, crisp Cupid's bow, high sculpted Scandinavian cheekbones and elegant tapered chin`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：飘逸及腰的极光白金微波长发（Platinum Icy Blonde），发丝在光线下泛着纯银反光，发丝极细柔顺。
  - *Prompt*: `waist-length flowing platinum icy-blonde wavy hair with shimmering silver highlights, silk-like texture catching rim light`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：极细腻的北欧冷白表皮，微小自然毛孔，肩膀与锁骨微光闪烁，背光时带有柔和的半透明皮下散射效应（Subsurface Scattering）。
  - *Prompt*: `pristine alabaster skin texture with realistic fine pores, delicate subsurface scattering along ears and fingers, subtle icy sheen on collarbones`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **体型特征**：高挑修长，优美的背脊沟，紧致平坦的小腹，纤长饱满的腿部线条与挺拔胸线。
  - *Prompt*: `tall statuesque silhouette, defined spinal furrow, firm naturally lifted bust, taut waist, slender muscular thighs, authentic classical anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（高反差冷光、完美高挑骨骼解剖还原） |
| **推荐 LoRA 2** | `nsfw-posture-v3.safetensors` | 权重 `0.85`（强力拉满雕塑级形体与姿态张力） |
| **推理步数 (Steps)** | `45 - 50` | 保证白金发丝与冷白皮肤反光无噪点 |
| **引导系数 (CFG)** | `2.5` | 极佳的柔和高动态范围 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最精准的亮部细节解析 |
| **生图分辨率** | `1152x1728` | 高挑人像黄金分辨率 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：纯净北欧天窗冷光影棚，测试芙蕾雅的白金卷发、冰蓝眼眸与雕塑骨相：

```text
A hyper-realistic full-body fine-art photograph of Freya Lind, an ethereal 24-year-old Scandinavian woman with breathtaking Nordic beauty. She is completely nude, standing tall in a classical contrapposto pose against a minimalist raw concrete wall inside a sunlit Stockholm loft. She has waist-length flowing platinum icy-blonde wavy hair catching silver rim lighting, piercing glacial ice-blue eyes with an otherworldly serene gaze, an aristocratic straight nose, and frosted pale-pink parted lips. Her tall 178cm statuesque frame displays long slender limbs, sharp elegant collarbones, and firm natural curves. Pure cool daylight pours down from a large frosted skylight above, casting delicate shadows along her defined cheekbones, spinal furrow, and long toned legs, highlighting authentic alabaster pale skin with micro-pores and realistic subcutaneous translucence. Authentic photorealistic anatomy, minimalist Scandinavian fine art, 8k resolution, Hasselblad 100mm lens.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接替换任意 `prompts/scene_*.txt` 中的主体描述部分。

```text
an ethereal 24-year-old Scandinavian woman named Freya Lind, featuring waist-length flowing platinum icy-blonde hair with silver sheen, piercing glacial ice-blue eyes with distant serene gaze, an aristocratic straight nose, and soft frosted pale-pink parted lips, with a tall 178cm statuesque Nordic physique, high sculpted cheekbones, elegant collarbones, and ultra-fair alabaster pale skin with natural fine pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 示例场景：芬兰桑拿·原木蒸汽 (`prompts/scene_sauna_steam.txt`)
将 `Freya Lind` 模块化词块注入芬兰原木桑拿房，热气与极光白金美人的极致温差碰撞：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle photograph of an ethereal 24-year-old Scandinavian woman named Freya Lind inside a traditional Finnish cedarwood sauna. She is completely nude, featuring waist-length flowing platinum icy-blonde waves damp with condensation, piercing glacial ice-blue eyes, flushed parted lips, and a tall 178cm statuesque Nordic physique with sculpted curves. The camera captures her from a medium-low upward angle seated comfortably on the upper tier cedar bench: she leans slightly back supporting her weight with hands resting on the smooth wood behind her, knees opened naturally in deep relaxation. Heavy clouds of white cedar steam swirl around her from hot stones, wrapping her silhouette in gentle mist. Authentic glistening droplets of sweat and water condensation trail across her flushed alabaster pale skin, catching amber under-bench LED lighting along her collarbones, toned stomach, and inner thighs centered naturally in the frame. Authentic skin pores, wet hair clinging to bare shoulders. 8k resolution, photorealistic anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_ca01_sauna `
  --prompt "A hyper-realistic, low-angle photograph of an ethereal 24-year-old Scandinavian woman named Freya Lind inside a traditional Finnish cedarwood sauna. She is completely nude, featuring waist-length flowing platinum icy-blonde waves damp with condensation, piercing glacial ice-blue eyes, flushed parted lips, and a tall 178cm statuesque Nordic physique with sculpted curves. The camera captures her from a medium-low upward angle seated comfortably on the upper tier cedar bench: she leans slightly back supporting her weight with hands resting on the smooth wood behind her, knees opened naturally in deep relaxation. Heavy clouds of white cedar steam swirl around her from hot stones, wrapping her silhouette in gentle mist. Authentic glistening droplets of sweat and water condensation trail across her flushed alabaster pale skin, catching amber under-bench LED lighting along her collarbones, toned stomach, and inner thighs centered naturally in the frame. Authentic skin pores, wet hair clinging to bare shoulders. 8k resolution, photorealistic anatomy." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/ca01_freya_sauna.png
```
