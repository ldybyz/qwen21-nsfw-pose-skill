# 人物卡：[CN-02] 杨玉瑶 (Yang Yuyao) - 盛唐国色·贵妃雍容

- **卡片编号**：`CN-02`
- **时代分类**：盛唐帝国 (Tang Dynasty)
- **原型灵感**：杨贵妃（融合殷桃 / 范冰冰盛唐贵妃丰盈、金钿牡丹、回眸百媚生的盛世雍容神韵）
- **主打风格**：盛唐国色 / 丰腴润泽 / 雍容华贵 / 额绘金红牡丹花钿 / 凝脂如雪
- **适配场景**：新中式茶室 (`prompts/scene_chinese_tearoom.txt`)、古典闺房拔步床 (`prompts/scene_chinese_canopy_bed.txt`)、私汤温泉 (`prompts/scene_onsen_hotspring.txt`)

---

## 1. 核心档案设定 (Core Persona Profile)

| 属性维度 | 设定内容 | 英文提示词映射 (Prompt Mapping) |
| :--- | :--- | :--- |
| **全名 (Name)** | 杨玉瑶 (Yang Yuyao) | `voluptuous regal 24-year-old Tang Dynasty imperial consort named Yang Yuyao` |
| **年龄 (Age)** | 24 岁 | `prime youth 24 years old` |
| **时代与身份** | 盛唐宫廷绝代贵妃，倾国倾城，六宫粉黛无颜色 | `opulent Tang Dynasty imperial nobility, golden age Chinese royal consort` |
| **身高体态** | 168cm，极富女性魅力的丰腴匀称沙漏身材（环肥燕瘦），肌肤丰盈紧致，胸臀饱满 | `voluptuous feminine hourglass silhouette, supple soft curves, full bosom, rounded hips, luxurious sensual proportions` |
| **肤色基底** | 温泉水滑洗凝脂，白皙温润如羊脂暖玉，微透极淡蜜桃粉晕 | `warm porcelain ivory skin with delicate peachy rose undertones, radiant dewy luster` |
| **气质神态** | 雍容华贵中带着天然的慵懒娇憨，桃花醉目，回眸一笑百媚丛生 | `languid sensual expression, intoxicating peach-blossom eyes, regal aristocratic poise, subtle seductive smile` |

---

## 2. 视觉特征与解剖细节解构 (Visual Breakdown)

### 2.1 面部与五官 (Facial Anatomy & Expressions)
- **眼部**：眼尾略向下后微翘的极品桃花醉眼，波光潋滟，瞳仁黑润如墨玉，眼神如醉似醒。
  - *Prompt*: `alluring peach-blossom shaped dark brown eyes with soft dewy luster, slightly misty intoxicating gaze, gentle eye curves, dark dense lashes`
- **眉型、面靥与花钿**：唐代经典宽远山螺子黛眉；额心手绘一朵精致炽烈的赤金牡丹花钿；颊边各点一粒极小红靥。
  - *Prompt*: `elegant softly-arched Tang Dynasty smoked-charcoal eyebrows, an intricate crimson and gold peony huadian bindi pattern painted on her forehead, two tiny vermilion dimple dots on her plump cheeks`
- **唇型与面颊**：饱满如初绽玫瑰花瓣的花瓣唇，唇珠圆润饱满，唇色朱砂微艳微启。
  - *Prompt*: `plump luscious rosebud lips glistening with natural sheen, soft rounded jawline, full radiant cheeks flushed with healthy vitality`

### 2.2 发型发质与颜色 (Hair Quality & Styling)
- **发型结构**：唐代高耸巍峨的高髻（牡丹髻/望仙髻），插缀精致的金步摇与红玛瑙流苏，几缕鬓发微湿贴于雪白颈侧。
  - *Prompt*: `magnificent Tang Dynasty high chignon coiffure crowned with antique ornate golden phoenix hairpins and dangling red agate tassels, glossy jet-black hair with silky texture`

### 2.3 肤质纹理与微观细节 (Skin Texture & Specular Highlights)
- **表皮质感**：如凝脂温玉，体表散发着微微的温热光泽，细微毛孔与皮肤微反光自然真实，锁骨与饱满胸前光泽如丝绸。
  - *Prompt*: `authentic human skin texture with microscopic pores, warm dewy subsurface scattering, soft silky specular sheen across plump chest, shoulders, and rounded curves`

### 2.4 身材比例与解剖特征 (Physique & Anatomy)
- **身段比例**：盛唐审美之大成——丰而不肥，骨肉匀停，腰肢微收曲线明显，丰盈饱满的双峰与圆润饱满的蜜桃臀，极具成熟东方肉感美。
  - *Prompt*: `sensual voluptuous proportions, soft supple waist with gentle feminine flesh, generous bustline, full rounded hips, smooth firm thighs, authentic natural female anatomy`

---

## 3. 推荐推理参数与 LoRA 适配 (Recommended Parameters)

| 参数项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| **推荐 LoRA 1** | `qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors` | 权重 `1.0`（完美雕琢盛唐丰腴肉感与细腻真实解剖） |
| **推荐 LoRA 2** | `thesealpacas-nsfw-v2.safetensors` | 权重 `0.8`（搭配 CFG 4.0，极度突出水光肌与温泉慵懒感） |
| **推理步数 (Steps)** | `45 - 50` | 保证花钿细节与华贵温润光影完全呈现 |
| **引导系数 (CFG)** | `2.5` (tawsLoRa) / `4.0` (TheseAlpacas) | 遵循基准 |
| **采样器 / 调度器** | `er_sde` / `beta` | 温暖柔润色调的最佳表现 |
| **生图分辨率** | `1152x1728` (竖版人像) | 突显饱满体态与雍容华服脱落后的肉感张力 |
| **Seed 推荐** | `80964` 或 `124880844757561` | 稳定盛唐面部特征与丰润体型 |

---

## 4. 独立基准测试提示词 (Standalone Benchmark Prompt)

> **直接运行**：用于验证杨玉瑶的盛唐面部花钿、桃花醉目与丰腴曼妙体态：

```text
A hyper-realistic full-body masterwork studio portrait of Yang Yuyao, a magnificent 24-year-old Tang Dynasty imperial consort. She is completely nude, reclining languidly on a rich imperial crimson velvet chaise lounge against a warm gilded sandalwood screen. She has an intricate Tang Dynasty high chignon adorned with golden phoenix ornaments, a detailed crimson and gold peony huadian painted on her forehead, intoxicating misty peach-blossom eyes, and luscious plump red lips. Her body is voluptuous and beautifully proportioned with soft supple curves, full rounded hips, and generous feminine fullness. Warm glowing lantern light casts a rich amber glow over her smooth ivory porcelain skin, highlighting microscopic pores, subtle dewy perspiration, and soft natural subsurface scattering across her chest and torso. Authentic photorealistic anatomy, lavish imperial aesthetic, 8k resolution, Hasselblad medium format photography.
```

---

## 5. 模块化主体描述词块 (Modular Insertion Block)

> **复制替换说明**：将下列英文字块直接嵌入 `prompts/scene_*.txt` 中的主体角色描述：

```text
a voluptuous 24-year-old Tang Dynasty imperial consort named Yang Yuyao with intoxicating peach-blossom eyes, crimson and gold peony huadian painted on her forehead, luscious plump rose lips, magnificent high Tang coiffure with gold ornaments, possessing a sensual voluptuous hourglass figure with full natural curves, rounded hips, and luminous warm ivory skin with dewy micro-pores and soft specular sheen
```

---

## 6. 与现有场景混搭实战示例 (Scene Blending Showcase)

### 搭配场景：私汤温泉氤氲暖池 (`prompts/scene_onsen_hotspring.txt`)
将 `Yang Yuyao` 模块化词块嵌入温泉温汤场景，重现“温泉水滑洗凝脂”的绝美画卷：

#### 合成完整 Prompt：
```text
A hyper-realistic atmospheric low-angle photograph of a voluptuous 24-year-old Tang Dynasty imperial consort named Yang Yuyao with intoxicating peach-blossom eyes, crimson and gold peony huadian painted on her forehead, luscious plump rose lips, magnificent high Tang coiffure with gold ornaments, possessing a sensual voluptuous hourglass figure with full natural curves, rounded hips, and luminous warm ivory skin with dewy micro-pores. She is completely nude, partially submerged in a natural steaming mineral hot-spring pool surrounded by smooth wet dark river stones. She leans back languidly against a smooth warm boulder, her arms resting along the stone rim, head tilted slightly back in sheer relaxation. Dense rising steam swirls around her shoulders. Droplets of condensation and hot mineral water glisten across her bare shoulders, collarbones, and generous bustline. The clear crystalline water reveals the sensual curves of her submerged torso and thighs. Warm ambient lanterns cast a golden amber glow across the steam and water ripples. Low perspective naturally framing the intimate contours of her lower anatomy through the clear water surface. 8k resolution, cinematic steam, photorealistic wet skin texture.
```

#### 快速执行命令 (PowerShell)：
```powershell
python scripts/qwen_pose_test.py `
  --mode t2i `
  --name char_cn02_yang_yuyao `
  --prompt "A hyper-realistic atmospheric low-angle photograph of a voluptuous 24-year-old Tang Dynasty imperial consort named Yang Yuyao with intoxicating peach-blossom eyes, crimson and gold peony huadian painted on her forehead, luscious plump rose lips, magnificent high Tang coiffure with gold ornaments, possessing a sensual voluptuous hourglass figure with full natural curves, rounded hips, and luminous warm ivory skin with dewy micro-pores. She is completely nude, partially submerged in a natural steaming mineral hot-spring pool surrounded by smooth wet dark river stones. She leans back languidly against a smooth warm boulder, her arms resting along the stone rim, head tilted slightly back in sheer relaxation. Dense rising steam swirls around her shoulders. Droplets of condensation and hot mineral water glisten across her bare shoulders, collarbones, and generous bustline. The clear crystalline water reveals the sensual curves of her submerged torso and thighs. Warm ambient lanterns cast a golden amber glow across the steam and water ripples. Low perspective naturally framing the intimate contours of her lower anatomy through the clear water surface. 8k resolution, cinematic steam, photorealistic wet skin texture." `
  --seed 80964 `
  --steps 45 `
  --cfg 2.5 `
  --sampler er_sde `
  --scheduler beta `
  --width 1152 `
  --height 1728 `
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" `
  --lora-strength 1.0 `
  --out outputs/characters/cn02_yang_yuyao_hotspring.png
```
