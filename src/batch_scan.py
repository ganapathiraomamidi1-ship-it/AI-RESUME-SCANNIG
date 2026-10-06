from pathlib import Path
import argparse
from resume_scanner import read_text, score_resume

p=argparse.ArgumentParser(description='Rank multiple resumes against one job description.')
p.add_argument('--resumes',required=True); p.add_argument('--job',required=True)
a=p.parse_args(); job=read_text(a.job); rows=[]
for f in sorted(Path(a.resumes).glob('*')):
    if f.suffix.lower() in {'.txt','.md'}:
        r=score_resume(read_text(str(f)),job); rows.append((f.name,r['overall_score'],r['skill_match_score']))
rows.sort(key=lambda x:x[1],reverse=True)
print('\nResume Ranking\n'+'='*60)
for i,(name,overall,skill) in enumerate(rows,1): print(f'{i:>2}. {name:<35} Overall: {overall:>6.1f}  Skills: {skill:>6.1f}%')