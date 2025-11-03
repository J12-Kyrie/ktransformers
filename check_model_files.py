#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
?? GGUF ?????????????
"""
import os
import sys

def check_gguf_model_files(model_dir):
    """
    ?? GGUF ???????????????????
    
    Args:
        model_dir: ??????
    """
    print(f"????: {model_dir}\n")
    
    # ???????
    required_files = {
        "????": [
            "configuration.json",  # ? config.json
            "config.json"
        ],
        "Tokenizer ??": [
            "tokenizer.json",
            "tokenizer_config.json",
            "special_tokens_map.json"
        ]
    }
    
    # ????????
    optional_files = [
        "vocab.json",
        "merges.txt",
        "tokenizer.model",
        "generation_config.json"
    ]
    
    # ????????
    if not os.path.exists(model_dir):
        print(f"? ??: ?????: {model_dir}")
        return False
    
    # ??????????
    files_in_dir = os.listdir(model_dir)
    print(f"?????? ({len(files_in_dir)} ?):")
    for f in sorted(files_in_dir):
        file_path = os.path.join(model_dir, f)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            size_str = f"{size / (1024*1024):.2f} MB" if size > 1024*1024 else f"{size / 1024:.2f} KB"
            print(f"  ?? {f} ({size_str})")
        else:
            print(f"  ?? {f}/")
    print()
    
    # ??????
    missing_files = []
    found_files = []
    
    # ??????
    config_found = False
    for config_file in required_files["????"]:
        if config_file in files_in_dir:
            config_found = True
            found_files.append(config_file)
            break
    if not config_found:
        missing_files.extend(required_files["????"])
    
    # ?? tokenizer ??
    for tokenizer_file in required_files["Tokenizer ??"]:
        if tokenizer_file in files_in_dir:
            found_files.append(tokenizer_file)
        else:
            missing_files.append(tokenizer_file)
    
    # ?? GGUF ??
    gguf_files = [f for f in files_in_dir if f.endswith('.gguf')]
    print(f"? ?? {len(gguf_files)} ? GGUF ??")
    if len(gguf_files) > 0:
        print("   GGUF ????:")
        for f in sorted(gguf_files):
            print(f"     - {f}")
    print()
    
    # ????
    print("=" * 60)
    print("????:")
    print("=" * 60)
    
    if len(found_files) > 0:
        print("\n? ??????:")
        for f in found_files:
            print(f"   ? {f}")
    
    if len(missing_files) > 0:
        print("\n? ?????:")
        for f in missing_files:
            print(f"   ? {f}")
        print("\n??  ??: ?? tokenizer ???????????????")
        print("\n??:")
        print("1. ? Hugging Face ?????? tokenizer ????")
        print("2. ???????????????????:")
        for f in missing_files:
            print(f"   - {f}")
    else:
        print("\n? ???????????")
    
    # ??????
    found_optional = [f for f in optional_files if f in files_in_dir]
    if found_optional:
        print("\n?? ?????????:")
        for f in found_optional:
            print(f"   ? {f}")
    
    return len(missing_files) == 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        model_dir = sys.argv[1]
    else:
        # ????????????????????????
        model_dir = input("?????????: ").strip()
    
    check_gguf_model_files(model_dir)
