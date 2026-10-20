# 人物卡：[CN-06] 林潇湘 (Lin Xiaoxiang) - 红楼绝韵·绛珠仙草

- **卡片编号**：`CN-06`
- **时代分类**：古典文学名著 (Classic Chinese Literature / Dream of the Red Chamber)
- **原型灵感**：林黛玉（以 87 版电视剧《红楼梦》陈晓旭绝代孤傲、幽怨出尘的仙姝神韵为灵魂复刻）
- **主打风格**：绛珠仙子 / 似蹙非蹙罥烟眉 / 似喜非喜含情目 / 娇袭一身之病 / 骨骼纤细柔美 / 东方古典忧郁美学
- **适配场景**：古典雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)、新中式茶室 (`prompts/scene_chinese_tearoom.txt`)、江南水阁亭台 (`prompts/scene_jiangnan_pavilion.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 林潇湘 (Lin Xiaoxiang) | `poetic delicate 19-year-old classical noble maiden named Lin Xiaoxiang` |
| **年龄 (Age)** | 19 岁 | `tender 19 years old` |
| **文学渊源** | 出自《红楼梦》潇湘馆绛珠仙草转世，诗社魁首，才情旷世 | `classical Dream of the Red Chamber aesthetic, tragic poetic heroine` |
| **身高体态** | 163cm，弱柳扶风般的极度纤细柔弱骨感，肩若削成，腰如约素，骨肉极净 | `delicate slender frame, frail graceful posture like a willow branch in wind, narrow sloping shoulders, slender fragile waist` |
| **肤色基底** | 极度通透的冷白偏象牙薄肌，微见青色静脉脉络，白中带着极淡的病态微红 | `translucent paper-white pale skin, delicate cool porcelain complexion with faint bluish vascular undertone, subtle melancholic blush` |
| **气质神态** | 两弯似蹙非蹙罥烟眉，一双似喜非喜含情目；孤高绝俗，多愁多病，令人心生怜惜 | `wistful melancholic gaze, subtle sorrowful brow, proud aloof yet tenderly vulnerable expression` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：含水清眸，似泣非泣，双目清澈深黑如含露晨星，眼眶微带薄红，长睫轻颤。
  - *Prompt*: `dewy glistening dark brown almond eyes brimmed with subtle unshed tears, tender vulnerable gaze, delicate epicanthic fold, fine sparse trembling eyelashes`
- **眉型与鼻梁**：名垂千古的“罥烟眉”——若聚若散、似蹙非蹙的极细黛青色轻眉；小巧精致的琼脂玉鼻，鼻尖微翘。
  - *Prompt*: `faint softly knitted smoky-charcoal willow eyebrows with a natural melancholic arch, delicate refined straight nose with small gentle tip`
- **唇型与面颊**：柔嫩淡樱粉色花瓣小唇，唇色淡雅微敛，下颌如细削鹅卵，双颊略带苍白透明感。
  - *Prompt*: `soft pale rosebud lips naturally parted in a faint sigh, slender tapering jawline with soft chin, delicate high cheekbones`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：古典江南半绾凌虚流云小髻，乌黑柔顺的长发大半如瀑倾泻于后背与单侧前胸，饰以一支极简的白玉簪与素白丝绦。
  - *Prompt*: `flowing waist-length soft silky raven-black hair, half-pinned in an elegant loose scholar maiden chignon with a simple white nephrite hairpin, silky strands resting on bare chest`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：如初雪般细嫩微凉的真实皮质，极细微毛孔与微观皮肤通透感，锁骨突出纤美，隐约可见柔和的光影漫射。
  - *Prompt*: `ultra-fine translucent skin texture with microscopic pores, delicate natural subsurface scattering, soft specular highlight along sharp prominent collarbones and fragile ribcage`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：极度纤巧清瘦的江南才女骨架：纤手修长如削葱根，腰肢不盈一握，小腹平坦微陷，双腿修长纤直。
  - *Prompt*: `fragile slender silhouette, extraordinarily narrow delicate waistline, gentle modest bust, smooth flat abdomen, slender graceful thighs and calves, delicate slender fingers, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美雕琢纤细瘦弱的东方古典骨架与真实私密结构） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，强化水光泪眸与古典闺阁的氛围感） |
| **推理步数 (Steps)** | `45 - 50` | 保证罥烟眉、发丝与羊脂薄肌质感完全收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 营造水墨古典的温润漫射光 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显弱柳扶风的清绝身姿与面容神态 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定清冷忧郁眼神 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证林潇湘的罥烟眉、含水清眸与弱柳扶风的纤弱身段：

```text
A hyper-realistic full-body masterwork studio portrait of Lin Xiaoxiang, a poetic 19-year-old classical noble maiden inspired by Dream of the Red Chamber. She is completely nude, sitting in a demure, fragile kneeling posture on a simple woven rush mat against a translucent silk folding screen painted with faint ink-wash bamboo. She has flowing waist-length silky jet-black hair pinned loosely with a white jade hairpin, softly knitted smoky willow-leaf eyebrows, tear-glistening dark almond eyes with an infinitely tender melancholic gaze, and pale rosebud lips. Her body is remarkably slender and delicate, with sharp prominent collarbones, a tiny frail waist, and slender pale limbs. Soft diffuse cool morning daylight filters through the paper screen, sculpting her translucent porcelain skin with microscopic pores, gentle shadows along her ribs, and a soft dewy sheen. Masterwork, 8k resolution, timeless oriental tragic elegance, Hasselblad 80mm portrait photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a poetic 19-year-old classical Chinese noble maiden named Lin Xiaoxiang with flowing waist-length jet-black hair half-pinned with a white jade pin, faint softly-knitted smoky willow eyebrows, tear-glistening dark almond eyes with an ethereal melancholic gaze, pale rosebud lips, possessing an exceptionally delicate slender frame with sharp collarbones, tiny fragile waist, and translucent porcelain fair skin with authentic fine pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：中式古典红木雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)
将 `Lin Xiaoxiang` 模块化词块嵌入红楼闺阁幽梦场景：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle wide shot of a poetic 19-year-old classical Chinese noble maiden named Lin Xiaoxiang with flowing waist-length jet-black hair half-pinned with a white jade pin, faint softly-knitted smoky willow eyebrows, tear-glistening dark almond eyes with an ethereal melancholic gaze, pale rosebud lips, possessing an exceptionally delicate slender frame with sharp collarbones, tiny fragile waist, and translucent porcelain fair skin with authentic fine pores. She is completely nude, sitting on her knees on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing three-quarters toward the camera, her body subtly arched with one hand resting delicately on the silk-covered bolster behind her, her knees gently spread apart. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn06_lin_xiaoxiang `
  --prompt "A hyper-realistic, low-angle wide shot of a poetic 19-year-old classical Chinese noble maiden named Lin Xiaoxiang with flowing waist-length jet-black hair half-pinned with a white jade pin, faint softly-knitted smoky willow eyebrows, tear-glistening dark almond eyes with an ethereal melancholic gaze, pale rosebud lips, possessing an exceptionally delicate slender frame with sharp collarbones, tiny fragile waist, and translucent porcelain fair skin with authentic fine pores. She is completely nude, sitting on her knees on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing three-quarters toward the camera, her body subtly arched with one hand resting delicately on the silk-covered bolster behind her, her knees gently spread apart. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn06_lin_xiaoxiang_bed.png
```
