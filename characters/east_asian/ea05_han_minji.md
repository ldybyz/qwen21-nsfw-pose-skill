# 人物卡：[EA-05] 韩敏智 (Han Minji) - 极致线条·普拉提健美超模

- **卡片编号**：`EA-05`
- **时代分类**：现代都市 / 健美塑形 (Modern Athletic / Fitness & Pilates)
- **原型灵感**：韩国首尔顶级普拉提私教兼高级时装超模，拥有惊人的肌肉柔韧度与极致腰臀比
- **主打风格**：高级健美骨相 / 紧致人鱼线 / 力量与柔韧兼备 / 水光肌微汗 / 极限瑜伽拉伸姿势
- **适配场景**：顶层豪宅落地窗 (`prompts/scene_penthouse_stretch.txt`)、3D姿态精准写真 (`templates/photobooks/pose3d_studio.yaml`)、极简现代摄影棚

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 韩敏智 (Han Minji) | `strikingly beautiful 24-year-old Korean pilates instructor and fitness model named Han Minji` |
| **年龄 (Age)** | 24 岁 | `athletic 24-year-old woman` |
| **国籍背景** | 韩国首尔，专业级普拉提教练与健美超模 | `Korean Seoul modern aesthetic, elite athletic conditioning` |
| **身高体态** | 172cm，长腿蜂腰，紧致微马甲线，紧实圆润蜜桃臀，极度舒展的肌肉线条 | `172cm, long toned legs, tight waist with subtle abdominal definition, sculpted athletic curves, exceptional flexibility` |
| **肤色基底** | 健康明亮的浅蜜色水光肌，微光粼粼，运动后带有清透自然的血色微红 | `glowing radiant glass-skin with subtle healthy flush and glossy finish` |
| **气质神态** | 充满活力自信、眼神专注坚定却带有女性独有的柔美张力，落落大方 | `confident radiant gaze, poised athletic energy, sophisticated modern charm` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：清澈明亮微上挑的猫系内双眸，眼神专注犀利，睫毛自然浓密，神情专注且具抓人力量。
  - *Prompt*: `clear captivating dark brown cat-like eyes with subtle double eyelids, sharp focus, natural defined eyelashes`
- **眉鼻**：自然平整带有轻微英气的野生雾眉，鼻梁高挺小巧，下颌线条清晰分明。
  - *Prompt*: `natural feathered brown eyebrows, sculpted straight nose bridge, crisp defined jawline`
- **唇齿与神态**：饱满水蜜桃裸色水光唇，嘴角自然微扬，呼吸间微露整齐皓齿。
  - *Prompt*: `plump glossy nude peach lips, confident composed expression, parted slightly in rhythmic breathing`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：深栗色轻微层次长发，束起的高马尾或运动后微湿散落于后颈与锁骨。
  - *Prompt*: `luxurious dark chestnut-brown hair, styled in a sleek high ponytail or tumbling naturally over her shoulders with fine wisps`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：典型的韩国水光肌（Glass Skin），微汗颗粒在侧光下晶莹闪烁，腹肌阴影与脊椎凹槽光影分明。
  - *Prompt*: `authentic glowing skin texture, fine micro-pores, delicate sheen of perspiration droplets catching studio light, crisp anatomical muscle shadows`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：常年普拉提与大拉伸塑造的修长肌肉线条，背阔肌线条优美，臀大肌紧实饱满，大腿紧致修长。
  - *Prompt*: `toned athletic hourglass silhouette, defined oblique lines, sculpted glutes, long slender muscular thighs, extreme flexibility`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（肌肉线条与腹肌解剖表现最佳） |
| **推荐 LoRA 2** | `VNCCS_QI2_PoseStudioV1.1.safetensors` | 权重 `1.0`（用于方式 2 3D 骨骼控制精准还原瑜伽体态） |
| **推理步数 (Steps)** | `45` | 保证水光肌高光与肌肉阴影细腻自然 |
| **引导系数 (CFG)** | `3.0` | 保证肌肉质感真实不生硬 |
| **采样器 / 调度器** | `er_sde` / `beta` | 现代自然光最佳表现 |
| **生图分辨率** | `1152x1728` (竖版) / `1344x768` (横版深蹲/拉伸) | 适配各种大动作幅度的骨骼姿势 |
| **Seed 推荐** | `80964` | 稳定韩国都市高级脸型 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

```text
A hyper-realistic full-body fitness portrait of Han Minji, a stunning 24-year-old Korean pilates instructor. She is completely nude, posing in a flexible stretch posture inside a sunlit minimalist penthouse loft. She has defined cat-like dark eyes, crisp jawline, and dark chestnut hair in a sleek high ponytail. Athletic hourglass physique with toned abdominal definition, long slender legs, and sculpted glutes. Bright morning sunlight casting warm diagonal rim lighting across her glowing glass-skin and perspiration sheen. Authentic skin pores, Hasselblad 85mm portrait, 8k resolution masterwork.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

```text
a stunning 24-year-old Korean pilates model named Han Minji with clear cat-like eyes, sleek dark chestnut hair, radiant glass-skin with a glistening athletic sheen, and a toned flexible athletic hourglass physique with subtle abdominal lines and long sculpted legs
```

---

## 6. 与 3D 姿态控制（方式 2）的适配性

韩敏智是针对 3D 骨骼控制（方式 2）的代表性角色。无论是下腰触足（`Bent over toe touch profile`）、大幅度深蹲（`Squatting Legs Spread`）还是跪姿后撑（`Kneeling Leaning Back`），其身材比例能完美契合 3D Mannequin 的骨骼刚体，彻底杜绝复杂拉伸动作中的 AI 四肢畸变。
