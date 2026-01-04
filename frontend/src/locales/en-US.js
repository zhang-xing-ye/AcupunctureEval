export default {
    nav: {
        home: 'Home',
        data: 'Data',
        // data_choice: 'AcupunctureMultiple Choice',
        data_qa: 'AcupunctureQA',
        data_vqa: 'AcupunctureVQA',
        data_video: 'AcupunctureVideo',
        leaderboard: 'Leaderboard',
        evaluate: 'Evaluate',
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
            dataset_classify_desc: 'There are 45,962 subjective question samples, covering four main domains: Acupuncture, TCM Syndromes, Moxibustion, and Massage.',
            vqa_classify_title: 'AcupunctureVQA Objective Questions Classification',
            vqa_classify_desc: 'AcupunctureVQA objective questions consist of 996 samples, categorized into Single Choice, Multiple Choice, Acupuncture Manipulation, and Acupoint Localization.',
            xuewei_classify_title: 'Human Acupoint Classification',
            xuewei_classify_desc: 'The video data involves 20 types of human acupoints, mainly including Xuehai, Yanglingquan, Yinlingquan, and Zusanli.',
            pig_xuewei_title: 'Pig Acupoint Classification',
            pig_xuewei_desc: 'The video data involves 7 types of pig acupoints.',
            tcm_symptom_title: 'Data Visualization of TCM Symptoms in Otorhinolaryngology',
            tcm_symptom_desc: 'Data Clustering Chart of TCM Symptoms in Otorhinolaryngology',
            figure_strice_title: 'Data Visualization of Acupoints of the Lung Meridian of Hand-Taiyin',
            figure_strice_desc: 'Data Clustering Chart of Acupoints of the Lung Meridian of Hand-Taiyin'
        },
        charts: {
            chart1_title: 'Dataset Distribution Overview',
            chart2_title: 'Video Comprehension Analysis'
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
            desc: 'AcupunctureQA consists of three parts: objective multiple-choice questions, subjective Q&A, and case analysis. The data for objective questions and case analysis are derived from textbooks rather than scattered internet question banks, ensuring data quality. Among them, there are 1,735 objective question samples covering three major categories: Meridians and Acupoints, Acupuncture and Moxibustion, and TCM Syndromes; the case analysis questions contain 100 samples, covering seven dimensions such as etiology and pathogenesis. The subjective Q&A contains 45,962 Q&A pair samples, covering four main domains: Acupuncture, TCM Syndromes, Moxibustion, and Massage.',
            tcm: {
                title: 'TCM Disease Q&A Pairs',
                desc: 'The TCM Disease Q&A dataset covers 4 departments and 108 diseases.'
            },
            acu: {
                title: 'Acupuncture Domain Q&A Pairs',
                desc: 'The Acupuncture Domain Q&A dataset contains a total of 20,841 data entries, including 5,205 for Acupuncture, 644 for Moxibustion, 12,576 for Acupoints, and 1,416 for Massage.'
            },
            mra: {
                title: 'Case Analysis Q&A Pairs',
                desc: 'The Case Analysis questions consist of 100 samples covering 7 dimensions including etiology and pathogenesis.'
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
            qa_objective: 'QA Objective Leaderboard',
            vqa: 'VQA Leaderboard'
        },
        columns: {
            rank: 'Rank',
            model: 'Model',
            average: 'Average',
            a1: 'A1',
            a2: 'A2',
            a3: 'A3',
            a4: 'A4',
            b: 'B',
            x: 'X',
            single_choice: 'Single Choice',
            multiple_choice: 'Multiple Choice',
            localization: 'Localization',
            operation: 'Operation'
        }
    },
    evaluate: {
        title: 'Model Evaluation',
        description: 'Upload your model predictions for evaluation.',
        qa_title: 'QA Objective Evaluation',
        vqa_title: 'VQA Evaluation',
        upload_guide: 'Please upload prediction files in JSON format.',
        upload_button: 'Select Files',
        submit_button: 'Start Evaluation',
        submitting: 'Evaluating...',
        success_message: 'Evaluation submitted successfully!',
        llm_name_label: 'Model Name',
        llm_name_placeholder: 'Enter model name',
        llm_org_label: 'Organization',
        llm_org_placeholder: 'Enter organization name (optional)',
        error_file_type: 'Only JSON files are allowed',
        error_no_file: 'Please upload files first',
        qa_instruction: 'Please upload the following 6 JSON prediction files separately.',
        vqa_instruction: 'Please upload the following 4 JSON prediction files separately.',
        wait_upload: 'Please wait for all files to finish uploading',
        reference_button: 'Reference Case',
        reference_title: 'Reference Case',
        reference_description: 'The following is an example of the submission file format. Please ensure your JSON file contains an output field for model predictions.',
        close: 'Close',
        file_types: {
            qa: {
                a1: 'Type A1',
                a2: 'Type A2',
                a3: 'Type A3',
                a4: 'Type A4',
                b: 'Type B',
                x: 'Type X'
            },
            vqa: {
                single: 'Single Choice',
                multi: 'Multiple Choice',
                localization: 'Localization',
                operation: 'Operation'
            }
        },
        missing_files: 'Missing files: {files}',
        upload_success: 'File {name} uploaded successfully'
    }
}
