# 人物卡：[CN-07] 龙芷清 (Long Zhiqing) - 终南绝俗·出尘剑仙

- **卡片编号**：`CN-07`
- **时代分类**：经典武侠名著 (Classic Wuxia Fiction / Mount Zhongnan Hermit)
- **原型灵感**：小龙女（融合刘亦菲 / 李若彤版古装武侠“白衣出尘、不食人间烟火”的天仙绝俗神韵）
- **主打风格**：不食人间烟火 / 冰肌玉骨 / 冷若霜雪 / 纯白丝绦 / 灵动出尘仙姿
- **适配场景**：幽篁竹林私密水阁 (`prompts/scene_bamboo_courtyard.txt`)、江南临水亭台 (`prompts/scene_jiangnan_pavilion.txt`)、新中式茶室 (`prompts/scene_chinese_tearoom.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 龙芷清 (Long Zhiqing) | `ethereal 20-year-old Wuxia immortal fairy maiden named Long Zhiqing` |
| **年龄 (Age)** | 20 岁 | `timeless youth 20 years old` |
| **武侠渊源** | 终南山活死人墓古墓派传人，久居幽室，不知世事，天生冰清玉洁 | `classical Wuxia swordsman fairy, ancient tomb hermit aesthetic` |
| **身高体态** | 167cm，身轻如燕若惊鸿，体态轻盈而富有习武之人的柔韧线条，仙气飘逸 | `lithe agile fairy physique, natural flexibility, slender waist, graceful dancer-swordsman posture` |
| **肤色基底** | 冰雪铸就的冷白玉肤，无丝毫血色杂质，通透如昆仑美玉 | `pristine crystalline snow-white fair skin, translucent cold jade undertone` |
| **气质神态** | 清冷空灵、不染纤尘、澄澈无波的冰霜眼眸，超脱于红尘俗世之外 | `serene untouched ethereal gaze, crystalline aloof expression, sublime otherworldly purity` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：澄澈如冰泉的黑玉丹凤眼，眼眸中无一丝世俗机巧，如秋水无波，长睫如雪后松针。
  - *Prompt*: `crystal-clear dark obsidian eyes with pure tranquil reflection, utterly unblemished by earthly emotion, fine straight eyelashes, calm serene gaze`
- **眉型与鼻梁**：极尽纯净的天然远山青黛平眉；琼鼻秀挺如削，山根挺拔清秀，侧颜弧度极品。
  - *Prompt*: `natural fine straight-arched eyebrows, exquisitely carved slender straight nose with a soft delicate tip`
- **唇型与面颊**：天生极淡的粉白初雪唇色，唇珠小巧，神态宁静超然，下颌线条流畅柔美。
  - *Prompt*: `delicate naturally pale-pink lips lightly closed, flawless oval face with pure innocent contours, pristine untainted complexion`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：及臀如瀑乌黑长直发，头顶半绾极简飞仙髻，系有纯白丝绸飘带，微风轻拂时发丝如墨玉流云。
  - *Prompt*: `hip-length cascading straight silk-like jet-black hair with mirror shine, half-bound in a simple high immortal knot with fluttering pure white silk ribbons, strands drifting across bare shoulders`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：真正的“冰肌玉骨”，肌肤细腻如冷冻白脂，微观毛孔清晰自然，在月光下折射出淡淡的银蓝色冷辉。
  - *Prompt*: `crystalline authentic human skin texture with microscopic pores, natural cool subsurface scattering, soft silvery-blue moonlight sheen on slender collarbones and spine`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：修长而极富柔韧张力的仙子身段：轻盈直角肩、纤细柔软的柳腰、紧致平坦的小腹与匀称修长的玉腿。
  - *Prompt*: `lithe athletic fairy silhouette, graceful sloping shoulders, extraordinarily supple narrow waistline, firm smooth abdomen, long toned legs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美雕琢仙气脱俗的东方古风骨相与纯净肉身结构） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.75`（搭配 CFG 4.0，兼顾冷白微光与真实皮肤反光） |
| **推理步数 (Steps)** | `45 - 50` | 保证及臀长发发丝与冰冷月光光影完全收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 纯净冷色调漫反射的最佳组合 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显及臀长发与超凡脱俗的仙气比例 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定超凡脱俗的天仙面庞 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证龙芷清的终南出尘白衣神仙姐姐神颜、极冷玉肤与及臀乌发：

```text
A hyper-realistic full-body masterwork studio portrait of Long Zhiqing, an ethereal 20-year-old classical Chinese Wuxia immortal fairy. She is completely nude, standing in a serene weightless posture against a dark slate-grey minimalist stone backdrop with pure white silk ribbons floating around her. She has hip-length straight silky jet-black hair with a simple immortal bun, crystal-clear dark obsidian eyes with an untouched tranquil gaze, finely sculpted straight nose, and pale blossom lips. Her frame is lithe, supple, and slender with delicate sloping shoulders, a tiny flexible waistline, and smooth toned legs. Cool silvery-blue diffused moonlight washes over her pristine alabaster skin, accentuating microscopic fine pores, natural subsurface scattering, and soft specular highlights along her collarbones and ribcage. Supreme oriental immortal elegance, 8k resolution, Hasselblad 100mm medium format photograph.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
an ethereal 20-year-old Wuxia immortal fairy maiden named Long Zhiqing with hip-length straight silky jet-black hair bound with pure white ribbons, crystal-clear tranquil dark obsidian eyes, pristine pale blossom lips, possessing a lithe supple fairy frame with delicate shoulders, tiny flexible waist, and crystalline snow-white porcelain skin with authentic micro-pores and cool moonlight sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：江南烟雨水阁临渊 (`prompts/scene_jiangnan_pavilion.txt`)
将 `Long Zhiqing` 模块化词块嵌入烟雨空灵的水阁亭台：

#### 合成完整 Prompt：
```text
A hyper-realistic, wide-angle cinematic shot of an ethereal 20-year-old Wuxia immortal fairy maiden named Long Zhiqing with hip-length straight silky jet-black hair bound with pure white ribbons, crystal-clear tranquil dark obsidian eyes, pristine pale blossom lips, possessing a lithe supple fairy frame with delicate shoulders, tiny flexible waist, and crystalline snow-white porcelain skin with authentic micro-pores and cool moonlight sheen. She is completely nude, sitting gracefully on the weathered dark wooden bench of a traditional open-air water pavilion extending over a misty lotus pond. Her body is seated in profile, one leg bent upward with her arm resting along her knee, gaze fixed peacefully on the calm water ripples, while her other leg hangs down toward the dark water. Cool evening dusk light combined with the soft glow of a nearby stone garden lantern illuminates her body, casting silvery highlights across her collarbones, soft stomach, and thighs. Dense evening mist rises from the pond, swirling around the timber posts. The low wide perspective captures the natural contours of her lower anatomy illuminated by cool lantern light reflections from the water below. 8k resolution, misty atmospheric depth, authentic photorealistic female anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn07_long_zhiqing `
  --prompt "A hyper-realistic, wide-angle cinematic shot of an ethereal 20-year-old Wuxia immortal fairy maiden named Long Zhiqing with hip-length straight silky jet-black hair bound with pure white ribbons, crystal-clear tranquil dark obsidian eyes, pristine pale blossom lips, possessing a lithe supple fairy frame with delicate shoulders, tiny flexible waist, and crystalline snow-white porcelain skin with authentic micro-pores and cool moonlight sheen. She is completely nude, sitting gracefully on the weathered dark wooden bench of a traditional open-air water pavilion extending over a misty lotus pond. Her body is seated in profile, one leg bent upward with her arm resting along her knee, gaze fixed peacefully on the calm water ripples, while her other leg hangs down toward the dark water. Cool evening dusk light combined with the soft glow of a nearby stone garden lantern illuminates her body, casting silvery highlights across her collarbones, soft stomach, and thighs. Dense evening mist rises from the pond, swirling around the timber posts. The low wide perspective captures the natural contours of her lower anatomy illuminated by cool lantern light reflections from the water below. 8k resolution, misty atmospheric depth, authentic photorealistic female anatomy." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn07_long_zhiqing_pavilion.png
```
