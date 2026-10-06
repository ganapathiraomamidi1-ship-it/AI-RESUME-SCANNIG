from __future__ import annotations
import argparse, json, re
from pathlib import Path

SKILLS={'python','java','c','c++','sql','mysql','postgresql','pandas','numpy','scikit-learn','tensorflow','pytorch','machine learning','deep learning','data science','data analysis','power bi','tableau','excel','statistics','nlp','computer vision','git','github','docker','aws','azure','gcp','spring boot','react','javascript','typescript','html','css','rest api','mongodb','communication','leadership'}

def read_text(path):
    p=Path(path)
    if not p.exists(): raise FileNotFoundError(f'File not found: {path}')
    return p.read_text(encoding='utf-8',errors='ignore')

def normalize(text): return re.sub(r'\s+',' ',text.lower()).strip()

def extract_skills(text):
    t=normalize(text)
    return {s for s in SKILLS if re.search(r'(?<!\w)'+re.escape(s)+r'(?!\w)',t)}

def contact_signals(text):
    return {'email_found':bool(re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+',text)),'phone_found':bool(re.search(r'(?:\+?\d[\d ()-]{8,}\d)',text)),'linkedin_found':'linkedin.com' in text.lower(),'github_found':'github.com' in text.lower()}

def score_resume(resume,job):
    rs,js=extract_skills(resume),extract_skills(job)
    matched=sorted(rs&js); missing=sorted(js-rs)
    skill_score=(len(matched)/len(js)*100) if js else 0.0
    contact=contact_signals(resume); contact_score=sum(contact.values())/len(contact)*100
    overall=0.85*skill_score+0.15*contact_score
    return {'overall_score':round(overall,2),'skill_match_score':round(skill_score,2),'matched_skills':matched,'missing_skills':missing,'resume_skill_count':len(rs),'job_skill_count':len(js),'contact_signals':contact,'recommendation':'Strong match' if overall>=75 else 'Moderate match' if overall>=50 else 'Needs improvement'}

def main():
    p=argparse.ArgumentParser(description='Analyze a resume against a job description.')
    p.add_argument('--resume',required=True); p.add_argument('--job',required=True); p.add_argument('--output',default='outputs/resume_analysis.json')
    a=p.parse_args(); report=score_resume(read_text(a.resume),read_text(a.job))
    out=Path(a.output); out.parent.mkdir(exist_ok=True); out.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(f"\nAI Resume Scanner\n{'='*30}\nOverall ATS-style score: {report['overall_score']:.1f}/100\nSkill match: {report['skill_match_score']:.1f}%\nRecommendation: {report['recommendation']}\nMatched: {', '.join(report['matched_skills']) or 'None'}\nMissing: {', '.join(report['missing_skills']) or 'None'}\nReport: {out}")

if __name__=='__main__': main()