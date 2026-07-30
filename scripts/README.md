# Release Checks

## Manifest Validator

Use this check before publishing Social, Media, Creator, or Press kits.

### What it validates
- Referenced asset files exist in ../assets/
- Deprecated variants are not referenced in release manifests
- Manifests include at least one asset reference

### Run
From repository root:

```bash
python3 scripts/check_release_manifests.py
```

### Exit behavior
- Exit code 0: pass
- Exit code non-zero: fail, fix manifest references before release
