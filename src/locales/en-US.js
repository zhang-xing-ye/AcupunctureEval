export default {
    nav: {
        home: 'Home',
        data: 'Data',
        data_choice: 'Multiple Choice',
        data_qa: 'QA',
        data_vqa: 'VQA',
        data_video: 'Video',
        leaderboard: 'Leaderboard',
        github: 'GitHub'
    },
    common: {
        language: 'Language',
        switch_lang: 'Switch Language',
        view_on_github: 'View on GitHub'
    },
    home: {
        stats: {
            choice_count: 'Choice Questions',
            qa_count: 'QA Pairs',
            video_count: 'Videos'
        },
        intro: {
            title: 'About TCM Benchmark',
            content: 'TCM Benchmark is a comprehensive evaluation platform dedicated to advancing Artificial Intelligence in Traditional Chinese Medicine (TCM). We integrate massive amounts of TCM literature, clinical cases, medical examinations, and multimodal data to provide a holistic and multi-level assessment of Large Language Models. Through a standardized evaluation system, we aim to objectively reflect model performance in core tasks such as TCM theory understanding, clinical auxiliary diagnosis, and prescription recommendation, fostering the deep integration and innovative development of TCM and modern AI technologies.'
        },
        images: {
            img1_title: 'Dataset Classification',
            img1_desc: 'Covering multi-dimensional data classification systems including TCM basic theory, clinical specialties, and prescription science.',
            img2_title: 'Acupoint Classification',
            img2_desc: 'Fine-grained visual recognition and localization tasks based on standard meridian acupoint charts.',
            img3_title: 'Validation & Testing',
            img3_desc: 'Scientifically rigorous division of training, validation, and test datasets to ensure the fairness of evaluation results.'
        },
        charts: {
            chart1_title: 'Dataset Distribution Overview',
            chart2_title: 'Subject Domain Statistics'
        }
    },
    datasets: {
        index: {
            browse_desc: 'Browse and search datasets related to {type}.',
            label_choice: 'Choice',
            label_qa: 'QA',
            label_vqa: 'VQA',
            label_video: 'Video'
        },
        columns: {
            id: 'ID',
            question: 'Question',
            answer: 'Answer',
            option_a: 'Option A',
            option_b: 'Option B',
            option_c: 'Option C',
            option_d: 'Option D',
            option_e: 'Option E',
            image: 'Image',
            options_answer: 'Options/Answer',
            video_title: 'Video Title',
            duration: 'Duration',
            category: 'Category',
            description: 'Description'
        },
        choice: {
            a1: {
                title: 'Type A1 (Single Sentence Best Choice)',
                desc: 'Each question consists of a stem and 5 options. The stem describes a single element.'
            },
            a2: {
                title: 'Type A2 (Case Summary Best Choice)',
                desc: 'The stem is a brief medical record, followed by 5 options with only one best choice.'
            },
            a3: {
                title: 'Type A3 (Case Group Best Choice)',
                desc: 'Starts with a patient-centered clinical scenario, followed by 2-3 related questions.'
            },
            a4: {
                title: 'Type A4 (Case Series Best Choice)',
                desc: 'Starts with a single patient or family-centered clinical scenario, followed by 3-6 related questions.'
            },
            b: {
                title: 'Type B (Standard Matching)',
                desc: 'Starts with 5 options, followed by at least 2 questions. Candidates must choose the closely related option for each question.'
            },
            x: {
                title: 'Type X (Multiple Choice)',
                desc: 'Consists of a stem and 5 options. Candidates must choose 2 or more correct answers.'
            }
        },
        qa: {
            tcm: {
                title: 'TCM QA',
                desc: 'QA dataset for TCM theory and clinical knowledge.'
            },
            acu: {
                title: 'ACU QA (Acupuncture)',
                desc: 'Professional QA data focused on acupuncture.'
            },
            mra: {
                title: 'MRA QA (Case Analysis)',
                desc: 'Analysis and diagnostic QA based on real clinical cases.'
            }
        },
        vqa: {
            type1: {
                title: 'VQA Type 1 (Single/Multiple Choice)',
                description: 'Image-based TCM diagnosis and identification questions.'
            },
            type2: {
                title: 'VQA Type 2 (Localization)',
                description: 'Precise localization and identification of acupoints and body parts.'
            },
            type3: {
                title: 'VQA Type 3 (Acupuncture Operation)',
                description: 'Visual QA for acupuncture techniques and operation procedures.'
            }
        },
        video: {
            section1_title: 'Operation Demo (Video 1)',
            section1_desc: 'Demonstration of basic acupuncture techniques.',
            section2_title: 'Clinical Diagnosis (Video 2)',
            section2_desc: 'Recording of the four diagnostic methods in a real clinical environment.',
            metadata_title: 'Video Metadata List'
        }
    },
    leaderboard: {
        title: 'Model Leaderboard',
        description: 'Ranking of large models on various TCM tasks.',
        tabs: {
            overall: 'Overall',
            choice: 'Choice',
            qa: 'QA',
            vqa: 'VQA',
            video: 'Video'
        },
        columns: {
            rank: 'Rank',
            model: 'Model',
            score: 'Avg Score',
            choice_score: 'Choice',
            qa_score: 'QA',
            vqa_score: 'VQA',
            video_score: 'Video',
            params: 'Params',
            org: 'Organization'
        }
    }
}
