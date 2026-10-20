# 人物卡：[CN-15] 柳天仙 (Liu Tianxian) - 现代神颜·纯欲天花板

- **卡片编号**：`CN-15`
- **时代分类**：现代神颜顶流 (Modern Contemporary Visual Peak)
- **原型灵感**：刘亦菲 (Liu Yifei) 现代红毯与私服“天仙神颜、纯欲脱俗、冷白发光皮”神韵
- **主打风格**：天仙神颜 / 东方极品驼峰琼鼻 / 清冷纯欲天花板 / 冷白皮牛奶肌 / 名门千金贵气
- **适配场景**：私汤温泉氤氲暖池 (`prompts/scene_onsen_hotspring.txt`)、顶层豪宅全景落地窗 (`prompts/scene_penthouse_stretch.txt`)、现代赛博夜景阳台 (`prompts/scene_cyber_balcony.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 柳天仙 (Liu Tianxian) | `peerless 23-year-old Chinese visual peak superstar named Liu Tianxian` |
| **年龄 (Age)** | 23 岁 | `prime youth 23 years old` |
| **职业与身份** | 华语影坛“国民天仙”，东方皮相与骨相完美兼备的神颜代表 | `iconic top Chinese actress, modern fairy aesthetic goddess` |
| **身高体态** | 170cm，极具东方天仙贵气的匀称微曲线身材：骨肉停匀、修长天鹅颈、优雅肩颈线、修长玉腿 | `tall 170cm statuesque graceful frame, long swan neck, soft feminine curves, naturally slender waist` |
| **肤色基底** | 标志性冷白皮，通透如凝脂牛奶，在任何自然光下自带漫反射发光感 | `luminous cool-toned milky-porcelain skin, radiant natural glow, pristine flawless tone` |
| **气质神态** | 不染纤尘、清冷疏离中透出纯真娇憨；看似不争不抢，却自带压倒全场的贵气天仙气场 | `effortless ethereal gaze, gentle regal composure, unearthly pure yet captivating aura` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：东方内双极品灵动丹凤眼，眼眸深黑清亮如晨星，眼角微微含蓄内敛，神态纯欲脱俗。
  - *Prompt*: `clear captivating dark almond eyes with delicate inner double eyelids, soft innocent yet alluring gaze, naturally fine straight eyelashes`
- **鼻型与立体度**：华语神颜标志性的极品微驼峰直鼻，山根高挺清秀，鼻头微翘小巧，侧颜绝美。
  - *Prompt*: `signature aristocratic straight nose with a subtle iconic dorsal hump and refined narrow tip, breathtaking side profile`
- **唇型与面颊**：天然樱桃肉粉色水润唇瓣，饱满微启；古典标准的圆润温润鹅蛋脸，下巴线条圆润柔美。
  - *Prompt*: `plump naturally petal-pink lips glistening with soft moisture, perfectly balanced classic Chinese oval face, smooth elegant jawline`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：丰盈柔顺的及腰黑曜石自然微卷长发，发质极其丝滑富有高级光泽，随意披散在雪白香肩。
  - *Prompt*: `waist-length luxurious silky jet-black wavy hair with healthy mirror shine, cascading softly over her bare shoulders and spine`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：如羊脂冷玉般的现代高清真人体感，微细毛孔均匀无瑕，锁骨、双肩与平坦小腹带有天然水光微汗高光。
  - *Prompt*: `authentic human skin texture with microscopic pores, soft cool-toned subsurface scattering, dewy moisture sheen across collarbones and stomach`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：典型的东方式“增一分则太肥，减一分则太瘦”：修长紧致的双腿、盈盈一握的柔美腰身、饱满恰到好处的天然胸型。
  - *Prompt*: `naturally balanced feminine curves, slender waistline, modest rounded natural bust, smooth toned thighs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.85`（搭配 CFG 4.0，绝妙呈现顶级明星私密写真质感与冷白发光皮） |
| **推荐 LoRA 2** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `0.95`（搭配 CFG 2.5，极致精准的解剖学与水润真实皮肤） |
| **推理步数 (Steps)** | `45 - 50` | 保证发丝质感与驼峰鼻轮廓完全收敛 |
| **引导系数 (CFG)** | `4.0` (TheseAlpacas) / `2.5` (tawsLoRa) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 柔美冷白高调光影最佳表现 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显 170cm 天仙神姿与面容神韵 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定经典天仙五官 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证柳天仙的标志性驼峰琼鼻、鹅蛋脸、冷白皮与天仙气质：

```text
A hyper-realistic full-body fashion studio photograph of Liu Tianxian, a peerless 23-year-old Chinese visual peak superstar. She is completely nude, posing in an elegant, effortless contrapposto standing posture against a minimalist soft dove-grey studio wall. She has waist-length silky soft black hair falling over her bare shoulders, clear enchanting dark almond eyes with delicate epicanthic folds, a signature aristocratic straight nose with a subtle dorsal hump, and luscious natural petal-pink lips. Her silhouette is tall at 170cm with graceful sloping shoulders, a slender waist, and soft feminine curves. Soft diffuse beauty-dish studio lighting sculpts her cool-toned milky-porcelain skin, revealing authentic microscopic pores, natural soft subsurface scattering, and dewy highlights along her collarbones and hips. Masterwork, 8k resolution, timeless ethereal goddess aesthetic, Hasselblad 100mm portrait photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a peerless 23-year-old Chinese visual peak superstar named Liu Tianxian with waist-length silky jet-black wavy hair, clear enchanting dark almond eyes, signature straight nose with subtle dorsal hump, plump petal-pink lips, classic oval face, possessing a tall 170cm graceful frame with delicate collarbones, slender waist, and luminous cool-toned milky-porcelain skin with authentic fine pores and dewy sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：私汤温泉氤氲暖池 (`prompts/scene_onsen_hotspring.txt`)
将 `Liu Tianxian` 模块化词块嵌入温泉温汤场景，化身水汽蒸腾中的绝美天仙：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle shot of a peerless 23-year-old Chinese visual peak superstar named Liu Tianxian with waist-length silky jet-black wavy hair, clear enchanting dark almond eyes, signature straight nose with subtle dorsal hump, plump petal-pink lips, classic oval face, possessing a tall 170cm graceful frame with delicate collarbones, slender waist, and luminous cool-toned milky-porcelain skin with authentic fine pores and dewy sheen resting in a traditional private outdoor hot spring (onsen) at dusk. The camera is set just above the steaming water line, looking slightly upward. She is kneeling on smooth dark volcanic stones with her knees slightly parted submerged in water, leaning her torso slightly back with both hands braced behind her on the damp rock rim. Her long black hair is pinned up loosely with moist strands sticking to her wet neck and collarbone. The warm thermal spring water leaves her glistening with wet sheen, water beads rolling down her shoulders and stomach. Due to her posture and low water clarity, her bare hips and the natural contour of her parted lower anatomy are subtly visible above and beneath the clear water surface. Soft golden lantern light reflects off the steam and water ripples, contrasting with the dark cedar wood and bamboo backdrop. Realistic skin texture with visible goosebumps and pores. 8k resolution, cinematic lighting, candid "caught in the moment" atmosphere, photorealistic anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn15_liu_tianxian `
  --prompt "A hyper-realistic, low-angle shot of a peerless 23-year-old Chinese visual peak superstar named Liu Tianxian with waist-length silky jet-black wavy hair, clear enchanting dark almond eyes, signature straight nose with subtle dorsal hump, plump petal-pink lips, classic oval face, possessing a tall 170cm graceful frame with delicate collarbones, slender waist, and luminous cool-toned milky-porcelain skin with authentic fine pores and dewy sheen resting in a traditional private outdoor hot spring (onsen) at dusk. The camera is set just above the steaming water line, looking slightly upward. She is kneeling on smooth dark volcanic stones with her knees slightly parted submerged in water, leaning her torso slightly back with both hands braced behind her on the damp rock rim. Her long black hair is pinned up loosely with moist strands sticking to her wet neck and collarbone. The warm thermal spring water leaves her glistening with wet sheen, water beads rolling down her shoulders and stomach. Due to her posture and low water clarity, her bare hips and the natural contour of her parted lower anatomy are subtly visible above and beneath the clear water surface. Soft golden lantern light reflects off the steam and water ripples, contrasting with the dark cedar wood and bamboo backdrop. Realistic skin texture with visible goosebumps and pores. 8k resolution, cinematic lighting, candid "caught in the moment" atmosphere, photorealistic anatomy." `
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
  --out outputs/characters/cn15_liu_tianxian_hotspring.png
```
