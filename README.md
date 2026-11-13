# ConvNeXt-Lite

Official implementation of the paper **ConvNeXt-Lite: Efficient Vision Backbones for Edge
Deployment** (WACV 2025).

**Release status: public release (v1.0).** This repository contains the code,
configurations and scripts used to produce the results reported in the paper.

## Contents

- `src/` - model definitions and the latency-aware search implementation
- `configs/` - search and training configurations for the WACV experiments
- `experiments/` - scripts that reproduce the latency and accuracy tables
- `data/` - notes on preparing the image classification datasets

## Quick start

```bash
python -m src.train --config configs/base.yaml
```

## Citation

Please cite the WACV 2025 paper if you use this code.
