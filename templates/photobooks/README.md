# 写真套图通用模板库 (Photobook Templates Library)

本目录包含了用于 **通用写真集系统（Photobook Suite）** 的场景模板定义。
每个模板为一个标准 `.yaml` 文件，定义了一整套写真场景的**推荐默认参数**与**系列姿态镜头序列（分镜）**。

---

## 一、现有模板一览 (共 7 套写真全集)

| 模板标识 (ID) | 模板名称 | 分镜数量 | 核心风格 / 氛围 | 推荐适用角色 | 模板文件 |
| :---: | :--- | :---: | :--- | :--- | :--- |
| `chinese_canopy_bed` | **古典闺房·雕花拔步床写真** | 5 幕 | 东方温香软玉、红木雕花、烛影微汗、轻纱半掩 | 古典妖姬、神话志怪 (苏魅儿、杨玉瑶、赵凌燕、姬无双) | [`chinese_canopy_bed.yaml`](chinese_canopy_bed.yaml) |
| `onsen_hotspring` | **私汤温泉·水滑凝脂写真** | 5 幕 | 露天私汤、水雾蒸腾、火山青石、湿身水光 | 凝脂白玉肌、纯欲灵动 (苏魅儿、杨玉瑶、加藤樱、柳天仙) | [`onsen_hotspring.yaml`](onsen_hotspring.yaml) |
| `chinese_tearoom` | **新中式茶室·禅意茶烟写真** | 5 幕 | 竹帘漏光、紫砂茶烟、琴台蒲团、清冷脱俗与温润玉肌 | 古典才女、文人雅士、清冷神女 (李清照、林语婷、施浣纱、甄洛仙) | [`chinese_tearoom.yaml`](chinese_tearoom.yaml) |
| `qipao_lounge` | **民国风华·暗光旗袍微解写真** | 5 幕 | 王家卫暗调、高开叉丝绸旗袍半褪、天鹅绒贵妃榻、老上海名伶 | 极致风情尤物、成熟名媛 (白曼清、邱曼妮、苏魅儿、柳如诗) | [`qipao_lounge.yaml`](qipao_lounge.yaml) |
| `penthouse_stretch` | **顶层豪宅·晨曦落地窗写真** | 5 幕 | 都市天际线、清晨金色侧逆光薄雾、羊绒地毯、猫牛式拉伸 | 现代超模、高级骨相、健美线条 (杜雯、陈悦、裴智友、艾琳娜) | [`penthouse_stretch.yaml`](penthouse_stretch.yaml) |
| `sunset_beach_rock` | **潮汐礁石·落日暮光写真** | 5 幕 | 琥珀晚霞落日熔金、潮汐浪沫微漾、湿发与微观盐晶水光 | 野性健康、阳光沙漏、异域神颜 (阿莱西亚、热依仙、芙蕾雅) | [`sunset_beach_rock.yaml`](sunset_beach_rock.yaml) |
| `vintage_motel` | **复古港风·暗红霓虹胶片写真** | 5 幕 | 90s胶片电影质感、暗红皮革沙发、百叶窗光斑、微醺私密抓拍 | 港风神颜、复古浪漫 (邱曼妮、热依仙、克洛伊) | [`vintage_motel.yaml`](vintage_motel.yaml) |

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
提示词中的 `{SUBJECT}` 会被通用写真引擎自动替换为目标人物卡中的 **“## 5. 模块化主体描述词块”**。

---

## 三、命令行使用方式

```powershell
# 1. 查看所有已注册的写真模板
python scripts/run_photobook.py --list-templates

# 2. 为苏魅儿套用【新中式茶室】模板进行预览 (Dry-run)
python scripts/run_photobook.py --character su_meier --template chinese_tearoom --dry-run

# 3. 为苏魅儿套用【民国旗袍】模板并导出全部提示词 txt
python scripts/run_photobook.py --character su_meier --template qipao_lounge --export-dir photobooks/su_meier_qipao

# 4. 为现代角色杜雯套用【顶层豪宅】模板并生成图片
python scripts/run_photobook.py --character cn04_du_wen --template penthouse_stretch --run
```
