# Colab 使用说明：出图与改图

适用于已按 [colab.md](colab.md) 跑通环境的用户，使用 `notebooks/colab_t4_quick.ipynb` 或直接调用
`scripts/colab_quickstart.py`。

> 本文描述的是命令行为与项目既有经验（`SKILL.md`）。改图模式（`--mode edit`）在 Colab T4 上**未经实测**，
> 请先用一张小图试跑。

## 1. 整体流程

```
① 挂载 Drive + 克隆仓库  →  ② 运行 colab_quickstart.py  →  ③ 看图  →（④ 改图，可选）
```

脚本每一步都可重复运行：已有文件跳过，ComfyUI 已在后台就复用。所以**第二次起只会花出图的时间**。

## 2. Drive 目录约定

`我的云端硬盘/qwen21_pose/`：

| 目录 | 用途 |
| --- | --- |
| `models/` | 底模缓存（约 16GB，默认开启；`--no-cache-base` 关闭） |
| `loras/` | LoRA 文件，文件名必须与 `--lora-name` 一致 |
| `outputs/` | 生成结果（`.png` + 同名 `.json`，含提示词/种子/步数） |
| `inputs/` | 改图用的原图 |
| `prompts/` | 你自己的提示词文件 |

## 3. 文字出图（路线①）

```bash
python scripts/colab_quickstart.py \
  --prompt-file /content/drive/MyDrive/qwen21_pose/prompts/my.txt \
  --width 768 --height 1152 --steps 20 --seed 123 --skip-doctor
```

### 参数速查

| 参数 | 默认 | 说明 |
| --- | --- | --- |
| `--prompt` / `--prompt-file` | 作者淋浴样例 | 提示词（行内 / 文件，文件可放 Drive） |
| `--negative` | 空 | 负向提示词 |
| `--width` `--height` | 1024×1024 | 竖版推荐 2:3；T4 上 768×1152 比 1024×1024 更省 |
| `--steps` | 20 | 越多越慢；项目配方是 50 |
| `--cfg` | 2.5 | 2.5–4，调高细节更多；CFG 1 会让 LoRA 失效 |
| `--seed` | 80964 | 换种子得到不同构图；同种子同参数基本复现 |
| `--lora-name` | femaledVaginus v1.3b | LoRA 文件名 |
| `--no-lora` | 关 | 不用任何 LoRA（非人物题材必开，用 `--preset` 时自动开启） |
| `--preset` | 无 | `landscape` / `animal` / `sticker`，见 §4.5 |
| `--lora-strength` | 1.0 | 建议 0.7–1.0 |
| `--lora-url` `--civitai-token` | 空 | LoRA 不在 Drive 时下载一次并缓存到 Drive |
| `--skip-doctor` | 关 | 跳过自检，省时间 |
| `--setup-only` | 关 | 只准备环境，不出图 |

### 提示词怎么写

提示词是最大的杠杆，短关键词会很平淡。项目的作者结构包含 7 个要素，建议都写，总长约 300–1500 字符：

1. **镜头**：摄影类型、机位、角度（低机位 / 俯拍）
2. **人物**：年龄、体型、发色发型状态
3. **姿势**：一次只选一个，逐肢体写清楚（哪条腿弯、手在哪、头和视线）
4. **场景与光线**
5. **皮肤质感**：光泽、毛孔、自然纹理
6. **露出程度的描述**：LoRA 用具体描述训练，笼统词几乎无效
7. **收尾**：分辨率、电影感光线、抓拍氛围、真实解剖

**最稳的做法是改写现成提示词**：把 `prompts/*.txt`（`taws_v13_shower.txt`、`taws_v13_massage.txt`、
`thesealpacas_v2_selfie.txt`）里的人物/场景/姿势换成自己的，保留整体结构。每个样例都有同名
`.params.json`，记录它实际用的参数，**一套提示词应配它自己的参数**（例如 selfie 用 CFG 4.0 + 另一个 LoRA）。

### 姿势与"大胆程度"

大胆程度由三件事叠加：**姿势开合度 × 机位 × 着装/湿身状态**。`SKILL.md` §4 把它分成 L0–L3 四档，
并给出"想要的效果 → 姿势"对照表。规则要点：

- 先决定露出程度，再选姿势；LoRA 搭配 L0（全着装）姿势是出图平淡的常见原因。
- 低机位、俯拍都会放大姿势效果。
- 一个提示词只写一个姿势，多个姿势描述会互相混合。

## 4. 改已有的图（路线②）

保留人物的脸、发型和服装，改变姿势或场景。

### 步骤

1. 把原图上传到 Drive 的 `qwen21_pose/inputs/`。
2. 运行：

```bash
python scripts/colab_quickstart.py --mode edit \
  --input /content/drive/MyDrive/qwen21_pose/inputs/my_image.png \
  --prompt "change her pose to kneeling on one knee, hands on hips, keep face hair and outfit" \
  --skip-doctor
```

结果保存为 `outputs/colab_edit_<时间>.png`，同样会复制到 Drive。

### 改图模式的默认值

| 项 | 改图默认 | 原因 |
| --- | --- | --- |
| `--cfg` | 3.0 | 项目经验：编辑模式 CFG 3 更稳 |
| `--steps` | 20 | 项目示例值 |
| LoRA | 不加 | SFW 的指令不会触发 NSFW LoRA；需要时再用 `--lora-name` 指定 edit 专用 LoRA |
| 尺寸 | 跟随原图 | `--width/--height` 对改图无效 |

### 写改图指令的建议

- 用**英文祈使句**，说清要改什么、要保留什么：`change ..., keep face hair and outfit`。
- 一次只改一件事（姿势或场景），改完再改下一件。
- 想要 edit 专用 LoRA（`qwen21-nsfw-image-edit.safetensors`），下载方式见 [setup.md](setup.md) §2，
  放进 Drive 的 `loras/` 后加 `--lora-name qwen21-nsfw-image-edit.safetensors`。

### 不要这样做

- **不要用照片或插画当"姿势参考"**。模型会把参考人物拼进画面，或把参考人物重画。
  需要姿势参考时用无身份特征的 3D 人偶渲染图（路线③④，在 Colab 上不推荐）。
- 路线④（VNCCS 3D 姿势库）依赖浏览器的 3D 实时捕获，Colab 上成本高，本说明不覆盖。

## 4.5 非人物题材：风景 / 动物 / 表情包

底模 Qwen-Image 2.1 是通用文生图模型，不只会画人；项目里偏向人物的是 NSFW LoRA、作者提示词样例和姿势库。
画风景、动物等题材时不要用这些 LoRA，否则可能引入不相关的人体特征或质感。

> 非人物题材在 T4 上**未经实测**；表情包里的文字渲染效果也未验证。

### 用预设

```bash
python scripts/colab_quickstart.py --preset landscape \
  --prompt "A misty mountain lake at sunrise, pine forest on the shore, golden light, wide angle photograph" \
  --seed 1 --skip-doctor
```

| 预设 | 默认画幅 | 适用 |
| --- | --- | --- |
| `landscape` | 1024×576（16:9） | 风景 |
| `animal` | 1024×768（4:3） | 动物 / 宠物 / 野生动物 |
| `sticker` | 1024×1024 | 表情包 / 贴纸 / 带文字的图 |

使用预设时：

- 自动**关闭 NSFW LoRA**（不会去 Drive 取 LoRA，也不用 LoRA 文件）。
- **必须自己写提示词**（`--prompt` 或 `--prompt-file`）。默认的样例提示词是作者的人像，预设和 `--no-lora` 下不会再回退到它，缺提示词会直接报错。
- 显式传 `--width/--height` 会覆盖预设的画幅；预设只对文字出图有效，不能和 `--mode edit` 一起用。
- 不想用预设时，等价写法是 `--no-lora --width ... --height ... --prompt ...`。

### 提示词怎么写

7 要素和 300–1500 字符的要求是针对 NSFW 人物的，**非人物题材不适用**。写清这几项即可：

- **主体**：是什么、什么状态
- **环境**：场景、时间、天气
- **光线**：如晨光、逆光、柔和阴影
- **镜头与风格**：广角 / 微距、摄影 / 插画 / 矢量
- 避免英文双引号 `"`（会破坏 shell 命令），需要引号用单引号

### 表情包的局限

- **不支持透明背景**，输出是普通不透明图片。
- 文字尽量短，并在提示词里明确写出要显示的内容（如 `a sign that says 'OK'`）。
- 想做同一角色的一套表情，可先出一张角色图，再用改图模式逐个改表情，保真度未验证。

### 改非人物的图

直接用 §4 的改图模式即可，默认就不带 LoRA。例如
`--prompt "change the background to a snowy forest, keep the animal and its pose unchanged"`。

### 示例 notebook

[`notebooks/colab_t4_examples.ipynb`](../notebooks/colab_t4_examples.ipynb) 提供了风景、动物、表情包、改图、批量换种子的示例，每个 cell 独立可运行。

### 视频

本项目**只做静态图**，没有视频模型、工作流或脚本。视频生成需要另选模型（如 Wan、LTX-Video 等）和独立的
ComfyUI 工作流，且通常比图像更吃显存和内存；T4 加 12.7GB 内存很可能吃紧（未实测）。建议另开独立 notebook 试验，不要混进本项目。

## 5. 批量与复现

- 脚本一次只出 1 张。多张请重复运行并**换种子**（`--seed 1`、`--seed 2` …）。
- 每张图旁边的 `.json` 记录了提示词、种子、步数、LoRA，复现时照抄即可。
- 在 notebook 里循环多张的示例（`colab_t4_examples.ipynb` 里有完整版）：

```python
import subprocess
for seed in (1, 2, 3):
    subprocess.run(["python", f"{POSELAB}/scripts/colab_quickstart.py",
                    "--prompt-file", "/content/drive/MyDrive/qwen21_pose/prompts/my.txt",
                    "--seed", str(seed), "--skip-doctor"])
```

## 6. 速度与资源

- 实测参考：1024×1024、20 步、CFG 2.5，约 303 秒（含模型加载）。
- 启动参数里的 `--disable-smart-memory` 会让每次出图都重新加载模型；内存允许时可用
  `--comfy-args "--lowvram --fp32-vae"` 去掉它，第二张起更快，但有 OOM 风险（需重启 ComfyUI 才生效：
  `pkill -f "main.py --listen"` 后重跑）。
- 不用时请「运行时 → 断开连接并删除运行时」释放 GPU；Drive 里的底模、LoRA、输出都不会丢。

## 7. 相对项目配方的降配说明

`SKILL.md` 规定的配方是 50 步、1152×1728、CFG 2.5、`er_sde` + `beta`、LoRA@1.0。Colab T4 默认
（20 步、1024×1024 或更小）属于**降配**，细节与质感可能弱于作者样图。对外展示时请标注参数，
不要把降配结果当作"作者配方的结果"。
