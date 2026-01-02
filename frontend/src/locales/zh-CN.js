export default {
    nav: {
        home: '主页',
        data: '数据',
        // data_choice: '选择题',
        data_qa: 'AcupunctureQA',
        data_vqa: 'AcupunctureVQA',
        data_video: 'AcupunctureVideo',
        leaderboard: '排行榜',
        evaluate: '评估',
        github: 'GitHub'
    },
    common: {
        language: '语言',
        switch_lang: '切换语言',
        view_on_github: '在 GitHub 上查看'
    },
    home: {
        stats: {
            choice_count: '选择题数量',
            qa_count: '问答对数量',
            vqa_count: '视觉问答对数量',
            video_count: '视频数量'
        },
        intro: {
            title: '关于 AcupunctureEval',
            content: 'AcupunctureEval 是一个致力于推动中医针灸领域人工智能发展的综合性评测基准平台。我们整合了海量的中医针灸文献、临床医案、医学试题及多模态数据，旨在为大语言模型提供全方位、多层次的能力评估。通过标准化的评测体系，我们期望能够客观反映模型在中医针灸理论理解、临床辅助诊疗等核心任务上的表现，促进中医针灸与现代人工智能技术的深度融合与创新发展。'
        },
        images: {
            val_test_title: 'AcupunctureQA客观题分类',
            val_test_desc: '客观题数据来源于教科书，其共有1735个样本涵盖经络腧穴、刺灸和中医病症三大类；其分为1516个样本的验证集与219个样本的测试集。每一类数据集中都包含A1、A2、A3、A4、B与X型题',
            dataset_classify_title: 'AcupunctureQA主观题分类',
            dataset_classify_desc: '主观题共有45962个样本，涵盖四大主要领域：针灸、中医证候、艾灸和推拿',
            vqa_classify_title: 'AcupunctureVQA客观题分类',
            vqa_classify_desc: 'AcupunctureVQA客观题共有996个样本，分为单选题、多选题、针灸操作题、穴位定位题',
            xuewei_classify_title: '人体穴位分类',
            xuewei_classify_desc: '在视频数据中共涉及到人体的20种穴位，主要的有血海穴、阳陵泉穴、阴陵泉穴和足三里穴',
            pig_xuewei_title: '猪体穴位分类',
            pig_xuewei_desc: '在视频数据中共涉及到猪体7种穴位',
            tcm_symptom_title: '耳鼻喉科中中医症状的数据可视化',
            tcm_symptom_desc: '耳鼻喉科中中医症状的数据聚类图',
            figure_strice_title: '手太阴肺经穴位的数据可视化',
            figure_strice_desc: '手太阴肺经穴位的数据聚类图'
        },
        charts: {
            chart1_title: '数据集分布概览',
            chart2_title: '学科领域数据统计'
        }
    },
    datasets: {
        index: {
            // browse_desc: '浏览与检索 {type} 相关的数据集资源。',
            label_qa: 'AcupunctureQA',
            label_vqa: 'AcupunctureVQA',
            label_video: 'AcupunctureVideo'
        },
        columns: {
            id: 'ID',
            question: '问题',
            answer: '答案',
            option_a: '选项 A',
            option_b: '选项 B',
            option_c: '选项 C',
            option_d: '选项 D',
            option_e: '选项 E',
            image: '图片',
            options_answer: '选项/答案',
            options: '选项',
            acupoint_name: '穴位名称',
            video_title: '视频标题',
            duration: '时长',
            category: '分类',
            description: '描述',
            shared_query: '共享题干',
            shared_option: '共享选项',
            diagnose: '诊断',
            syndromes: '证型',
            therapy: '治法',
            prescription: '处方',
            prescription_meaning: '方义',
            operation: '操作'
        },
        choice: {
            a1: {
                title: 'A1 型题',
                desc: '每道试题由1个题干和5个供选择的备选答案组成。每题只有一个正确答案。'
            },
            a2: {
                title: 'A2 型题',
                desc: '试题结构是由1个简要病历作为题干、5个供选择的备选答案组成，每题只有一个正确答案。'
            },
            a3: {
                title: 'A3 型题',
                desc: '试题结构是开始叙述一个以患者为中心的临床情景，然后提出2个个相关问题。每题只有一个正确答案。'
            },
            a4: {
                title: 'A4 型题',
                desc: '试题结构是开始叙述一个以患者为中心的临床情景，然后提出3个相关问题。每题只有一个正确答案。'
            },
            b: {
                title: 'B 型题',
                desc: '试题开始是5个备选答案，备选答案后提出2道试题，要求应试者为每一道试题选择一个正确答案。'
            },
            x: {
                title: 'X 型题',
                desc: '由1个题干和5个备选答案组成。多选题型每题有多个正确答案。'
            }
        },
        qa: {
            desc: 'AcupunctureQA包含客观选择题、主观问答题和病例分析题三部分。客观题和病例分析题的数据来源于教科书，而非零散的互联网题库，从而保证了数据的质量。其中，客观题有1735个样本，涵盖经络腧穴、针灸和中医病症三大类；病例分析题有100个样本，包含病例的病因病机等七个维度。主观问答题含有45,962个问答对样本，涵盖四大主要领域：针灸、中医证候、艾灸和推拿。',
            tcm: {
                title: '中医疾病问答对',
                desc: '中医疾病问答对数据集共涵盖4个科室与108种疾病'
            },
            acu: {
                title: '针灸领域问答对',
                desc: '针灸领域问答对数据集共包含20841条数据，其中针灸5205条数据、艾灸644条数据、穴位12576条数据和推拿1416条数据'
            },
            mra: {
                title: '病例分析问答对',
                desc: '病例分析题有100个样本包含病例的病因病机等7个纬度'
            }
        },
        vqa: {
            desc: 'AcupunctureVQA，共构造10729个数据样本，包含图像理解和图像推理两类任务。',
            single: {
                title: 'VQA单选题',
                description: '基于图像的中医诊断与辨识单选或多选题。'
            },
            multi: {
                title: 'VQA多选题',
                description: '基于图像的中医诊断与辨识多选题。'
            },
            type2: {
                title: 'VQA穴位定位题',
                description: '穴位与身体部位的精确定位识别。'
            },
            type3: {
                title: 'VQA针灸操作题',
                description: '针灸手法与操作流程的视觉问答。'
            }
        },
        video: {
            desc: '关于针灸穴位实践操作的视频被构建命名为AcupunctureVideo ，视频共1000个样本并分为三类，第一类是针灸师对人体针灸穴位的标准手法实践操作。第二类是专家在真实临床场景下对患者的实际操作视频，第三类是针灸师对实验猪针灸穴位的标准手法实践操作。',
            section1_title: '操作演示视频 (Video 1)',
            section1_desc: '展示针灸提插捻转的基本手法演示。',
            section2_title: '临床诊疗视频 (Video 2)',
            section2_desc: '记录真实临床环境下的望闻问切过程。',
            metadata_title: '视频元数据列表'
        }
    },
    leaderboard: {
        title: '模型排行榜',
        description: '展示各大模型在中医各个任务上的性能表现排名。',
        tabs: {
            qa_objective: 'QA客观题排行榜',
            vqa: 'VQA排行榜'
        },
        columns: {
            rank: '排名',
            model: '模型名称',
            average: '平均分',
            a1: 'A1',
            a2: 'A2',
            a3: 'A3',
            a4: 'A4',
            b: 'B',
            x: 'X',
            single_choice: '单选题',
            multiple_choice: '多选题',
            localization: '定位题',
            operation: '操作题'
        }
    },
    evaluate: {
        title: '模型评估',
        description: '上传您的模型预测结果进行评估。',
        qa_title: 'QA 客观题评估',
        vqa_title: 'VQA 评估',
        upload_guide: '请上传 JSON 格式的预测结果文件。',
        upload_button: '选择文件',
        submit_button: '开始评估',
        submitting: '评估中...',
        success_message: '评估提交成功！',
        llm_name_label: '模型名称',
        llm_name_placeholder: '请输入模型名称',
        llm_org_label: '所属组织',
        llm_org_placeholder: '请输入组织名称 (可选)',
        error_file_type: '只能上传 JSON 文件',
        error_no_file: '请先上传文件',
        qa_instruction: '请分别上传以下6个类型的 JSON 预测结果文件。',
        vqa_instruction: '请分别上传以下4个类型的 JSON 预测结果文件。',
        wait_upload: '请等待所有文件上传完成',
        reference_button: '参考案例',
        reference_title: '参考案例',
        reference_description: '以下是提交文件的格式示例，请确保您的 JSON 文件中以output字段作为模型输出。',
        close: '关闭',
        file_types: {
            qa: {
                a1: 'A1型题',
                a2: 'A2型题',
                a3: 'A3型题',
                a4: 'A4型题',
                b: 'B型题',
                x: 'X型题'
            },
            vqa: {
                single: '单选题',
                multi: '多选题',
                localization: '定位题',
                operation: '操作题'
            }
        },
        missing_files: '缺少文件: {files}',
        upload_success: '文件 {name} 上传成功'
    }
}
