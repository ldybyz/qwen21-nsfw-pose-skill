# 人物卡：[CN-01] 赵凌燕 (Zhao Lingyan) - 汉宫绝色·掌上飞燕

- **卡片编号**：`CN-01`
- **时代分类**：汉代宫廷 (Han Dynasty)
- **原型灵感**：赵飞燕（融合佟丽娅《母仪天下》汉宫第一美人绝尘神韵）
- **主打风格**：掌上轻舞 / 楚腰纤细 / 清绝冷艳 / 汉宫凝脂仙姿
- **适配场景**：汉宫暖阁、幽篁竹林 (`prompts/scene_bamboo_courtyard.txt`)、古典闺房拔步床 (`prompts/scene_chinese_canopy_bed.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 赵凌燕 (Zhao Lingyan) | `ethereal 21-year-old Han Dynasty noblewoman named Zhao Lingyan` |
| **年龄 (Age)** | 21 岁 | `young 21 years old` |
| **时代与身份** | 汉代宫廷绝代舞姬与宠妃，身轻若燕，名动天下 | `Han Dynasty royal court dancer, classical ancient Chinese aesthetic` |
| **身高体态** | 165cm，极致纤细轻盈（掌中轻盈），腰肢纤细柔荑，肩骨削平如刃 | `exceptionally slender and feather-light frame, wasp waist, delicate sloping shoulders, graceful dancer posture` |
| **肤色基底** | 凝脂冷玉白，带有月光般的冷调通透微光 | `translucent alabaster fair skin, moonlit porcelain tone with natural soft glow` |
| **气质神态** | 眉间清冷高绝，顾盼神飞，回眸极尽媚态却又疏离孤傲 | `breathtaking alluring yet distant gaze, subtle haughty charm, captivating phoenix eyes` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：东方极品丹凤眼微扬，眼尾似刀裁般微挑，眼眸清冽如深潭寒水，长睫如蝶翼扑朔。
  - *Prompt*: `exquisite upturned phoenix eyes with subtle alluring eye-wings, deep obsidian dark pupils, naturally fine long eyelashes, mesmerizing piercing yet graceful gaze`
- **眉型与鼻梁**：远山长翠细蛾眉，琼鼻秀挺笔直，鼻尖精致小巧带有一丝孤傲。
  - *Prompt*: `delicate elongated willow-leaf crescent eyebrows, perfectly straight aristocratic slender nose bridge with a delicate tip`
- **唇型与面颊**：饱满朱唇色若熟樱，唇峰清晰如菱角，唇瓣微启含情带怨；下颌线条精致如画。
  - *Prompt*: `crimson ruby petal-shaped lips with sharply defined Cupid's bow, slightly parted lips, razor-sharp delicate jawline, soft rose flush on high cheekbones`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：汉代垂鬟分髾高盘髻，几缕乌黑青丝垂落于胸前与玉颈，饰有精致的汉代金错玉簪。
  - *Prompt*: `elaborate classical Han Dynasty high topknot with delicate flowing locks draping across bare shoulders and collarbones, adorned with a delicate antique jade hairpin, lustrous jet-black hair`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：羊脂白玉般的极致通透感，真实微毛孔清晰可辨，锁骨与背脊反衬柔和的月华漫射光。
  - *Prompt*: `authentic fine human skin texture with microscopic pores, soft subsurface scattering, luminous porcelain sheen on sharp collarbones and smooth spine, natural skin elasticity`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：纤手柔荑，楚腰盈盈一握，小腹平坦微陷，双腿笔直修长如仙鹤，足弓弧度优美极致。
  - *Prompt*: `hyper-slender dancer physique, delicate prominent collarbones, extraordinarily narrow wasp waistline, gentle rounded feminine hips, long toned slender legs, arched delicate bare feet, genuine female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（首选，完美刻画汉式古典骨相与私密解剖轮廓） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，强化肌肤微汗与微观质感） |
| **推理步数 (Steps)** | `45 - 50` | 保证汉风发髻、微挑凤眼与骨肉光影完全收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循模型平衡 |
| **采样器 / 调度器** | `er_sde` / `beta` | 最佳质感与柔光漫射组合 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显修长体态与舞姿动态张力 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定五官与修长肢体表现 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证赵凌燕的汉代绝色容颜、丹凤眼神态与纤细如燕的身姿：

```text
A hyper-realistic full-body masterwork studio portrait of Zhao Lingyan, an exquisite 21-year-old Han Dynasty noblewoman and imperial dancer. She is completely nude, posing in a dynamic, graceful classical Chinese dancer contrapposto stance against a minimalist antique off-white silk scroll backdrop. She has an intricate Han Dynasty high coiffure with flowing raven-black strands across her bare chest, piercing upturned phoenix eyes with captivating allure, perfectly defined Cupid's bow crimson lips slightly parted, and an extraordinarily slender frame featuring a tiny wasp waist and delicate sharp collarbones. Soft diffused moonlit lantern lighting sculpts her porcelain white skin, revealing microscopic pores, natural soft subsurface scattering, and dewy highlights along her spine and slender thighs. Authentic photorealistic anatomy, breathtaking oriental aesthetic, 8k resolution, Hasselblad 80mm medium format photograph.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
an exquisite 21-year-old Han Dynasty noblewoman named Zhao Lingyan with piercing upturned phoenix eyes, sharply defined crimson lips slightly parted, elaborate classical Han topknot with flowing jet-black strands over her shoulders, possessing an extraordinarily slender dancer frame with a wasp waist, sharp delicate collarbones, and luminous porcelain alabaster skin with subtle authentic pores and dewy sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：幽篁竹林私密水阁 (`prompts/scene_bamboo_courtyard.txt`)
将 `Zhao Lingyan` 模块化词块嵌入竹林月夜场景：

#### 合成完整 Prompt：
```text
A hyper-realistic wide-angle cinematic shot of an exquisite 21-year-old Han Dynasty noblewoman named Zhao Lingyan with piercing upturned phoenix eyes, sharply defined crimson lips slightly parted, elaborate classical Han topknot with flowing jet-black strands over her shoulders, possessing an extraordinarily slender dancer frame with a wasp waist, sharp delicate collarbones, and luminous porcelain alabaster skin with subtle authentic pores. She is completely nude, seated in a flexible kneeling arched posture on a smooth dark river-stone terrace in an ancient moonlit courtyard surrounded by towering emerald bamboo stalks. One slender arm is extended touching a mossy rock, her back gracefully arched to highlight her slender spine and feminine curves. Pale cool moonlight filters through the bamboo leaves, casting intricate dancing dappled shadow patterns across her alabaster skin. Subtle water mist rises from a shallow stone reflecting pool in front of her. The low camera angle captures the soft contours of her lower anatomy naturally illuminated by the ambient moonlit water reflections. 8k resolution, atmospheric mist, photorealistic anatomy, cinematic lighting.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn01_zhao_lingyan `
  --prompt "A hyper-realistic wide-angle cinematic shot of an exquisite 21-year-old Han Dynasty noblewoman named Zhao Lingyan with piercing upturned phoenix eyes, sharply defined crimson lips slightly parted, elaborate classical Han topknot with flowing jet-black strands over her shoulders, possessing an extraordinarily slender dancer frame with a wasp waist, sharp delicate collarbones, and luminous porcelain alabaster skin with subtle authentic pores. She is completely nude, seated in a flexible kneeling arched posture on a smooth dark river-stone terrace in an ancient moonlit courtyard surrounded by towering emerald bamboo stalks. One slender arm is extended touching a mossy rock, her back gracefully arched to highlight her slender spine and feminine curves. Pale cool moonlight filters through the bamboo leaves, casting intricate dancing dappled shadow patterns across her alabaster skin. Subtle water mist rises from a shallow stone reflecting pool in front of her. The low camera angle captures the soft contours of her lower anatomy naturally illuminated by the ambient moonlit water reflections. 8k resolution, atmospheric mist, photorealistic anatomy, cinematic lighting." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn01_zhao_lingyan_bamboo.png
```
