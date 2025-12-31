export default {
    nav: {
        home: 'Home',
        data: 'Data',
        // data_choice: 'AcupunctureMultiple Choice',
        data_qa: 'AcupunctureQA',
        data_vqa: 'AcupunctureVQA',
        data_video: 'AcupunctureVideo',
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
            vqa_count: 'VQA Pairs',
            video_count: 'Videos'
        },
        intro: {
            title: 'About AcupunctureEval',
            content: 'AcupunctureEval is a comprehensive evaluation benchmark platform dedicated to advancing the development of Artificial Intelligence in the field of TCM Acupuncture. We integrate massive amounts of TCM acupuncture literature, clinical cases, medical examinations, and multimodal data to provide a holistic and multi-level capability assessment for Large Language Models. Through a standardized evaluation system, we aim to objectively reflect model performance in core tasks such as TCM acupuncture theory understanding and clinical auxiliary diagnosis, fostering the deep integration and innovative development of TCM acupuncture and modern AI technologies.'
        },
        images: {
            val_test_title: 'AcupunctureQA Objective Questions Classification',
            val_test_desc: 'The objective question data originates from textbooks, totaling 1,735 samples covering three major categories: Meridians and Acupoints, Acupuncture and Moxibustion, and TCM Syndromes. It is divided into a validation set of 1,516 samples and a test set of 219 samples. Each category includes question types A1, A2, A3, A4, B, and X.',
            dataset_classify_title: 'AcupunctureQA Subjective Questions Classification',
            dataset_classify_desc: 'There are 19,841 subjective question samples, covering four main domains: Acupuncture, TCM Syndromes, Moxibustion, and Acupoints.',
            vqa_classify_title: 'AcupunctureVQA Objective Questions Classification',
            vqa_classify_desc: 'AcupunctureVQA objective questions consist of 996 samples, categorized into Single Choice, Multiple Choice, Acupuncture Manipulation, and Acupoint Localization.',
            xuewei_classify_title: 'Human Acupoint Classification',
            xuewei_classify_desc: 'The video data involves 20 types of human acupoints, mainly including Xuehai, Yanglingquan, Yinlingquan, and Zusanli.',
            pig_xuewei_title: 'Pig Acupoint Classification',
            pig_xuewei_desc: 'The video data involves 7 types of pig acupoints, specifically',
        },
        charts: {
            chart1_title: 'Dataset Distribution Overview',
            chart2_title: 'Subject Domain Statistics'
        }
    },
    datasets: {
        index: {
            // browse_desc: 'Browse and search datasets related to {type}.',
            label_qa: 'AcupunctureQA',
            label_vqa: 'AcupunctureVQA',
            label_video: 'AcupunctureVideo'
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
            options: 'Options',
            acupoint_name: 'Acupoint Name',
            video_title: 'Video Title',
            duration: 'Duration',
            category: 'Category',
            description: 'Description',
            shared_query: 'Shared Case',
            shared_option: 'Shared Options',
            diagnose: 'Diagnosis',
            syndromes: 'Syndromes',
            therapy: 'Therapy',
            prescription: 'Prescription',
            prescription_meaning: 'Prescription Analysis',
            operation: 'Operation'
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
            desc: 'AcupunctureVQA, with a total of 10,729 data samples, includes two types of tasks: image understanding and image reasoning.',
            single: {
                title: 'VQA Single Choice',
                description: 'Image-based TCM diagnosis and identification single or multiple choice questions.'
            },
            multi: {
                title: 'VQA Multiple Choice',
                description: 'Image-based TCM diagnosis and identification multiple choice questions.'
            },
            type2: {
                title: 'VQA Localization',
                description: 'Precise localization and identification of acupoints and body parts.'
            },
            type3: {
                title: 'VQA Acupuncture Operation',
                description: 'Visual QA for acupuncture techniques and operation procedures.'
            }
        },
        video: {
            desc: 'The AcupunctureVideo dataset, constructed for practical acupuncture point operations, consists of 1,000 samples divided into three categories: the first category features standard practical operation demonstrations by acupuncturists on human acupuncture points; the second category contains videos of experts performing actual operations on patients in real clinical scenarios; the third category features standard practical operation demonstrations by acupuncturists on experimental pig acupuncture points.',
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
