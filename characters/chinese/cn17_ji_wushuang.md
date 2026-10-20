# 人物卡：[CN-17] 姬无双 (Ji Wushuang) - 仙侠小说·绝色魔尊赤足妖姬

- **卡片编号**：`CN-17`
- **时代分类**：仙侠修真小说 (Xianxia Cultivation / Novel Fantasy)
- **原型灵感**：仙侠修真小说经典魔教圣女 / 绝色魔尊（融合张雨绮《妖猫传》春琴之妖艳与白鹿仙侠红衣魔女霸道倾城神韵）
- **主打风格**：红衣似火 / 赤足系金铃 / 额心朱砂烈焰魔纹 / 杀伐果断又媚骨天成 / 冰雪肌与赤血轻纱的极致冲击
- **适配场景**：中式古典红木雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)、幽篁竹林私密水阁 (`prompts/scene_bamboo_courtyard.txt`)、江南水阁临渊 (`prompts/scene_jiangnan_pavilion.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 姬无双 (Ji Wushuang) | `breathtaking dangerous 22-year-old Xianxia demonic empress named Ji Wushuang` |
| **年龄 (Age)** | 外表 22 岁（修为通玄） | `perpetual prime 22 years old` |
| **小说渊源** | 仙侠世界九幽魔宗至高女尊，修习太阴合欢极道魔功，视天下正道名门如玩物 | `Xianxia fantasy cultivation novel, supreme demonic sect matriarch` |
| **身高体态** | 169cm，极具柔韧张力与肉感爆棚的魔女体态：水蛇细腰、饱满高耸双峰、修长玉腿配系金铃的白嫩赤足 | `supple agile hourglass silhouette, narrow serpentine waistline, full voluptuous bosom, rounded hips, bare feet with golden ankle bells` |
| **肤色基底** | 如万年玄冰凝结成的无瑕冷白雪肤，极具冰凉触感，在赤红血光映衬下白到晃眼 | `crystalline paper-white pale skin, cold marble undertone with intense visual contrast` |
| **气质神态** | 霸道张狂、生杀予夺，回眸间眼波如钩勾人心魄，危险而致命的顶级魔女压迫感 | `predatory alluring gaze, dangerous seductive smirk, dominant fearless composure` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：极致艳丽的狭长狐系凤眼，眼尾斜飞入鬓，眼周晕染深红魔纹眼影，眸底隐现金红异火流光。
  - *Prompt*: `elongated piercing dark phoenix eyes with subtle glowing crimson inner fire, smoky vermilion winged eye-shadow, dangerously mesmerizing predatory gaze`
- **眉型与魔纹**：斜飞凌厉的柳叶飞刀黛眉；额心手绘一枚鲜艳欲滴的赤红烈焰九幽魔纹。
  - *Prompt*: `sharp fine arched eyebrows, an intricate glowing crimson flame crest mark (bindi) painted on her smooth forehead`
- **唇型与面颊**：饱满如饮鲜血般的深红剧毒花瓣唇，下唇极度饱满微启，下颌线条如寒玉刀削般分明。
  - *Prompt*: `luscious deep blood-red plump lips parted with a cruel seductive smirk, high aristocratic cheekbones, razor-sharp jawline`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：狂野而极富张力的及臀浓密黑长直发，头顶以赤金魔角簪半束，几缕凌乱黑发随魔气飘荡在赤裸胸前。
  - *Prompt*: `wildly cascading hip-length straight glossy jet-black hair caught in ethereal motion, half-pinned with an ornate golden dragon-bone pin, strands framing bare breasts`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：如初雪寒霜般的真实皮肤微毛孔质感，锁骨深凹如刃，在赤色烛火下折射出冰冷而诱惑的白玉微光。
  - *Prompt*: `authentic human skin texture with microscopic pores, cold crystalline subsurface scattering, sharp specular highlights along prominent collarbones and spine`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：极度柔韧的水蛇腰肢，饱满挺拔的胸部与圆润肉感的丰臀，脚踝处各系一串细金链串缀的赤金小铃铛。
  - *Prompt*: `hyper-supple hourglass proportions, extraordinarily narrow flexible waist, full voluptuous bustline, rounded firm hips, smooth shapely thighs, dainty bare feet with delicate gold chain ankle bells, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美刻画魔女水蛇腰身与高精度解剖） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.85`（搭配 CFG 4.0，强化血色纱幔与私密魔殿真实质感） |
| **推理步数 (Steps)** | `45 - 50` | 保证额心魔纹细节与飘散长发光影完全收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 暗黑赤红与冷白高对比光影表现 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显及臀长发与赤足金铃的魔女身段 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定妖艳霸道眼神 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证姬无双的额心烈焰魔纹、赤足金铃与极度霸道妖娆的魔尊身段：

```text
A hyper-realistic full-body masterwork studio portrait of Ji Wushuang, a dangerous 22-year-old Xianxia demonic empress. She is completely nude, posing in a dominant contrapposto arched stance against a pitch-black obsidian backdrop with floating crimson silk ribbons. She has hip-length glossy raven-black hair cascading wildly, piercing dark phoenix eyes with glowing crimson inner embers, an intricate red flame crest painted on her forehead, and blood-red lips curled in a ruthless smirk. Her frame is an intensely supple hourglass with a snake-like waistline, full natural bosom, and rounded hips, with delicate gold chain bells around her slender ankles. Dramatic warm crimson side-lighting sculpts her pristine cold alabaster skin, highlighting microscopic pores, sharp collarbones, and deep sculpted anatomical shadows. Masterwork, 8k resolution, dark Xianxia fantasy aesthetic, Hasselblad 100mm portrait photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a dangerous seductive 22-year-old Xianxia demonic empress named Ji Wushuang with wildly cascading hip-length jet-black hair, piercing dark phoenix eyes with crimson embers, a red flame crest mark on her forehead, deep blood-red lips, dainty bare feet with gold ankle bells, possessing a hyper-supple hourglass frame with narrow snake waist, full natural bust, rounded hips, and pristine cold alabaster skin with authentic fine pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：中式古典红木雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)
将 `Ji Wushuang` 模块化词块嵌入血红罗帐暖玉大床，化身寝宫中的绝色魔尊：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle wide shot of a dangerous seductive 22-year-old Xianxia demonic empress named Ji Wushuang with wildly cascading hip-length jet-black hair, piercing dark phoenix eyes with crimson embers, a red flame crest mark on her forehead, deep blood-red lips, dainty bare feet with gold ankle bells, possessing a hyper-supple hourglass frame with narrow snake waist, full natural bust, rounded hips, and pristine cold alabaster skin with authentic fine pores. She is completely nude, sitting on her knees on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing three-quarters toward the camera, her body subtly arched with one hand resting delicately on the silk bolster behind her, her knees gently spread apart. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn17_ji_wushuang `
  --prompt "A hyper-realistic, low-angle wide shot of a dangerous seductive 22-year-old Xianxia demonic empress named Ji Wushuang with wildly cascading hip-length jet-black hair, piercing dark phoenix eyes with crimson embers, a red flame crest mark on her forehead, deep blood-red lips, dainty bare feet with gold ankle bells, possessing a hyper-supple hourglass frame with narrow snake waist, full natural bust, rounded hips, and pristine cold alabaster skin with authentic fine pores. She is completely nude, sitting on her knees on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing three-quarters toward the camera, her body subtly arched with one hand resting delicately on the silk bolster behind her, her knees gently spread apart. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn17_ji_wushuang_bed.png
```
