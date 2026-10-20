# 人物卡模板 (Character Card Template)

> **使用说明**：复制本模板并在对应分类目录（如 `east_asian/`, `caucasian/`, `latina/` 等）中重命名为 `<character_id>.md`。按提示填写中英文说明与提示词。

---

# 人物卡：[中文名] ([英文名]) - [人设风格代号]

- **卡片编号**：[例如：EA-05 / CA-05]
- **人物归属**：[例如：东亚系 East Asian / 欧美高加索系 Caucasian / 拉丁系 Latina / 非裔 African]
- **主打风格**：[例如：清纯学院风 / 哥特暗黑 / 运动健美 / 贵气名媛]

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | [中文名] / [英文名] | [English Name / Epithet] |
| **年龄 (Age)** | [例如：22 岁] | `young 22-year-old woman` |
| **国籍/血统** | [例如：中国江南 / 瑞典斯德哥尔摩] | `Chinese` / `Scandinavian Swedish` |
| **身高体态** | [例如：168cm, 匀称轻微曲线] | `168cm, slender frame, delicate feminine curves` |
| **肤色基底** | [例如：冷白皮 / 暖调象牙白 / 蜜糖小麦色] | `fair porcelain pale skin, subtle warm undertone` |
| **气质关键词** | [例如：清冷、优雅、若即若离] | `serene, delicate, graceful, ethereal gaze` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：[眼型与瞳色，例如：杏眼、深棕色瞳孔、浓密睫毛、含蓄柔光]
  - *Prompt*: `almond-shaped dark brown eyes with delicate eyeliner, naturally dense eyelashes, soft captivating gaze`
- **眉鼻**：[眉形与鼻型，例如：柳叶细眉、小巧挺直的鼻梁]
  - *Prompt*: `fine softly-arched eyebrows, elegant slender straight nose bridge`
- **唇齿与神态**：[唇形与表情，例如：饱满樱唇微启、神情慵懒清冷]
  - *Prompt*: `plump naturally pink lips slightly parted, serene relaxed expression`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：[长度与造型，例如：中分披肩、波浪长发、齐耳利落短发]
- **发色光泽**：[颜色与反光，例如：深黑曜石光泽、微风吹拂丝发分明]
  - *Prompt*: `luxurious long silky jet-black straight hair falling gracefully past her shoulders, individual strands catching soft highlights`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：[真实微毛孔、皮肤微透光、锁骨反光、水光感]
  - *Prompt*: `authentic authentic human skin texture with microscopic pores, natural subsurface scattering, soft diffuse sheen along collarbones and shoulders, unblemished complexion`

### 2.4 身材比例与解剖结构 (Physique & Anatomy)
- **身段比例**：[肩宽、腰围、臀腿线条、锁骨线条]
  - *Prompt*: `slender waist, gentle feminine hip curve, elegant collarbones, smooth toned legs, natural anatomical proportions`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重推荐 `1.0`，主打清晰解剖学细节与真实皮肤质感 |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重推荐 `0.8`（需搭配 CFG 4.0），突出网红真实质感与私密感 |
| **推理步数 (Steps)** | `45 - 50` | 保证细节完全收敛 |
| **引导系数 (CFG)** | `2.5` (搭配 tawsLoRa) / `4.0` (搭配 TheseAlpacas) | 遵循模型推荐基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | Qwen-Image 2.1 推荐最佳画质组合 |
| **推荐生图尺寸** | `1152x1728` (竖构图) / `1344x768` (横构图) | 匹配高画质渲染与人像全身表现 |
| **推荐负面词** | `blurry, deformed, bad anatomy, bad hands, plastic skin` | 可选，配合 TheseAlpacas 强烈建议加入 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **用途**：开箱即用，用于在纯白棚拍/极简自然光下独立验证该角色的面部还原度、五官一致性与身体特征。

```text
A hyper-realistic full-body fashion studio portrait of [English Name], a [Age]-year-old [Ethnicity] woman. She is completely nude, standing in an elegant contrapposto posture against a clean warm-toned minimalist plaster wall. She has [Facial details], [Hair details], and [Skin details]. Her body is [Body proportions and curves]. Soft cinematic north-window diffuse lighting sculpting her facial contours and highlighting her collarbones, smooth waistline, and delicate curves. Authentic photorealistic skin texture with visible fine pores, soft specular sheen, and natural anatomy. 8k resolution, cinematic color grading, masterwork, Hasselblad 80mm photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **用途**：已提炼好的纯人物描述模块，可直接复制替换 `prompts/scene_*.txt` 中的主体角色描述。

```text
a gorgeous [Age]-year-old [Ethnicity] woman ([English Name]) with [Facial features], [Hair styling], and [Skin tone/texture], featuring a [Body description]
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：[场景名称，如：新中式茶室 / 私汤温泉 / 落地窗伸展]
- **原场景提示词**：`prompts/scene_xxx.txt`
- **合成后完整 Prompt**：
```text
[将模块化主体词块嵌入原场景镜头与环境后的完整 Prompt]
```

### 快速执行命令 (PowerShell / Bash)
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_test_example `
  --prompt "[填入上述完整 Prompt]" `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/example.png
```
