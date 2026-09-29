import json
from pathlib import Path

BASE_DIR = Path("/Users/shameelabid/MyWork/PsychLearno/psychLearno_data/staging/intro_psychology/raw")

def build_projects():
    proj_dir = BASE_DIR / "projects"
    proj_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. projects.json manifest
    manifest = {
        "projects": [
            {
                "id": "project1",
                "title": "Applied Psychological Research Proposal",
                "description": "Formulate a rigorous empirical study to investigate a contemporary behavioral phenomenon.",
                "difficulty": "Intermediate",
                "estimatedHours": "4-6"
            },
            {
                "id": "project2",
                "title": "Biopsychosocial Clinical Case Formulation",
                "description": "Synthesize biological, cognitive, and social factors to formulate a clinical case diagnosis and treatment plan.",
                "difficulty": "Advanced",
                "estimatedHours": "5-7"
            },
            {
                "id": "project3",
                "title": "Comprehensive Behavior Modification & Cognitive Habit Architecture",
                "description": "Design an evidence-based behavioral intervention utilizing operant conditioning and cognitive reframing.",
                "difficulty": "Intermediate",
                "estimatedHours": "3-5"
            }
        ]
    }
    with open(BASE_DIR / "projects.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    # 2. projects/project1.json
    project1_data = {
        "id": "project1",
        "title": "Applied Psychological Research Proposal",
        "description": "Formulate a rigorous empirical study to investigate a contemporary behavioral phenomenon.",
        "difficulty": "Intermediate",
        "estimatedHours": "4-6",
        "problemStatement": "Design a complete, publication-ready psychological research proposal investigating whether push notifications on smartphones impair Working Memory capacity during complex analytical problem-solving.\n\n### Context:\nPsychologists increasingly study the 'brain drain' phenomenon—how physical proximity to active digital devices consumes limited cognitive bandwidth even when not in active use.\n\n### Your Objective:\nConstruct a formal experimental proposal detailing operational definitions, experimental design, and ethical human-subject safeguards.",
        "requirements": [
            "Formulate an unambiguous, falsifiable hypothesis predicting the exact relationship between notification conditions and working memory performance.",
            "Explicitly define the Independent Variable (with at least 3 conditions: phone visible with alerts, phone silent on desk, phone in separate room) and the Dependent Variable (measured via a standardized working memory task like the OSPAN or n-back).",
            "Detail methodological controls: random assignment, double-blind testing procedures, and elimination of confounding variables (screen brightness, time of day).",
            "Draft a comprehensive Institutional Review Board (IRB) ethical compliance statement covering informed consent, right to withdraw, data anonymization, and post-experiment debriefing."
        ],
        "hints": [
            "Hint 1: Ensure your working memory task measures active manipulation of information, not mere rote recall.",
            "Hint 2: Anticipate potential demand characteristics and explain how double-blind testing neutralizes them."
        ]
    }
    with open(proj_dir / "project1.json", "w", encoding="utf-8") as f:
        json.dump(project1_data, f, indent=2)

    # 3. projects/project2.json
    project2_data = {
        "id": "project2",
        "title": "Biopsychosocial Clinical Case Formulation",
        "description": "Synthesize biological, cognitive, and social factors to formulate a clinical case diagnosis and treatment plan.",
        "difficulty": "Advanced",
        "estimatedHours": "5-7",
        "problemStatement": "You are a clinical psychologist evaluating a complex clinical case: 'Alex', a 24-year-old financial analyst presenting with debilitating lethargy, sleep-onset insomnia, severe anhedonia, and unexpected episodes of heart palpitations and trembling that occur during client presentations.\n\nAlex's family history reveals a maternal grandmother with Bipolar I Disorder. Alex reports constant automatic thoughts: 'If I make one mistake, my career is finished' and 'I am fundamentally incompetent'.\n\n### Your Objective:\nConduct a comprehensive diagnostic intake, apply the Biopsychosocial and Diathesis-Stress models, and outline an integrated evidence-based treatment protocol.",
        "requirements": [
            "Conduct a DSM-5-TR differential diagnosis: evaluate and distinguish between Major Depressive Disorder, Panic Disorder, Social Anxiety Disorder, and Bipolar II (screening for past hypomanic episodes).",
            "Analyze the etiology across the Biopsychosocial framework: Biological (genetic vulnerability, autonomic hyperreactivity), Psychological (Beck's cognitive triad, catastrophizing, negative reinforcement of avoidance), and Social (workplace pressures, isolation).",
            "Design an 8-week Cognitive-Behavioral Therapy (CBT) intervention incorporating cognitive restructuring of automatic distortions, behavioral activation, and systematic interoceptive exposure for panic sensations.",
            "Formulate collaborative biomedical recommendations regarding psychopharmacological consultation (e.g., SSRIs vs mood stabilizers) and evaluate potential side effects."
        ],
        "hints": [
            "Hint 1: Always check for a history of hypomanic episodes before recommending antidepressant monotherapy.",
            "Hint 2: Interoceptive exposure involves intentionally hyperventilating or spinning in a chair to desensitize the patient to bodily panic cues."
        ]
    }
    with open(proj_dir / "project2.json", "w", encoding="utf-8") as f:
        json.dump(project2_data, f, indent=2)

    # 4. projects/project3.json
    project3_data = {
        "id": "project3",
        "title": "Comprehensive Behavior Modification & Cognitive Habit Architecture",
        "description": "Design an evidence-based behavioral intervention utilizing operant conditioning and cognitive reframing.",
        "difficulty": "Intermediate",
        "estimatedHours": "3-5",
        "problemStatement": "Develop a comprehensive behavior modification and habit formation program to help university students eliminate chronic bedtime social media scrolling (revenge bedtime procrastination) and establish a restorative sleep routine.\n\n### Context:\nSleep deprivation impairs neuroplasticity, memory consolidation, and emotional regulation. Overcoming this habit requires altering the environmental stimulus cues, behavioral responses, and reinforcement consequences.\n\n### Your Objective:\nCreate an actionable multi-phase intervention synthesizing Operant Conditioning, Classical Stimulus Control, and Cognitive Reframing.",
        "requirements": [
            "Perform a functional behavioral analysis identifying the antecedent environmental cues (phone on nightstand, darkness), the target behaviors, and the immediate reinforcing payoffs (dopamine bursts, stress distraction).",
            "Apply Classical Conditioning stimulus control principles: re-associating the bed and bedroom exclusively with sleep and relaxation rather than work and screens.",
            "Incorporate Operant Conditioning techniques: formulate a shaping ladder with successive approximations, select effective positive reinforcers, and design an intermittent reinforcement fading schedule.",
            "Integrate Cognitive Restructuring: identify and reframe maladaptive thoughts (e.g., 'I worked hard all day, so I deserve to scroll for 2 hours') with adaptive rational thoughts that promote long-term well-being."
        ],
        "hints": [
            "Hint 1: Replacing an undesirable habit with a competing constructive habit (e.g., listening to an audiobook) is vastly more effective than attempting cold-turkey suppression.",
            "Hint 2: Establish clear pre-commitment strategies (such as placing the phone in a charging station outside the bedroom)."
        ]
    }
    with open(proj_dir / "project3.json", "w", encoding="utf-8") as f:
        json.dump(project3_data, f, indent=2)

    print("✅ Course Projects generated successfully!")

if __name__ == "__main__":
    build_projects()
