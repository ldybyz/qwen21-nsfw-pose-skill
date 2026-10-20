# 人物卡：[CN-11] 武明空 (Wu Mingkong) - 大周天后·至尊红颜

- **卡片编号**：`CN-11`
- **时代分类**：大周武唐 (Wu Zhou Dynasty / Imperial Court)
- **原型灵感**：一代女皇武则天（融合刘晓庆经典版与贾静雯《至尊红颜》至尊帝王霸气与成熟艳丽神韵）
- **主打风格**：日月当空 / 至尊红颜 / 凤目含威 / 帝王气场与成熟丰腴肉感 / 金顶暖阁雍容
- **适配场景**：中式古典红木雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)、私汤温泉 (`prompts/scene_onsen_hotspring.txt`)、新中式茶室 (`prompts/scene_chinese_tearoom.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 武明空 (Wu Mingkong) | `commanding magnificent 28-year-old Tang Dynasty Empress named Wu Mingkong` |
| **年龄 (Age)** | 28 岁（成熟风华巅峰） | `mature sovereign 28 years old` |
| **历史渊源** | 华夏历史唯一正统女皇帝，自名“曌”，君临天下，四海臣服 | `sole reigning Empress of ancient China, Wu Zetian archetype` |
| **身高体态** | 172cm，挺拔修长且极具成熟肉感美：饱满酥胸、挺拔端庄脊梁、圆润肉感丰臀 | `tall 172cm commanding mature hourglass figure, majestic posture, full bust, rounded regal hips` |
| **肤色基底** | 暖润如羊脂白玉，常年御用宫廷养颜秘方，白皙中泛着淡淡的琥珀金光与血色 | `luminous warm porcelain skin with rich amber undertone and healthy royal flush` |
| **气质神态** | 凤目含威、唯我独尊，眼神深邃锐利能洞察人心，霸气中透着致命的成熟女性侵略性 | `commanding piercing phoenix gaze, regal dominant poise, intense magnetic matriarchal aura` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：极其霸气的长型丹凤眼，眼尾微扬，黑白分明，透出掌控一切的冷峻与威严。
  - *Prompt*: `commanding sharp dark phoenix eyes with penetrating dominant gaze, intense intelligent pupils, long defined dark eyelashes`
- **眉型与额相**：高挑斜飞入鬓的帝王剑眉；额心饱满，绘有象征至高皇权的赤金九尾凤羽花钿。
  - *Prompt*: `regal high-arched sword-shaped dark eyebrows, imperial crimson and gold phoenix-feather huadian crest painted on her smooth forehead`
- **唇型与面颊**：饱满朱红帝王烈焰红唇，唇角微启带着从容掌控的冷笑，下颌线条高贵端庄。
  - *Prompt*: `luscious deep imperial crimson lips with sharp contours slightly curled in a self-assured faint smirk, noble sculpted jawline`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：九龙九凤冠卸下后半挽的大周帝王高髻，浓密乌黑长发如黑瀑般披落于赤裸香肩与脊背，散发着沉香木与龙涎香的贵气。
  - *Prompt*: `partially released magnificent imperial chignon, long cascading heavy glossy black hair flowing across bare shoulders, adorned with single antique golden dragon hairpin`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：细腻温热的真实皮肤微毛孔质感，锁骨深邃，胸前与腰腹在宫廷明黄烛光下反射出尊贵的金色微光。
  - *Prompt*: `authentic human skin texture with micro-pores, rich golden candlelight specular highlights over collarbones, generous bust, and regal arched back`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：极具压迫感与征服感的成熟丰腴沙漏身材：挺拔宽阔的御姐骨架、紧致微弧的腹部、圆润丰满的臀腿。
  - *Prompt*: `tall voluptuous mature female silhouette, majestic broad shoulders, generous natural bust, firm curved waist, rounded full hips, smooth toned thighs, authentic female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（精准雕琢成熟女性丰满肉身与帝王骨骼比例） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.85`（搭配 CFG 4.0，强化龙榻烛光下的私密与威严质感） |
| **推理步数 (Steps)** | `45 - 50` | 保证凤羽花钿与霸气眼神完全收敛 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 浓郁金黄暖调光影的最佳表现 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显 172cm 帝王身段与至尊威严 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定女帝面部五官与凤目威严 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证武明空的帝王凤目、凤羽花钿与成熟霸气身段：

```text
A hyper-realistic full-body masterwork studio portrait of Wu Mingkong, a commanding 28-year-old sovereign Empress of ancient China. She is completely nude, sitting in a dominant, regal posture on an intricately carved golden sandalwood throne draped with imperial crimson silk. She has heavy cascading glossy black hair loosely pinned with a gold dragon hairpin, intense piercing dark phoenix eyes with an aura of supreme power, a gold and crimson phoenix-feather huadian painted on her forehead, and deep crimson lips with a faint self-assured smirk. Her frame is tall at 172cm with mature voluptuous curves, full bosom, and rounded hips. Dramatic warm golden lantern light illuminates her figure from a three-quarter angle, accentuating authentic skin pores, rich amber specular highlights along her throat and collarbones, and deep sculpted anatomical shadows. Supreme imperial Chinese matriarch, 8k resolution, Hasselblad 100mm medium format photograph.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a commanding magnificent 28-year-old Tang Dynasty Empress named Wu Mingkong with heavy cascading glossy black hair, piercing dominant dark phoenix eyes, crimson and gold phoenix huadian painted on her forehead, deep imperial crimson lips, possessing a tall 172cm mature voluptuous hourglass silhouette with full bosom, rounded hips, and luminous warm porcelain skin with rich amber candlelight sheen and authentic micro-pores
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：中式古典红木雕花拔步床 (`prompts/scene_chinese_canopy_bed.txt`)
将 `Wu Mingkong` 模块化词块嵌入龙凤暖阁拔步床：

#### 合成完整 Prompt：
```text
A hyper-realistic, low-angle wide shot of a commanding magnificent 28-year-old Tang Dynasty Empress named Wu Mingkong with heavy cascading glossy black hair, piercing dominant dark phoenix eyes, crimson and gold phoenix huadian painted on her forehead, deep imperial crimson lips, possessing a tall 172cm mature voluptuous hourglass silhouette with full bosom, rounded hips, and luminous warm porcelain skin with rich amber candlelight sheen and authentic micro-pores. She is completely nude, seated dominantly on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing the camera with head held high and knees spread apart, one hand resting firmly on the edge of the carved frame. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn11_wu_mingkong `
  --prompt "A hyper-realistic, low-angle wide shot of a commanding magnificent 28-year-old Tang Dynasty Empress named Wu Mingkong with heavy cascading glossy black hair, piercing dominant dark phoenix eyes, crimson and gold phoenix huadian painted on her forehead, deep imperial crimson lips, possessing a tall 172cm mature voluptuous hourglass silhouette with full bosom, rounded hips, and luminous warm porcelain skin with rich amber candlelight sheen and authentic micro-pores. She is completely nude, seated dominantly on a traditional woven bamboo mat atop a massive dark rosewood Chinese canopy bed. Translucent crimson and amber silk curtains drape softly around the bedposts, slightly parted. She is facing the camera with head held high and knees spread apart, one hand resting firmly on the edge of the carved frame. Warm golden lantern light from a bedside carved wooden lamp illuminates her front, casting soft romantic shadows along her collarbones, ribs, and inner thighs, while incense smoke drifts in lazy tendrils through the bedframe. The low perspective looks slightly upward, capturing the clear, authentic anatomical detail of her lower body centered naturally between her parted knees against the lustrous silk bedding. 8k resolution, cinematic candlelit atmosphere, rich cultural texture." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn11_wu_mingkong_canopy.png
```
