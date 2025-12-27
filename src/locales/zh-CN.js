export default {
    nav: {
        home: '主页',
        data: '数据',
        data_choice: '选择题',
        data_qa: '问答对',
        data_vqa: '视觉问答对',
        data_video: '视频',
        leaderboard: '排行榜',
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
            video_count: '视频数量'
        },
        intro: {
            title: '关于 TCM Benchmark',
            content: 'TCM Benchmark 是一个致力于推动中医人工智能发展的综合性评测基准平台。我们整合了海量的中医文献、临床医案、医学试题及多模态数据，旨在为大语言模型提供全方位、多层次的能力评估。通过标准化的评测体系，我们期望能够客观反映模型在中医理论理解、临床辅助诊疗、方剂推荐等核心任务上的表现，促进中医与现代人工智能技术的深度融合与创新发展。'
        },
        images: {
            img1_title: '数据集分类',
            img1_desc: '涵盖中医基础理论、临床各科、方剂学等多维度数据分类体系。',
            img2_title: '穴位分类',
            img2_desc: '基于标准经络穴位图谱的精细化视觉识别与定位任务。',
            img3_title: '验证与测试',
            img3_desc: '科学严谨的训练、验证与测试数据集划分，确保评测结果的公正性。'
        },
        charts: {
            chart1_title: '数据集分布概览',
            chart2_title: '学科领域数据统计'
        }
    },
    datasets: {
        index: {
            browse_desc: '浏览与检索 {type} 相关的数据集资源。',
            label_choice: '选择题',
            label_qa: '问答对',
            label_vqa: '视觉问答',
            label_video: '视频'
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
            video_title: '视频标题',
            duration: '时长',
            category: '分类',
            description: '描述'
        },
        choice: {
            a1: {
                title: 'A1 型题 (单句型最佳选择题)',
                desc: '每道试题由1个题干和5个供选择的备选答案组成。题干以叙述一个单一要素为特征，是为“单句型”。'
            },
            a2: {
                title: 'A2 型题 (病例摘要型最佳选择题)',
                desc: '试题结构是由1个简要病历作为题干、5个供选择的备选答案组成，备选答案中只有1个是最佳选择。'
            },
            a3: {
                title: 'A3 型题 (病例组型最佳选择题)',
                desc: '试题结构是开始叙述一个以患者为中心的临床情景，然后提出2个～3个相关问题。'
            },
            a4: {
                title: 'A4 型题 (病例串型最佳选择题)',
                desc: '开始叙述一个以单一患者或家庭为中心的临床情景，然后提出3个～6个相关问题。'
            },
            b: {
                title: 'B 型题 (标准配伍题)',
                desc: '试题开始是5个备选答案，备选答案后提出至少2道试题，要求应试者为每一道试题选择一个与其关系密切的答案。'
            },
            x: {
                title: 'X 型题 (多选题)',
                desc: '由1个题干和5个备选答案组成。题干在前，备选答案在后。要求考生从5个备选答案中选出2个或2个以上的正确答案。'
            }
        },
        qa: {
            tcm: {
                title: 'TCM 问答对',
                desc: '中医理论与临床知识的问答数据集。'
            },
            acu: {
                title: 'ACU 问答对 (针灸)',
                desc: '专注于针灸领域的专业问答数据。'
            },
            mra: {
                title: 'MRA 问答对 (病案分析)',
                desc: '基于真实临床病案的分析与诊断问答。'
            }
        },
        vqa: {
            type1: {
                title: 'VQA 第一类题型 (单选/多选)',
                description: '基于图像的中医诊断与辨识单选或多选题。'
            },
            type2: {
                title: 'VQA 第二类题型 (定位题)',
                description: '穴位与身体部位的精确定位识别。'
            },
            type3: {
                title: 'VQA 第三类题型 (针灸操作)',
                description: '针灸手法与操作流程的视觉问答。'
            }
        },
        video: {
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
            overall: '总榜',
            choice: '选择题',
            qa: '问答对',
            vqa: '视觉问答',
            video: '视频理解'
        },
        columns: {
            rank: '排名',
            model: '模型名称',
            score: '平均分',
            choice_score: '选择题',
            qa_score: '问答',
            vqa_score: '视觉问答',
            video_score: '视频',
            params: '参数量',
            org: '机构'
        }
    }
}
