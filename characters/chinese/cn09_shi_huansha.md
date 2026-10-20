# 人物卡：[CN-09] 施浣纱 (Shi Huansha) - 春秋越国·沉鱼绝代

- **卡片编号**：`CN-09`
- **时代分类**：春秋战国 (Spring & Autumn Period / Ancient Yue)
- **原型灵感**：西施（融合蒋勤勤经典古装《西施》江南水灵初恋、清水出芙蓉的第一神颜）
- **主打风格**：沉鱼落雁 / 苎萝浣纱 / 天然去雕饰 / 捧心微蹙娇美 / 江南水乡初恋白月光
- **适配场景**：江南水阁临渊 (`prompts/scene_jiangnan_pavilion.txt`)、幽篁竹林私密水阁 (`prompts/scene_bamboo_courtyard.txt`)、新中式茶室 (`prompts/scene_chinese_tearoom.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 施浣纱 (Shi Huansha) | `breathtaking innocent 18-year-old ancient Yue maiden named Shi Huansha` |
| **年龄 (Age)** | 18 岁（桃李初绽） | `tender youthful 18 years old` |
| **历史渊源** | 春秋战国越国苎萝山下浣纱女，四大美女之首，沉鱼倾国 | `ancient Chinese Spring and Autumn period, legendary Xi Shi archetype` |
| **身高体态** | 165cm，江南水乡浑然天成的骨肉匀称与纤软柔荑，腰肢柔若无骨，身段玲珑灵秀 | `naturally graceful slender frame, delicate sloping shoulders, soft natural curves, supple waistline` |
| **肤色基底** | 仿佛山泉涤荡出的天然羊脂白透，粉嫩通透，如带露初荷 | `pure dewy porcelain skin with natural rosy water-lily undertones, translucent clarity` |
| **气质神态** | 清纯脱俗、我见犹怜；微捧胸口时微蹙双眉，眼波如秋水横生，纯真中带着致命的楚楚动人 | `innocent bewitching gaze, faint vulnerable brow, captivating pure maiden charm, tender bashful smile` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：如春水般澄澈温润的东方杏仁水眸，眼底清亮无瑕，睫毛微翘带着天然露水感。
  - *Prompt*: `crystal-clear dewy dark almond eyes with soft innocent expression, naturally dense curved eyelashes, pristine gentle gaze filled with pure emotion`
- **眉型与鼻梁**：天然秀气的初春柳叶细黛眉，眉峰微蹙带着江南女儿特有的娇憨与柔弱；小巧挺秀的天然水葱琼鼻。
  - *Prompt*: `natural fine willow-leaf eyebrows slightly knitted in delicate vulnerability, dainty straight nose with gentle rounded soft tip`
- **唇型与面颊**：天然水嫩的樱桃淡粉小唇，饱满微嘟，双颊如春桃初熟般透出自然的粉润血色。
  - *Prompt*: `tender petal-pink lips naturally parted with soft dewy gloss, soft oval jawline, naturally blushing peach-blossom cheeks`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：春秋越女质朴自然的双环垂髻，大部分乌黑亮丽的发丝柔顺披散于后背与前胸，饰以一支质朴的天然木簪。
  - *Prompt*: `natural waist-length silky soft raven-black hair, half-pinned in modest ancient Yue twin loop chignons with a simple carved wooden hairpin, flowing softly over bare shoulders`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：清水出芙蓉般的极品原生肌肤，微观毛孔清晰细微，微汗与山泉水珠在锁骨与平坦小腹上滑落反光。
  - *Prompt*: `pristine authentic human skin texture with microscopic pores, delicate moisture droplets glistening along collarbones and stomach, luminous natural subsurface scattering`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：纤秾合度，骨肉亭匀，胸型挺拔小巧如初绽蓓蕾，纤细柔韧的柳腰，小腿线条如削玉般纤直。
  - *Prompt*: `youthful slender maiden silhouette, modest firm natural bosom, tiny supple waist, soft rounded hips, smooth slender thighs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美雕琢清纯水灵的东方古典少女骨肉） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，强化水珠滑落与山涧私密写真真实感） |
| **推理步数 (Steps)** | `45 - 50` | 保证水润皮肤通透感与发丝细节完全收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 柔美清澈自然光的最佳表现 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显水乡少女的灵秀身段与清水出芙蓉的面庞 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定清纯初恋五官 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证施浣纱的纯天然沉鱼神颜、捧心微蹙娇态与如水凝脂：

```text
A hyper-realistic full-body masterwork studio portrait of Shi Huansha, a breathtaking 18-year-old ancient Chinese Yue maiden inspired by the legendary Xi Shi. She is completely nude, standing demurely with one hand gently hovering near her chest in a faint vulnerable gesture against a minimalist soft green silk scroll backdrop. She has waist-length silky soft black hair with modest loop chignons and a wooden hairpin, pristine dewy dark almond eyes with a tender innocent gaze, faint soft willow eyebrows slightly knitted, and fresh petal-pink parted lips. Her body is lithe, soft, and naturally slender with delicate sloping shoulders, a narrow supple waist, and firm smooth thighs. Soft natural diffused morning stream-light illuminates her porcelain skin with a gentle peachy bloom, highlighting microscopic pores, fine water-droplets glistening on her collarbones, and authentic anatomical contours. Masterpiece, 8k resolution, timeless oriental innocence, Hasselblad 80mm portrait photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a breathtaking innocent 18-year-old ancient Yue maiden named Shi Huansha with waist-length soft silky black hair half-pinned in loop chignons with a wooden pin, crystal-clear dewy dark almond eyes, faint softly-knitted willow eyebrows, tender petal-pink lips, possessing a youthful slender frame with delicate sloping shoulders, narrow supple waist, and dewy porcelain skin with natural rosy undertones and authentic fine pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：江南烟雨水阁临渊 (`prompts/scene_jiangnan_pavilion.txt`)
将 `Shi Huansha` 模块化词块嵌入烟雨空灵的水乡水阁亭台：

#### 合成完整 Prompt：
```text
A hyper-realistic, wide-angle cinematic shot of a breathtaking innocent 18-year-old ancient Yue maiden named Shi Huansha with waist-length soft silky black hair half-pinned in loop chignons with a wooden pin, crystal-clear dewy dark almond eyes, faint softly-knitted willow eyebrows, tender petal-pink lips, possessing a youthful slender frame with delicate sloping shoulders, narrow supple waist, and dewy porcelain skin with natural rosy undertones and authentic fine pores. She is completely nude, sitting gracefully on the weathered dark wooden bench of a traditional open-air water pavilion extending over a misty lotus pond. Her body is seated in profile, one leg bent upward with her arm resting along her knee, gaze fixed peacefully on the calm water ripples, while her other leg hangs down toward the dark water. Cool evening dusk light combined with the soft glow of a nearby stone garden lantern illuminates her body, casting silvery highlights across her collarbones, soft stomach, and thighs. Dense evening mist rises from the pond, swirling around the timber posts. The low wide perspective captures the natural contours of her lower anatomy illuminated by cool lantern light reflections from the water below. 8k resolution, misty atmospheric depth, authentic photorealistic female anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn09_shi_huansha `
  --prompt "A hyper-realistic, wide-angle cinematic shot of a breathtaking innocent 18-year-old ancient Yue maiden named Shi Huansha with waist-length soft silky black hair half-pinned in loop chignons with a wooden pin, crystal-clear dewy dark almond eyes, faint softly-knitted willow eyebrows, tender petal-pink lips, possessing a youthful slender frame with delicate sloping shoulders, narrow supple waist, and dewy porcelain skin with natural rosy undertones and authentic fine pores. She is completely nude, sitting gracefully on the weathered dark wooden bench of a traditional open-air water pavilion extending over a misty lotus pond. Her body is seated in profile, one leg bent upward with her arm resting along her knee, gaze fixed peacefully on the calm water ripples, while her other leg hangs down toward the dark water. Cool evening dusk light combined with the soft glow of a nearby stone garden lantern illuminates her body, casting silvery highlights across her collarbones, soft stomach, and thighs. Dense evening mist rises from the pond, swirling around the timber posts. The low wide perspective captures the natural contours of her lower anatomy illuminated by cool lantern light reflections from the water below. 8k resolution, misty atmospheric depth, authentic photorealistic female anatomy." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn09_shi_huansha_pavilion.png
```
