# 人物卡：[CN-19] 苏青荷 (Su Qinghe) - 幽兰冷玉·古典茶道名媛

- **卡片编号**：`CN-19`
- **时代分类**：新中式典雅名媛 (Neo-Chinese Elegant Aristocrat)
- **原型灵感**：江南书香世家与茶道名媛，结合清冷仙姿与内敛温润的东方身段
- **主打风格**：清冷禁欲 / 幽兰冷香 / 骨相绝美 / 旗袍微解 / 极度柔韧的古典肢体语言
- **适配场景**：新中式禅意茶室 (`prompts/scene_chinese_tearoom.txt`)、古典雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)、3D姿态精准写真 (`templates/photobooks/pose3d_studio.yaml`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 苏青荷 (Su Qinghe) | `stunning 23-year-old elegant classical Chinese aristocrat named Su Qinghe` |
| **年龄 (Age)** | 23 岁 | `young 23-year-old woman` |
| **血统背景** | 江南名门，精通琴棋茶道与传统舞姿 | `heritage Chinese nobility, refined tea master aura` |
| **身高体态** | 170cm，修长优雅的白鹭体态，纤细柔韧的水蛇腰与挺拔优美的锁骨轮廓 | `170cm, tall slender lithe frame, narrow flexible waistline, sculpted delicate collarbones, elegant proportions` |
| **肤色基底** | 冷玉羊脂白，微透光泽，在自然天光与烛影下温润如瓷 | `cool porcelain alabaster skin with translucent dewy glow` |
| **气质神态** | 外表清冷孤傲如幽兰，眼神平静却暗含摄人微澜，静若处子动若惊鸿 | `serene aloof expression, noble ethereal gaze, subtle quiet sensuality` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：标准的东方丹凤杏眼，内眼角微尖，眼尾平滑修长，睫毛密长而下垂，眼神清冷而深邃。
  - *Prompt*: `refined classical almond phoenix eyes with sharp inner corners and elongated outer lash lines, deep obsidian pupils, quiet piercing gaze`
- **眉鼻**：远山黛眉，鼻梁细窄秀挺，鼻头圆润小巧，极具东方骨相之美。
  - *Prompt*: `delicate soft willow brows, straight slender nose bridge with refined tip`
- **唇齿与神态**：天然淡樱色薄唇，唇峰分明，微启时露出齐整贝齿，神情沉静淡泊中微带一丝迷离。
  - *Prompt*: `naturally pale rosebud lips slightly parted, calm aristocratic poise, subtly alluring detachment`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：乌黑如瀑的顺直丝绸长发，垂落至腰际，或以一支冷玉簪半挽，微分散落于雪白香肩。
  - *Prompt*: `long lustrous jet-black silky straight hair cascading down her spine, loose tendrils framing her neck and bare shoulders`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：如浸润雨露的上等羊脂白玉，真实微观毛孔透气细腻，锁骨线条与脊椎凹线具有丝缎般的漫反射高光。
  - *Prompt*: `hyper-realistic human skin texture, delicate microscopic pores, soft dewy luminescence along collarbones, spine curve, and shoulders`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：常年习舞与茶道的绝佳柔韧体态，脊背挺拔优美，腰臀比例紧致曼妙，四肢修长匀称。
  - *Prompt*: `supple dancer physique, naturally arched spine, graceful elongated limbs, slender waist, toned gentle hip curves`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（纯净画质与高精准解剖结构） |
| **推荐 LoRA 2** | `VNCCS_QI2_PoseStudioV1.1.safetensors` | 权重 `1.0`（当采用方式 2 3D 姿态控制时专用） |
| **推理步数 (Steps)** | `45 - 50` | 保证玉石般冷白肤质与顺滑发丝充分收敛 |
| **引导系数 (CFG)** | `2.5 - 3.5` | 避免过度锐化，保留自然柔美层次 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最佳质感与光影组合 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显高挑修长身段与高难度姿势线条 |
| **Seed 推荐** | `80964` | 清冷五官与东方韵味最佳表现 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

```text
A hyper-realistic full-body studio portrait of Su Qinghe, a breathtaking 23-year-old Chinese noblewoman. She is completely nude, standing in an elegant poised posture against a minimalist muted silk screen. She has refined classical phoenix eyes, delicate slender nose, and long lustrous straight black hair cascading over her shoulders. Lithe dancer physique with a supple slender waist and sculpted collarbones. Soft diffuse northern window light illuminating her translucent porcelain white skin. Authentic skin texture with visible micro-pores, masterwork, Hasselblad 85mm portrait, 8k resolution.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

```text
a stunning 23-year-old classical Chinese noblewoman named Su Qinghe with refined phoenix eyes, long silky straight raven hair cascading over bare shoulders, translucent cool alabaster porcelain skin, and a lithe dancer's slender hourglass frame with sculpted collarbones and delicate curves
```

---

## 6. 与 3D 姿态控制（方式 2）的适配性

苏青荷极度适合 [templates/photobooks/pose3d_studio.yaml](pose3d_studio.yaml) 模板，能将 3D 骨骼库中的高难度跪姿、后仰下腰与俯卧爬行姿势演绎出东方冷玉般的高级美感。
