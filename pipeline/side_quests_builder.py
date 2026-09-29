import json
from pathlib import Path

BASE_DIR = Path("/Users/shameelabid/MyWork/PsychLearno/psychLearno_data/staging/intro_psychology/raw")

def build_side_quests():
    sq_dir = BASE_DIR / "side_quests"
    sq_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. side_quests.json manifest
    manifest = [
        {
            "id": "sq_intro_psychology_1",
            "title": "Midterm Challenge: Mind, Body & Scientific Rigor",
            "triggerChapterIndex": 1,
            "metadata": {
                "type": "scenario_analysis"
            }
        },
        {
            "id": "sq_intro_psychology_2",
            "title": "Case Investigation: Perception & Learned Behaviors",
            "triggerChapterIndex": 3,
            "metadata": {
                "type": "case_study"
            }
        },
        {
            "id": "sq_intro_psychology_3",
            "title": "Speed Run: Comprehensive Cognitive & Social Psych",
            "triggerChapterIndex": 6,
            "metadata": {
                "type": "speed"
            }
        }
    ]
    with open(BASE_DIR / "side_quests.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    # 2. sq_intro_psychology_1.json (Scenario Analysis, Cumulative Ch 1 & 2)
    sq1_data = {
        "id": "sq_intro_psychology_1",
        "title": "Midterm Challenge: Mind, Body & Scientific Rigor",
        "triggerChapterIndex": 1,
        "metadata": {
            "type": "scenario_analysis"
        },
        "questions": [
            {
                "id": "sq1_q1",
                "type": "multiple_choice",
                "question": "A clinical neuroscientist hypothesizes that a new memory-enhancing drug increases acetylcholine release in the hippocampus. In a double-blind trial, what serves as the Dependent Variable?",
                "options": [
                    {"id": "opt1", "text": "The dosage of the drug versus placebo administered", "isCorrect": False},
                    {"id": "opt2", "text": "The participants' scores on subsequent episodic memory retention tests", "isCorrect": True},
                    {"id": "opt3", "text": "The age and gender of the laboratory staff", "isCorrect": False},
                    {"id": "opt4", "text": "The brand of scanner used", "isCorrect": False}
                ],
                "explanation": "The dependent variable is the measured outcome behavior (memory test scores) hypothesized to be affected by the independent drug manipulation.",
                "xpReward": 20,
                "difficulty": 2
            },
            {
                "id": "sq1_q2",
                "type": "multiple_choice",
                "question": "Scenario: Patient Marcus suffers localized brain damage following a motorcycle accident. He can easily understand everything his doctor says, but his speech is slow, halting, and missing grammar. What specific structure was damaged?",
                "options": [
                    {"id": "opt1", "text": "Broca's Area in the left frontal lobe", "isCorrect": True},
                    {"id": "opt2", "text": "Wernicke's Area in the left temporal lobe", "isCorrect": False},
                    {"id": "opt3", "text": "The Occipital visual association cortex", "isCorrect": False},
                    {"id": "opt4", "text": "The Medulla oblongata", "isCorrect": False}
                ],
                "explanation": "Non-fluent, telegraphic speech with intact comprehension is classic Broca's motor aphasia.",
                "xpReward": 20,
                "difficulty": 2
            },
            {
                "id": "sq1_q3",
                "type": "multiple_choice",
                "question": "Scenario: A pharmaceutical company advertises a herbal beverage claiming it 'permanently detoxifies your synaptic vesicles without diet changes'. How would an empirical psychologist critique this claim?",
                "options": [
                    {"id": "opt1", "text": "Accept it immediately if a famous celebrity endorses it", "isCorrect": False},
                    {"id": "opt2", "text": "Demand peer-reviewed randomized controlled trials and check for falsifiability", "isCorrect": True},
                    {"id": "opt3", "text": "Assume correlation equates to causation", "isCorrect": False},
                    {"id": "opt4", "text": "Rely strictly on introspection to test it", "isCorrect": False}
                ],
                "explanation": "Scientific claims require empirical peer review, falsifiable testing, and randomized control groups.",
                "xpReward": 20,
                "difficulty": 2
            },
            {
                "id": "sq1_q4",
                "type": "multiple_choice",
                "question": "Scenario: While exploring a dark alley, a sudden loud clang causes an immediate surge in adrenaline, dilated pupils, and tachycardia. Which branch of the nervous system orchestrated this response?",
                "options": [
                    {"id": "opt1", "text": "Parasympathetic Nervous System", "isCorrect": False},
                    {"id": "opt2", "text": "Sympathetic Nervous System", "isCorrect": True},
                    {"id": "opt3", "text": "Somatic Sensory division", "isCorrect": False},
                    {"id": "opt4", "text": "Central Spinal Cord reflex", "isCorrect": False}
                ],
                "explanation": "The sympathetic branch activates the physiological fight-or-flight mobilization.",
                "xpReward": 20,
                "difficulty": 1
            },
            {
                "id": "sq1_q5",
                "type": "multiple_choice",
                "question": "Scenario: An experimental neurotoxin selectively inhibits voltage-gated sodium ($Na^+$) channels from opening on neuronal axons. What will happen to exposed neurons?",
                "options": [
                    {"id": "opt1", "text": "They will generate constant continuous action potentials", "isCorrect": False},
                    {"id": "opt2", "text": "They will be unable to depolarize and cannot fire action potentials", "isCorrect": True},
                    {"id": "opt3", "text": "Their myelin sheath will immediately double in thickness", "isCorrect": False},
                    {"id": "opt4", "text": "They will convert into glial cells", "isCorrect": False}
                ],
                "explanation": "Without sodium influx, the neuronal membrane cannot depolarize past threshold to initiate an action potential.",
                "xpReward": 25,
                "difficulty": 3
            },
            {
                "id": "sq1_q6",
                "type": "multiple_choice",
                "question": "Scenario: A split-brain patient is presented with the word 'RING' to their left visual field and 'KEY' to their right visual field. When asked what they saw, what will the patient verbalize?",
                "options": [
                    {"id": "opt1", "text": "'RING'", "isCorrect": False},
                    {"id": "opt2", "text": "'KEY'", "isCorrect": True},
                    {"id": "opt3", "text": "'RING-KEY'", "isCorrect": False},
                    {"id": "opt4", "text": "They will be unable to speak at all", "isCorrect": False}
                ],
                "explanation": "The right visual field sends information to the left hemisphere, where vocal speech centers reside, so the patient verbalizes 'KEY'.",
                "xpReward": 25,
                "difficulty": 3
            }
        ]
    }
    with open(sq_dir / "sq_intro_psychology_1.json", "w", encoding="utf-8") as f:
        json.dump(sq1_data, f, indent=2)

    # 3. sq_intro_psychology_2.json (Case Study, Cumulative Ch 1-4)
    sq2_data = {
        "id": "sq_intro_psychology_2",
        "title": "Case Investigation: Perception & Learned Behaviors",
        "triggerChapterIndex": 3,
        "metadata": {
            "type": "case_study"
        },
        "questions": [
            {
                "id": "sq2_q1",
                "type": "multiple_choice",
                "question": "Case Study: 6-year-old Leo developed a paralyzing fear of thunder after a violent storm. Now, whenever he sees a bright camera flash, his heart races with fear. What classical conditioning mechanism explains his reaction to the camera flash?",
                "options": [
                    {"id": "opt1", "text": "Stimulus Generalization", "isCorrect": True},
                    {"id": "opt2", "text": "Stimulus Discrimination", "isCorrect": False},
                    {"id": "opt3", "text": "Spontaneous Recovery", "isCorrect": False},
                    {"id": "opt4", "text": "Sensory Adaptation", "isCorrect": False}
                ],
                "explanation": "Generalization occurs when stimuli resembling the conditioned stimulus (lightning/flash) evoke the conditioned emotional response.",
                "xpReward": 20,
                "difficulty": 2
            },
            {
                "id": "sq2_q2",
                "type": "multiple_choice",
                "question": "Case Study: In the storm scenario above, what was the original Unconditioned Stimulus (US) that triggered the innate startle response?",
                "options": [
                    {"id": "opt1", "text": "The loud booming thunderclap", "isCorrect": True},
                    {"id": "opt2", "text": "The camera flash", "isCorrect": False},
                    {"id": "opt3", "text": "The heart racing response", "isCorrect": False},
                    {"id": "opt4", "text": "The room lighting", "isCorrect": False}
                ],
                "explanation": "The loud noise of the thunderclap naturally and automatically triggered an unconditioned startle response.",
                "xpReward": 20,
                "difficulty": 1
            },
            {
                "id": "sq2_q3",
                "type": "multiple_choice",
                "question": "Case Study: A graphic design firm creates a brand logo featuring an incomplete silhouette of a lion. Customers effortlessly perceive a complete, majestic lion. Which Gestalt grouping principle explains this?",
                "options": [
                    {"id": "opt1", "text": "Closure", "isCorrect": True},
                    {"id": "opt2", "text": "Proximity", "isCorrect": False},
                    {"id": "opt3", "text": "Trichromatic vision", "isCorrect": False},
                    {"id": "opt4", "text": "Linear perspective", "isCorrect": False}
                ],
                "explanation": "Closure causes the human perceptual system to automatically fill in visual gaps to perceive a unified form.",
                "xpReward": 20,
                "difficulty": 1
            },
            {
                "id": "sq2_q4",
                "type": "multiple_choice",
                "question": "Case Study: A sleep lab patient exhibits irregular breathing, high brain metabolic activity on EEG resembling wakefulness, but their limbs are completely paralyzed. What sleep stage are they in?",
                "options": [
                    {"id": "opt1", "text": "REM Sleep", "isCorrect": True},
                    {"id": "opt2", "text": "NREM-3 Slow-wave sleep", "isCorrect": False},
                    {"id": "opt3", "text": "NREM-1 Transitional stage", "isCorrect": False},
                    {"id": "opt4", "text": "Hypnagogic sleep paralysis only", "isCorrect": False}
                ],
                "explanation": "REM sleep features paradoxical physiological activity: alert brainwaves with profound skeletal muscle atonia.",
                "xpReward": 20,
                "difficulty": 2
            },
            {
                "id": "sq2_q5",
                "type": "multiple_choice",
                "question": "Case Study: A mobile game gives players a mystery prize box after an unpredictable number of completed levels (sometimes after 3 levels, sometimes after 9, averaging 5). What reinforcement schedule is this?",
                "options": [
                    {"id": "opt1", "text": "Variable-Ratio (VR)", "isCorrect": True},
                    {"id": "opt2", "text": "Fixed-Interval (FI)", "isCorrect": False},
                    {"id": "opt3", "text": "Fixed-Ratio (FR)", "isCorrect": False},
                    {"id": "opt4", "text": "Variable-Interval (VI)", "isCorrect": False}
                ],
                "explanation": "Reinforcing behavior after an unpredictable number of responses is a Variable-Ratio schedule.",
                "xpReward": 20,
                "difficulty": 2
            },
            {
                "id": "sq2_q6",
                "type": "multiple_choice",
                "question": "Case Study: A patient is prescribed a dopamine antagonist to treat hallucinations. As a side effect, the patient begins experiencing muscle tremors and stiffness. Which neurological structure is being impacted?",
                "options": [
                    {"id": "opt1", "text": "The Basal Ganglia and Substantia Nigra motor pathways", "isCorrect": True},
                    {"id": "opt2", "text": "The Primary Visual Cortex", "isCorrect": False},
                    {"id": "opt3", "text": "The Cochlea", "isCorrect": False},
                    {"id": "opt4", "text": "The Corpus Callosum", "isCorrect": False}
                ],
                "explanation": "Blocking dopamine in motor basal ganglia circuits mimics Parkinsonian extrapyramidal symptoms.",
                "xpReward": 25,
                "difficulty": 3
            },
            {
                "id": "sq2_q7",
                "type": "multiple_choice",
                "question": "Case Study: In an observational study, preschool children who watched an adult solve a puzzle by singing a specific rhythm imitated the song while solving the puzzle, while children who saw silent solving did not. This demonstrates:",
                "options": [
                    {"id": "opt1", "text": "Albert Bandura's Social Observational Modeling", "isCorrect": True},
                    {"id": "opt2", "text": "B.F. Skinner's Aversive Extinction", "isCorrect": False},
                    {"id": "opt3", "text": "Signal Detection Hit Bias", "isCorrect": False},
                    {"id": "opt4", "text": "Vestibular Accommodation", "isCorrect": False}
                ],
                "explanation": "Bandura demonstrated that children reproduce novel behavioral routines through vicarious observational modeling.",
                "xpReward": 20,
                "difficulty": 2
            }
        ]
    }
    with open(sq_dir / "sq_intro_psychology_2.json", "w", encoding="utf-8") as f:
        json.dump(sq2_data, f, indent=2)

    # 4. sq_intro_psychology_3.json (Speed Run, Cumulative Ch 1-7)
    sq3_data = {
        "id": "sq_intro_psychology_3",
        "title": "Speed Run: Comprehensive Cognitive & Social Psych",
        "triggerChapterIndex": 6,
        "metadata": {
            "type": "speed"
        },
        "questions": [
            {
                "id": "sq3_q1",
                "type": "true_false",
                "question": "In a normal distribution of standardized WAIS intelligence scores (M=100, SD=15), approximately 68% of the population scores between 85 and 115.",
                "options": [
                    {"id": "opt1", "text": "True", "isCorrect": True},
                    {"id": "opt2", "text": "False", "isCorrect": False}
                ],
                "explanation": "True. In a normal bell curve, 68.2% of all values fall within ±1 standard deviation of the mean.",
                "xpReward": 15,
                "difficulty": 1
            },
            {
                "id": "sq3_q2",
                "type": "multiple_choice",
                "question": "Which cognitive shortcut leads people to overestimate the danger of a plane crash because dramatic crashes are easily retrieved from memory?",
                "options": [
                    {"id": "opt1", "text": "Availability Heuristic", "isCorrect": True},
                    {"id": "opt2", "text": "Representativeness Heuristic", "isCorrect": False},
                    {"id": "opt3", "text": "Functional Fixedness", "isCorrect": False},
                    {"id": "opt4", "text": "Confirmation Bias", "isCorrect": False}
                ],
                "explanation": "The availability heuristic estimates frequency based on ease of mental recall.",
                "xpReward": 15,
                "difficulty": 1
            },
            {
                "id": "sq3_q3",
                "type": "multiple_choice",
                "question": "In Stanley Milgram's classic obedience studies, what proportion of participants delivered the maximum 450-volt shock?",
                "options": [
                    {"id": "opt1", "text": "Approximately 65%", "isCorrect": True},
                    {"id": "opt2", "text": "Under 2%", "isCorrect": False},
                    {"id": "opt3", "text": "Exactly 100%", "isCorrect": False},
                    {"id": "opt4", "text": "About 33%", "isCorrect": False}
                ],
                "explanation": "Two-thirds (65%) of ordinary participants administered the maximum electrical shock under authority commands.",
                "xpReward": 15,
                "difficulty": 1
            },
            {
                "id": "sq3_q4",
                "type": "multiple_choice",
                "question": "According to Jean Piaget, during which stage does a child first master the principle of Conservation?",
                "options": [
                    {"id": "opt1", "text": "Concrete Operational Stage (ages 7-11)", "isCorrect": True},
                    {"id": "opt2", "text": "Sensorimotor Stage (ages 0-2)", "isCorrect": False},
                    {"id": "opt3", "text": "Preoperational Stage (ages 2-7)", "isCorrect": False},
                    {"id": "opt4", "text": "Postconventional Stage", "isCorrect": False}
                ],
                "explanation": "Concrete operational children grasp conservation of volume, mass, and number.",
                "xpReward": 15,
                "difficulty": 1
            },
            {
                "id": "sq3_q5",
                "type": "multiple_choice",
                "question": "Mary Ainsworth classified infants who become distressed upon mother's departure but are quickly comforted upon her return as having:",
                "options": [
                    {"id": "opt1", "text": "Secure Attachment", "isCorrect": True},
                    {"id": "opt2", "text": "Insecure-Avoidant Attachment", "isCorrect": False},
                    {"id": "opt3", "text": "Insecure-Resistant Attachment", "isCorrect": False},
                    {"id": "opt4", "text": "Disorganized Attachment", "isCorrect": False}
                ],
                "explanation": "Secure attachment is shown by using the caregiver as a haven of safety and being easily soothed.",
                "xpReward": 15,
                "difficulty": 1
            },
            {
                "id": "sq3_q6",
                "type": "multiple_choice",
                "question": "The reduction in personal effort that occurs when individuals pool their work together in a collective group is known as:",
                "options": [
                    {"id": "opt1", "text": "Social Loafing", "isCorrect": True},
                    {"id": "opt2", "text": "Social Facilitation", "isCorrect": False},
                    {"id": "opt3", "text": "Groupthink", "isCorrect": False},
                    {"id": "opt4", "text": "Deindividuation", "isCorrect": False}
                ],
                "explanation": "Social loafing is the drop in personal exertion when responsibility is shared.",
                "xpReward": 15,
                "difficulty": 1
            },
            {
                "id": "sq3_q7",
                "type": "multiple_choice",
                "question": "Which Big Five personality dimension describes an individual who is highly organized, dependable, disciplined, and goal-oriented?",
                "options": [
                    {"id": "opt1", "text": "Conscientiousness", "isCorrect": True},
                    {"id": "opt2", "text": "Openness", "isCorrect": False},
                    {"id": "opt3", "text": "Agreeableness", "isCorrect": False},
                    {"id": "opt4", "text": "Neuroticism", "isCorrect": False}
                ],
                "explanation": "Conscientiousness reflects self-discipline, orderliness, and reliability.",
                "xpReward": 15,
                "difficulty": 1
            },
            {
                "id": "sq3_q8",
                "type": "true_false",
                "question": "Retroactive interference occurs when previously learned old memories prevent you from remembering newly acquired information.",
                "options": [
                    {"id": "opt1", "text": "True", "isCorrect": False},
                    {"id": "opt2", "text": "False", "isCorrect": True}
                ],
                "explanation": "False. Old memories disrupting new recall is Proactive interference. Retroactive interference is when new learning disrupts old recall.",
                "xpReward": 15,
                "difficulty": 2
            }
        ]
    }
    with open(sq_dir / "sq_intro_psychology_3.json", "w", encoding="utf-8") as f:
        json.dump(sq3_data, f, indent=2)

    print("✅ Side Quests generated successfully!")

if __name__ == "__main__":
    build_side_quests()
