# 人物卡：[CN-12] 李清照 (Li Qingzhao) - 两宋风骨·千古词仙

- **卡片编号**：`CN-12`
- **时代分类**：两宋雅韵 (Song Dynasty)
- **原型灵感**：千古第一才女李清照（融合周迅年轻时的古灵精怪与诗书灵气、刘诗诗宋制汉服清雅素简神韵）
- **主打风格**：宋式极简美学 / 误入藕花深处微醺少女感 / 知性文人风骨 / 清瘦灵秀 / 水墨书斋闺秀
- **适配场景**：新中式茶室 (`prompts/scene_chinese_tearoom.txt`)、江南水阁临渊 (`prompts/scene_jiangnan_pavilion.txt`)、中式古典红木雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 李清照 (Li Qingzhao) | `intellectual spirited 23-year-old Song Dynasty poetess named Li Qingzhao` |
| **年龄 (Age)** | 23 岁（才华与灵气横溢） | `spirited youth 23 years old` |
| **时代与身份** | 宋代金石学者与词坛泰斗，号易安居士，华夏第一才女 | `Song Dynasty literati nobility, classical Chinese female scholar aesthetic` |
| **身高体态** | 166cm，体态清瘦修长、骨架清奇秀挺，兼具少女灵动与学者端雅 | `slender refined scholar frame, delicate sloping shoulders, graceful straight posture, light feminine curves` |
| **肤色基底** | 宋瓷般温润哑光的青白釉玉肌，白皙澄澈，带着极淡的书卷淡雅光华 | `smooth Celadon-jade matte porcelain skin, clean pale ivory complexion with delicate translucent glow` |
| **气质神态** | 眉宇间书香自华，眼波微醺流转带有一丝不羁的才气与狡黠，傲骨凌霜却又娇俏可爱 | `witty intelligent gaze, faint tipsy playful smile, aristocratic literary elegance, poised rebellious spirit` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：灵动如清泉的东方内双细杏眼，瞳眸清澈透亮，微醺时眼尾泛出极淡绯红，充满文人灵气。
  - *Prompt*: `bright lively dark almond eyes with intelligent sparkle, faint wine-kissed rosy blush at the outer corners, fine natural eyelashes, playfully piercing gaze`
- **眉型与鼻梁**：修长清秀的自然青黛细平眉；鼻梁清挺如笔，鼻尖秀气玲珑。
  - *Prompt*: `natural softly defined straight-arched dark eyebrows, slender elegant straight nose bridge with small refined tip`
- **唇型与面颊**：天生淡肉桂粉色花瓣小唇，唇角微微勾起一抹诗意浅笑，下颌线条秀丽干净。
  - *Prompt*: `delicate natural cinnamon-pink petal lips with a subtle poetic smile, smooth refined chin, pure intellectual facial contours`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：宋代标志性的素雅高耸发髻，插有一柄宋式白玉冠梳与一根极简银簪，几缕秀发微乱垂于耳侧。
  - *Prompt*: `refined classical Song Dynasty high chignon secured with an antique white nephrite crown comb and a slender silver hairpin, smooth glossy raven-black hair`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：宋代汝窑瓷器般的细腻哑光质感，微观毛孔清晰细微，肩颈与锁骨在纸窗漫射日光下呈现温润漫反射。
  - *Prompt*: `authentic human skin texture with microscopic pores, soft diffuse matte sheen like antique Song celadon porcelain, clean natural anatomical lighting`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：清瘦柔美的宋代文人审美：修长柔荑（指尖常伴研墨微痕）、纤细锁骨、不盈一握的楚腰与匀称纤直双腿。
  - *Prompt*: `gracefully slender silhouette, delicate prominent collarbones, extraordinarily narrow delicate waist, smooth flat belly, long slender legs, graceful calligrapher hands, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美刻画宋代极简清瘦骨相与真人体表） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，强化书斋私密写真与微醺氛围感） |
| **推理步数 (Steps)** | `45 - 50` | 保证玉梳发髻与青白釉皮肤质感完全呈现 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 清雅漫射自然光最佳平衡 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显宋代知性才女身姿 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定灵动眼眸与清丽五官 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证李清照的宋代才女风骨、宋式冠梳与微醺灵动神态：

```text
A hyper-realistic full-body masterwork studio portrait of Li Qingzhao, an intellectual 23-year-old Song Dynasty female poet. She is completely nude, sitting in an elegant cross-legged scholar pose on a woven tatami reed mat next to a low black lacquer inkstone desk against a plain rice-paper screen. She has a high Song Dynasty chignon secured with an antique white jade comb, lively dark almond eyes with an intelligent sparkle and faint wine blush at her eye corners, and delicate cinnamon-pink lips with a playful half-smile. Her body is lithe and gracefully slender with prominent collarbones, a tiny flexible waistline, and slender hands with calligrapher poise. Soft morning sunlight filtering through the bamboo lattice illuminates her celadon-pale porcelain skin, highlighting microscopic pores, subtle natural subsurface scattering, and soft anatomical shadows. Timeless oriental literary grace, 8k resolution, Hasselblad 80mm portrait photograph.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
an intellectual spirited 23-year-old Song Dynasty poetess named Li Qingzhao with high Song chignon and white jade comb, bright lively dark almond eyes with faint wine-blush at corners, delicate cinnamon-pink lips with a playful subtle smile, possessing a gracefully slender scholar frame with prominent collarbones, narrow waist, and smooth celadon-matte porcelain skin with authentic fine pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：新中式禅意茶室 (`prompts/scene_chinese_tearoom.txt`)
将 `Li Qingzhao` 模块化词块嵌入古雅茶室，化身茶香墨韵中的千古才女：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle photograph of an intellectual spirited 23-year-old Song Dynasty poetess named Li Qingzhao with high Song chignon and white jade comb, bright lively dark almond eyes with faint wine-blush at corners, delicate cinnamon-pink lips with a playful subtle smile, possessing a gracefully slender scholar frame with prominent collarbones, narrow waist, and smooth celadon-matte porcelain skin with authentic fine pores inside an elegant minimalist modern tea pavilion. She is completely nude, sitting on a woven tatami floor cushion next to a low black walnut tea table. The camera shoots from the floor level looking up at her figure: she is kneeling with her knees gently parted, one hand gracefully resting on the edge of the tea tray near a steaming purple clay teapot, her other hand placed on her thigh. Warm diffuse light shines through a translucent rice-paper wooden lattice screen behind her, casting subtle bamboo shadows and outlining her silhouette. Gentle swirls of tea steam rise into the air. The low angle naturally frames the distinct contours of her lower anatomy in the center between her parted thighs. 8k resolution, cinematic warm atmospheric lighting, photorealistic anatomy.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn12_li_qingzhao `
  --prompt "A hyper-realistic, low-angle photograph of an intellectual spirited 23-year-old Song Dynasty poetess named Li Qingzhao with high Song chignon and white jade comb, bright lively dark almond eyes with faint wine-blush at corners, delicate cinnamon-pink lips with a playful subtle smile, possessing a gracefully slender scholar frame with prominent collarbones, narrow waist, and smooth celadon-matte porcelain skin with authentic fine pores inside an elegant minimalist modern tea pavilion. She is completely nude, sitting on a woven tatami floor cushion next to a low black walnut tea table. The camera shoots from the floor level looking up at her figure: she is kneeling with her knees gently parted, one hand gracefully resting on the edge of the tea tray near a steaming purple clay teapot, her other hand placed on her thigh. Warm diffuse light shines through a translucent rice-paper wooden lattice screen behind her, casting subtle bamboo shadows and outlining her silhouette. Gentle swirls of tea steam rise into the air. The low angle naturally frames the distinct contours of her lower anatomy in the center between her parted thighs. 8k resolution, cinematic warm atmospheric lighting, photorealistic anatomy." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn12_li_qingzhao_tearoom.png
```
