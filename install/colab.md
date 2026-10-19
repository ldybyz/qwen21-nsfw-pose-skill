# Google Colab（T4）运行指南

> ⚠️ 本文基于代码与文档分析整理，**未在 T4 上实测**。`int8_convrot` 在 Turing（sm_75）上的兼容性、
> fp16 是否黑图均需自行验证。

## 1. 资源对照

| 项目 | 项目需求 | Colab T4 | 判断 |
| --- | --- | --- | --- |
| 显存 | 推荐 24GB，最低 12GB + offload | 15GB | 勉强，靠 ComfyUI 自动卸载 |
| 内存 | 推荐/最低 32GB | **12.7GB** | **最大瓶颈**，文本编码器 8.7GB 易 OOM |
| 硬盘 | ~40GB | ~70GB 可用 | 够 |
| 系统 | Linux（`media_lock.py` 用 `fcntl`） | Linux | 可用 |

建议只用路线①②（T2I / Edit）。路线④需要浏览器 WebGL 3D 捕获，在 Colab 上成本高，不推荐。

## 2. 主要风险

1. **`int8_convrot` 对 sm_75 的支持不确定**：先把 ComfyUI 更新到最新版，并确认 `TextEncodeQwenImage21` 节点存在。
2. **fp16 黑图/NaN**：T4 无原生 bf16，ComfyUI 默认用 fp16。出黑图时试 `--fp32-vae`，或 `--bf16-unet`（慢）。
3. **速度**：粗估 1152×1728、50 步单张 15–30 分钟（估算）；1024×1024、30 步约 5–10 分钟。
4. **内存 OOM**：12.7GB 内存跑 8.7GB 文本编码器很吃紧；仍不稳定时改用 GGUF 量化版（需改 `workflows/*.json` 的加载节点）。
5. 请自行确认 Colab 使用条款对生成内容的限制。

## 3. 环境配置

```bash
export COMFY=/content/ComfyUI
export COMFYUI_URL=http://127.0.0.1:8188
export COMFYUI_INPUT=$COMFY/input
export COMFYUI_OUTPUT=$COMFY/output

git clone https://github.com/comfyanonymous/ComfyUI.git $COMFY
pip install -r $COMFY/requirements.txt
mkdir -p $COMFY/models/{diffusion_models,text_encoders,vae,loras}
```

## 4. 下载模型（Colab 在海外，直接用 huggingface.co，不用 hf-mirror）

```bash
B=https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main
wget -c -P $COMFY/models/diffusion_models $B/diffusion_models/qwen_image_2.1_int8_convrot.safetensors
wget -c -P $COMFY/models/text_encoders    $B/text_encoders/qwen3vl_8b_int8_convrot.safetensors
wget -c -P $COMFY/models/vae              $B/vae/qwen_image_2.1_vae_bf16.safetensors
```

LoRA 见 [setup.md](setup.md) §2（Civitai 需 API token，文件名须与表格一致）。

## 5. 启动 ComfyUI（后台）

```bash
cd $COMFY
nohup python main.py --listen 127.0.0.1 --port 8188 \
  --lowvram --disable-smart-memory --fp32-vae > comfy.log 2>&1 &
# 等待就绪
until curl -s $COMFYUI_URL/system_stats >/dev/null; do sleep 3; done; echo ready
```

## 6. 运行（降配示例）

相对 README 配方（1152×1728 / 50 步）已降配，交付时需如实标注：

```bash
python3 scripts/doctor.py

python3 scripts/qwen_pose_test.py --mode t2i --name test \
  --prompt "$(cat prompts/taws_v13_shower.txt)" --seed 80964 \
  --steps 30 --cfg 2.5 --sampler er_sde --scheduler beta \
  --width 1024 --height 1024 \
  --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" \
  --lora-strength 1.0 --out outputs/test.png
```

## 7. 使用 Google Drive 持久化

Colab 会话结束后 `/content` 全部清空。用 Drive 保存需要保留的东西：

| 内容 | 大小 | 建议 |
| --- | --- | --- |
| 输出图 | 小 | 放 Drive |
| LoRA | 每个 ≤608MB | 放 Drive（Civitai 需手动下载后上传） |
| 底模 | 约 16GB | 免费 Drive 只有 15GB，装不下；默认每次从 HF 重下 |

```python
from google.colab import drive
drive.mount("/content/drive")
```

- **不要直接从 Drive 加载模型**（FUSE 读取慢，8.7GB 的文本编码器尤其明显）。先 `shutil.copyfile` 到 `/content/ComfyUI/models/...` 再启动 ComfyUI。
- 不推荐用符号链接把 `models/` 指向 Drive，原因同上。
- 目录约定：`MyDrive/qwen21_pose/{loras,models,outputs}`。
- 有足够 Drive 空间时，可以缓存底模，下次会话直接复制，比下载更稳。

以上流程已写成 notebook：[`notebooks/colab_t4.ipynb`](../notebooks/colab_t4.ipynb)，在 Colab 里「文件 → 打开笔记本 → GitHub」选本仓库即可。

## 8. 建议试跑顺序

1. `doctor.py` 自检。
2. 512×512、10 步，确认无黑图、无 OOM。
3. 逐步加到 1024×1024、30 步。
4. 反复 OOM 或 `int8_convrot` 不兼容 → 换 GGUF Q4 + `ComfyUI-GGUF`。
5. 想稳定产出：Colab Pro 高内存运行时（~51GB）或租 24GB 显存 GPU。
