import os
import subprocess
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请指定汇编文件名（无需扩展名），例如：./sos-build sos")
        sys.exit(1)

    asm_base = sys.argv[1]
    temp_asm = f'{asm_base}.asm'
    temp_obj = f'{asm_base}.obj'
    output_exe = f'{asm_base}.exe'

    try:
        # 1. 编译为 64 位 OBJ
        compile_cmd = f'nasm -fwin64 {temp_asm} -o {temp_obj}'
        compile_result = subprocess.run(compile_cmd, shell=True, capture_output=True, text=True)
        if compile_result.returncode != 0:
            print("NASM 编译失败！错误信息：")
            print(compile_result.stderr)
            sys.exit(1)
        else:
            print("NASM 编译成功！")

        # 2. 使用 GCC 链接
        gcc_cmd = f'gcc -s {temp_obj} -o {output_exe} -lkernel32'
        gcc_result = subprocess.run(gcc_cmd, shell=True, capture_output=True, text=True)
        if gcc_result.returncode != 0:
            print("GCC 链接失败！错误信息：")
            print(gcc_result.stderr)
            sys.exit(1)
        else:
            print(f"GCC 链接成功！生成 {output_exe}")

    except Exception as e:
        print(f"运行时错误: {e}")
        if os.path.exists(temp_asm):
            os.remove(temp_asm)
        if os.path.exists(temp_obj):
            os.remove(temp_obj)
    finally:
        # 3. 清理临时文件
        if os.path.exists(temp_asm):
            os.remove(temp_asm)
        if os.path.exists(temp_obj):
            os.remove(temp_obj)