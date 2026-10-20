# 人物卡：加藤樱 (Sakura Kato) - 日系元气透明感美少女

- **卡片编号**：`EA-03`
- **人物归属**：东亚系 (East Asian / 日系纯欲)
- **主打风格**：透明感水光肌 / 纯欲元气 / 胶原蛋白幼态脸 / 柔软轻盈曲线
- **适配场景**：私汤温泉、复古旅馆、日系榻榻米、拍立得胶片自拍

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 加藤 樱 (Sakura Kato / かとう さくら) | `adorable 20-year-old Japanese young woman named Sakura Kato` |
| **年龄 (Age)** | 20 岁 | `young 20 years old` |
| **文化背景** | 日本东京，大学艺术系学生，兼职透明感写真模特 | `Japanese youthful natural aesthetic` |
| **身高体态** | 160cm，娇小柔软玲珑体态，饱满蜜桃曲线与纤柔四肢 | `petite 160cm, soft supple feminine curves, delicate waist, natural youthful proportions` |
| **肤色基底** | 通透透粉的白皙蜜桃肌，胶原蛋白饱满，水润光泽 | `translucent dewy fair skin with a natural soft peach-pink flush on cheeks and shoulders` |
| **气质神态** | 娇憨清纯、纯欲无辜、微张小嘴、眼神湿漉漉带灵气 | `innocent yet subtly alluring expression, wide curious brown eyes, glossy parted lips, youthful radiant charm` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：微垂的大鹿眼（小狗眼），圆润清澈，深琥珀蜜糖色瞳孔，带有可爱的卧蚕。
  - *Prompt*: `large round doe-like honey-amber eyes with subtle aegyo sal under eyes, soft naturally curled eyelashes, innocent glistening gaze`
- **眉型与鼻骨**：柔和自然的浅棕雾面自然眉，鼻梁小巧微翘，鼻尖圆润精致。
  - *Prompt*: `soft natural light-brown feathered eyebrows, cute small button nose with a soft delicate tip`
- **唇型与颊红**：果冻般水润的草莓粉唇，微张露出整齐皓齿一角，双颊自带天然粉嫩微醺血色感。
  - *Prompt*: `plump juicy glossy strawberry-pink lips slightly parted, soft rounded youthful jawline, adorable blush across cheeks and nose bridge`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：齐锁骨微卷亚麻栗棕色（Milk Tea Chestnut）中长发，带有轻盈日系空气刘海与略微蓬松的空气感碎发。
  - *Prompt*: `shoulder-length wavy chestnut-brown hair with soft airy see-through bangs, effortless wispy tendrils framing her cute round face, sunlit golden highlights`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：如剥壳鸡蛋般富有弹性饱满的胶原蛋白质感，微汗或水汽中呈现天然清透水光感，无妆感微观真毛孔。
  - *Prompt*: `super-fine youthful skin texture with realistic micro-pores, dewy water-like sheen, subtle peach fuzz catching backlighting, tender youthful glow`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **体型特征**：小骨架柔美身材，圆润匀称的胸型与臀线，小腹平坦柔软，双腿纤细白皙。
  - *Prompt*: `petite soft natural feminine contours, delicate collarbones, smooth flat tummy, slender thighs, authentic natural anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（极佳的日系私密质感与真实皮肤光泽） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，特别适合拍立得胶片与自拍纯欲风） |
| **推理步数 (Steps)** | `45` | 保证空气刘海与水光水汽完全解析 |
| **引导系数 (CFG)** | `2.5` (搭配 tawsLoRa) / `4.0` (搭配 TheseAlpacas) | 视 LoRA 选择 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最佳质感与漫反射平衡 |
| **生图分辨率** | `1152x1728` | 竖构图人像特写与全身兼备 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：日系窗边午后柔光写真，测试加藤樱的栗色空气感卷发与纯欲水光肌：

```text
A hyper-realistic 35mm film photograph of Sakura Kato, a lovely 20-year-old Japanese young woman with natural youthful beauty. She is completely nude, sitting cross-legged on a traditional woven tatami mat next to a sun-drenched shoji window. She has wavy shoulder-length milk-tea chestnut hair with airy see-through bangs, large glistening round honey-amber doe eyes with cute aegyo-sal, and glossy strawberry-pink parted lips with a tender flush across her cheeks. Her petite 160cm soft frame showcases natural delicate curves and youthful smooth contours. Soft afternoon sunlight filters through paper screens, creating a warm luminous rim light along her shoulders and illuminating her dewy peach skin texture with fine authentic pores. Genuine anatomy, nostalgic tender atmosphere, 8k resolution, Masterpiece Fujichrome film aesthetic.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接替换任意 `prompts/scene_*.txt` 中的主体描述部分。

```text
an adorable 20-year-old Japanese woman named Sakura Kato, featuring shoulder-length wavy chestnut-brown hair with soft airy see-through bangs, large sparkling honey-amber doe eyes with cute aegyo-sal, and glossy strawberry-pink parted lips with a natural peach blush, possessing a petite soft feminine frame, smooth youthful curves, and luminous dewy fair skin with authentic fine pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 示例场景：私汤温泉·石阶半浸 (`prompts/scene_onsen_hotspring.txt`)
将 `Sakura Kato` 模块化词块注入私汤温泉场景，水汽蒸腾下的纯欲元气：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle photograph of an adorable 20-year-old Japanese woman named Sakura Kato relaxing in a secluded outdoor natural hot spring at twilight. She is completely nude, featuring shoulder-length wavy chestnut-brown hair with damp airy bangs clinging to her forehead, large glistening honey-amber doe eyes, and glossy strawberry-pink parted lips with soft flushed cheeks. The camera is positioned just above the steaming mineral water surface looking up at her figure: she is kneeling half-submerged on smooth dark volcanic stone steps, her knees naturally parted and her upper body leaning slightly back with arms supporting her weight on the warm stone rim behind her. Rising steam from the thermal bath wraps softly around her shoulders, creating glistening water beads and a radiant dewy sheen across her pale peach skin. The water reflection shimmers below her, framing her lower anatomy clearly between her parted thighs. Background of frosted cedar trees and bamboo lantern glow. Authentic micro skin texture with goosebumps and moisture. 8k resolution, cinematic twilight atmosphere, photorealistic anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_ea03_onsen `
  --prompt "A hyper-realistic, low-angle photograph of an adorable 20-year-old Japanese woman named Sakura Kato relaxing in a secluded outdoor natural hot spring at twilight. She is completely nude, featuring shoulder-length wavy chestnut-brown hair with damp airy bangs clinging to her forehead, large glistening honey-amber doe eyes, and glossy strawberry-pink parted lips with soft flushed cheeks. The camera is positioned just above the steaming mineral water surface looking up at her figure: she is kneeling half-submerged on smooth dark volcanic stone steps, her knees naturally parted and her upper body leaning slightly back with arms supporting her weight on the warm stone rim behind her. Rising steam from the thermal bath wraps softly around her shoulders, creating glistening water beads and a radiant dewy sheen across her pale peach skin. The water reflection shimmers below her, framing her lower anatomy clearly between her parted thighs. Background of frosted cedar trees and bamboo lantern glow. Authentic micro skin texture with goosebumps and moisture. 8k resolution, cinematic twilight atmosphere, photorealistic anatomy." `
  --seed 80964 `
  --steps 50 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/ea03_sakura_onsen.png
```
