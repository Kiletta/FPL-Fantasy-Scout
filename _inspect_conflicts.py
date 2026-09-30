from pathlib import Path

files = [
    Path(r'c:\Users\chris\FPL_Fantasy_Scouting\Fantasy_Scout.ipynb'),
    Path(r'c:\Users\chris\FPL_Fantasy_Scouting\Deeper_Player_Scouting.ipynb'),
]

for path in files:
    print(f'FILE: {path.name}')
    lines = path.read_text(encoding='utf-8').splitlines()
    found = False
    for i, line in enumerate(lines, 1):
        if '<<<<<<<' in line or '=======' in line or '>>>>>>>' in line:
            if not found:
                found = True
            start = max(1, i - 8)
            end = min(len(lines), i + 12)
            print(f'--- around line {i} ---')
            for j in range(start, end + 1):
                print(f'{j}: {lines[j-1]}')
            print()
    if not found:
        print('No conflict markers found.')
    print('====')
