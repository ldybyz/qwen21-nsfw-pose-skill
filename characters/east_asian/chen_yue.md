# 人物卡：陈悦 (Chen Yue) - 都市清冷高骨相御姐

- **卡片编号**：`EA-02`
- **人物归属**：东亚系 (East Asian / 现代都市)
- **主打风格**：清冷禁欲 / 骨相超模 / 高级厌世脸 / 现代摩登线条
- **适配场景**：落地窗晨曦、深夜厨房、赛博雨夜阳台、镜前私密自拍

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 陈悦 (Chen Yue) | `chic 26-year-old modern East Asian woman named Chen Yue` |
| **年龄 (Age)** | 26 岁 | `26 years old` |
| **文化背景** | 现代国际都市独立女性，高定时装模特/艺术总监 | `modern metropolitan high-fashion aesthetic` |
| **身高体态** | 175cm，九头身修长超模比例，清晰锁骨与直角肩，微肌腹线 | `tall 175cm, high-fashion slender proportions, defined collarbones, sharp square shoulders, athletic waistline` |
| **肤色基底** | 象牙冷调白皙，干净通透，微哑光高级质感 | `cool ivory porcelain skin with a smooth editorial satin finish` |
| **气质神态** | 清冷疏离，不屑一顾的高级厌世感，眉宇英气，神情内敛自信 | `haute-couture aloof expression, sharp piercing gaze, sophisticated composure, slightly parted confident lips` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：微挑的修长丹凤眼，深墨黑色瞳仁，眼尾锋利上扬，眼神深邃锐利。
  - *Prompt*: `elongated feline dark eyes with a slight upward tilt, sharp eyeliner contour, intense cool piercing gaze`
- **眉型与鼻骨**：立体利落野生平剑眉，高挺笔直的骨感鼻梁，下颌角清晰转折，颧骨微高有雕塑感。
  - *Prompt*: `defined straight architectural eyebrows, high straight sculpted nose bridge, prominent high cheekbones and sharp chiseled jawline`
- **唇型与面部构架**：薄而锋利的裸色唇线，唇峰清晰，冷淡微阖。
  - *Prompt*: `well-defined nude rose lips with crisp Cupid's bow, slightly relaxed aloof pout, elegant model-tier bone structure`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：三七侧分利落齐肩黑色短直发（Bob / Lob），发尾剪裁干净利落，一侧掖于耳后露出耳廓与下颌线。
  - *Prompt*: `sleek side-parted shoulder-length jet-black blunt bob hair, sharp razor-cut ends, one side neatly tucked behind ear revealing chiseled neck and jawline`

### 2.3 肤质纹理与微观细节 (Skin Texture & Micro Details)
- **表皮质感**：现代时尚大片级别的真实肤质，细腻皮脂漫射光，锁骨凹陷与肋骨边缘有极佳的光影明暗对比。
  - *Prompt*: `high-end editorial skin texture with visible fine pores, subtle natural specularity along shoulders and collarbone ridges, clean unblemished satin complexion`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **体型特征**：高挑纤长，四肢修长，马甲线若隐若现，紧致的臀腿线条与挺拔脊柱曲线。
  - *Prompt*: `tall statuesque silhouette, defined taut abdomen with subtle ab crack, toned long slender legs, sharp pelvic bones, authentic human anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，特别适合捕捉真实模特私密质感与骨相） |
| **推荐 LoRA 2** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（CFG 2.5，极致的人体解剖学细节刻画） |
| **推理步数 (Steps)** | `45` | 高细节收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 视 LoRA 选择匹配 |
| **采样器 / 调度器** | `er_sde` / `beta` | 细腻光影渲染 |
| **生图分辨率** | `1152x1728` | 完美呈现超模修长九头身比例 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：高反差现代影棚打光，测试陈悦的利落短发、厌世高级脸与高挑身段：

```text
A hyper-realistic full-length editorial fashion photograph of Chen Yue, a stunning 26-year-old East Asian high-fashion model. She is completely nude, standing tall in an asymmetrical architectural pose against a dark charcoal concrete wall in a minimalist loft. She has a sleek side-parted jet-black blunt bob hair tucked behind one ear, elongated feline dark brown eyes with an aloof piercing gaze, high sculpted cheekbones, a sharp chiseled jawline, and natural nude lips. The shot showcases her tall 175cm statuesque silhouette, sharp square shoulders, deeply defined collarbones, toned taut stomach, and long slender legs. Strong cinematic directional key light from the side creates dramatic chiaroscuro shadows across her facial structure and body contours. Authentic skin texture with natural fine pores, realistic matte skin finish. 8k resolution, Masterpiece, Hasselblad medium format photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接替换任意 `prompts/scene_*.txt` 中的主体描述部分。

```text
a tall 26-year-old East Asian high-fashion model named Chen Yue, featuring a sleek side-parted jet-black blunt bob hair, sharp sculpted cheekbones, elongated feline dark eyes with an aloof cool gaze, chiseled jawline, and nude lips, with a 175cm statuesque slender frame, defined square shoulders, prominent collarbones, taut toned abdomen, and cool ivory satin skin with fine authentic pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 示例场景：深夜厨房·冰箱冷光 (`prompts/scene_midnight_kitchen.txt`)
将 `Chen Yue` 模块化词块注入深夜厨房场景，极冷色温与清冷骨相的完美碰撞：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle photograph of a tall 26-year-old East Asian high-fashion model named Chen Yue in a pitch-black luxury penthouse kitchen at 2:00 AM. She is completely nude, leaning down toward an open stainless-steel refrigerator. She features a sleek side-parted jet-black blunt bob hair tucked behind one ear, sharp sculpted cheekbones, elongated dark feline eyes with an aloof gaze, a chiseled jawline, and a statuesque slender frame with prominent collarbones and a taut toned abdomen. The camera shoots from the dark polished slate floor looking up: she is captured in a slight squat, reaching for a glass bottle. The intense cold white LED light spilling from inside the refrigerator serves as the sole dramatic key light in the pitch-dark room, brilliantly illuminating the high-contrast contours of her face, shoulders, waistline, and slender legs. Authentic editorial skin texture with visible microscopic pores and crisp specular highlights. 8k resolution, cinematic chiaroscuro lighting, photorealistic anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_ea02_kitchen `
  --prompt "A hyper-realistic, low-angle photograph of a tall 26-year-old East Asian high-fashion model named Chen Yue in a pitch-black luxury penthouse kitchen at 2:00 AM. She is completely nude, leaning down toward an open stainless-steel refrigerator. She features a sleek side-parted jet-black blunt bob hair tucked behind one ear, sharp sculpted cheekbones, elongated dark feline eyes with an aloof gaze, a chiseled jawline, and a statuesque slender frame with prominent collarbones and a taut toned abdomen. The camera shoots from the dark polished slate floor looking up: she is captured in a slight squat, reaching for a glass bottle. The intense cold white LED light spilling from inside the refrigerator serves as the sole dramatic key light in the pitch-dark room, brilliantly illuminating the high-contrast contours of her face, shoulders, waistline, and slender legs. Authentic editorial skin texture with visible microscopic pores and crisp specular highlights. 8k resolution, cinematic chiaroscuro lighting, photorealistic anatomy." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/ea02_chen_yue_kitchen.png
```
