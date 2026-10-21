# 写真套图通用模板库 (Photobook Templates Library)

本目录包含了用于 **通用写真集系统（Photobook Suite）** 的场景模板定义。
每个模板为一个标准 `.yaml` 文件，定义了一整套写真场景的**推荐默认参数**与**系列姿态镜头序列（分镜）**。

---

## 一、现有模板一览

| 模板标识 (ID) | 模板名称 | 分镜数量 | 适用风格 / 推荐角色 | 模板文件 |
| :---: | :--- | :---: | :--- | :--- |
| `chinese_canopy_bed` | **古典闺房·雕花拔步床写真** | 5 幕 | 古典神话妖姬、汉唐名媛、仙侠修仙 (如苏魅儿、杨玉瑶、赵凌燕) | [`chinese_canopy_bed.yaml`](chinese_canopy_bed.yaml) |
| `onsen_hotspring` | **私汤温泉·水滑凝脂写真** | 5 幕 | 水雾湿身、凝脂白玉肌、纯欲与慵懒 (如苏魅儿、杨玉瑶、加藤樱、柳天仙) | [`onsen_hotspring.yaml`](onsen_hotspring.yaml) |

---

## 二、模板设计规范与语法

### 1. 字段说明
```yaml
id: my_custom_scene                 # 模板唯一标识 (ID)
name_zh: "我的自定义场景写真套图"      # 中文名称
description: "场景详细描述与适用建议"   # 简介说明
scene_reference: "prompts/scene_*.txt" # 可选：参考的单张场景文件

default_params:                      # 默认推荐参数 (当人物卡未指定时生效)
  lora: "thesealpacas-nsfw-v2.safetensors"
  lora_strength: 0.85
  cfg: 4.0
  steps: 45
  sampler: "er_sde"
  scheduler: "beta"
  width: 1152
  height: 1728
  negative: "blurry, deformed, bad anatomy, bad hands, plastic skin, cartoon"

shots:                               # 写真分镜列表 (可定义任意幕数：3幕、5幕、8幕等)
  - id: "01_shot_name"               # 分镜标识
    name_zh: "分镜中文名"
    shot_type: "镜头与景别类型"
    steps: 45                        # 该分镜专属步数 (可选)
    prompt: >-                       # 提示词，必须包含 {SUBJECT} 占位插槽
      A cinematic medium shot of {SUBJECT}. She is completely nude, posing in ...
```

### 2. 核心插槽 `{SUBJECT}`
提示词中的 `{SUBJECT}` 会被自动替换为目标人物卡中的 **“## 5. 模块化主体描述词块”**。

---

## 三、命令行使用方式

```powershell
# 1. 查看所有已注册的写真模板
python scripts/run_photobook.py --list-templates

# 2. 指定任意角色 + 任意模板进行预览 (Dry-run)
python scripts/run_photobook.py --character su_meier --template onsen_hotspring --dry-run

# 3. 导出指定角色在指定模板下的全部提示词 txt 和 params.json
python scripts/run_photobook.py --character su_meier --template onsen_hotspring --export-dir photobooks/su_meier_onsen

# 4. 一键批量生成图片
python scripts/run_photobook.py --character su_meier --template chinese_canopy_bed --run
```
