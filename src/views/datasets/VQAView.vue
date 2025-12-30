<template>
    <div class="space-y-6">
        <DatasetSection :sections="sections" />
    </div>
</template>

<script setup>
import { ref, h } from 'vue'
import { useI18n } from 'vue-i18n'
import { NImage } from 'naive-ui'
import DatasetSection from './components/DatasetSection.vue'

const { t } = useI18n()

// 定义渲染图片的函数
const renderImage = (row) => {
    return h(NImage, {
        src: '/vqa.jpg', // Placeholder for all items as per requirement, or row.image if available
        alt: 'VQA Image',
        width: 100,
        height: 100,
        objectFit: 'contain',
        class: 'rounded border border-gray-200 bg-gray-50',
        lazy: true,
        intersectionObserverOptions: { rootMargin: '50px' }
    })
}

const vqaSingleData = [
    {
        "ID": "1",
        "Type": "Image Understanding",
        "Class": "手太阴腧穴",
        "Images": [
            "图3-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 列缺",
            "B. 云门",
            "C. 孔最",
            "D. 经渠"
        ],
        "Answer": "B"
    },
    {
        "ID": "2",
        "Type": "Image Understanding",
        "Class": "足太阳腧穴",
        "Images": [
            "图9-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 大杼",
            "B. 眉冲",
            "C. 天柱",
            "D. 风门"
        ],
        "Answer": "B"
    },
    {
        "ID": "3",
        "Type": "Image Understanding",
        "Class": "足厥阴腧穴",
        "Images": [
            "图14-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 急脉",
            "B. 大敦",
            "C. 阴廉",
            "D. 章门"
        ],
        "Answer": "B"
    },
    {
        "ID": "4",
        "Type": "Image Understanding",
        "Class": "足阳明腧穴",
        "Images": [
            "图5-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 承泣",
            "B. 缺盆",
            "C. 气舍",
            "D. 气户"
        ],
        "Answer": "A"
    },
    {
        "ID": "5",
        "Type": "Image Understanding",
        "Class": "手少阴腧穴",
        "Images": [
            "图7-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 青灵",
            "B. 神门",
            "C. 少冲",
            "D. 少府"
        ],
        "Answer": "A"
    },
]
const vqaMultiData = [
    {
        "ID": "1",
        "Type": "Image Understanding",
        "Class": "手厥阴腧穴",
        "Images": [
            "图11-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 天泉",
            "B. 天池",
            "C. 郄门",
            "D. 间使"
        ],
        "Answer": [
            "A",
            "B"
        ]
    },
    {
        "ID": "2",
        "Type": "Image Understanding",
        "Class": "足太阳腧穴",
        "Images": [
            "图9-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 天柱",
            "B. 玉枕",
            "C. 曲差",
            "D. 眉冲"
        ],
        "Answer": [
            "C",
            "D"
        ]
    },
    {
        "ID": "3",
        "Type": "Image Understanding",
        "Class": "足太阴腧穴",
        "Images": [
            "图6-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 隐白",
            "B. 大都",
            "C. 血海",
            "D. 箕门"
        ],
        "Answer": [
            "A",
            "B"
        ]
    },
    {
        "ID": "4",
        "Type": "Image Understanding",
        "Class": "足阳明腧穴",
        "Images": [
            "图5-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 水突",
            "B. 承泣",
            "C. 四白",
            "D. 人迎"
        ],
        "Answer": [
            "B",
            "C"
        ]
    },
    {
        "ID": "5",
        "Type": "Image Understanding",
        "Class": "手厥阴腧穴",
        "Images": [
            "图11-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 天池",
            "B. 郄门",
            "C. 曲泽",
            "D. 间使"
        ],
        "Answer": [
            "A",
            "C"
        ]
    },
]
const vqaType2Data = [
    {
        "ID": "1",
        "Type": "Image Understanding",
        "Class": "手太阴腧穴",
        "Acupoint name": "鱼际",
        "Images": [
            "图3-2-3.jpeg"
        ],
        "Question": "鱼际穴的正确定位是？",
        "Options": [
            "A. 第2掌骨桡侧中点赤白肉际处。",
            "B. 第1掌骨尺侧中点赤白肉际处。",
            "C. 第1掌骨桡侧中点赤白肉际处。",
            "D. 腕横纹上，尺侧腕屈肌腱的桡侧凹陷处。"
        ],
        "Answer": "C"
    },
    {
        "ID": "2",
        "Type": "Image Understanding",
        "Class": "足太阴腧穴",
        "Acupoint name": "太白",
        "Images": [
            "图6-2-2.jpeg"
        ],
        "Question": "太白的正确定位是？",
        "Options": [
            "A. 第1跖趾关节近端赤白肉际凹陷中",
            "B. 第1跖趾关节远端赤白肉际凹陷中",
            "C. 第2跖趾关节近端赤白肉际凹陷中",
            "D. 足大趾内侧，趾甲角旁0.1寸"
        ],
        "Answer": "A"
    },
    {
        "ID": "3",
        "Type": "Image Understanding",
        "Class": "足少阴腧穴",
        "Acupoint name": "灵墟",
        "Images": [
            "图10-2-7.jpeg"
        ],
        "Question": "灵墟的正确定位是？",
        "Options": [
            "A. 第2肋间隙，前正中线旁开2寸",
            "B. 第4肋间隙，前正中线旁开2寸",
            "C. 第3肋间隙，前正中线旁开3寸",
            "D. 第3肋间隙，前正中线旁开2寸"
        ],
        "Answer": "D"
    },
    {
        "ID": "4",
        "Type": " Image Understanding ",
        "Class": " 足厥阴腧穴 ",
        "Acupoint name": " 行间 ",
        "Images": [
            "图14-2-2.jpeg"
        ],
        "Question": " 行间的正确定位是？ ",
        "Options": [
            "A. 第2、3趾之间，趾蹼缘后方赤白肉际处",
            "B. 第1、2趾之间，趾蹼缘后方赤白肉际处",
            "C. 足背，第1、2趾结合部前方的凹陷中",
            "D. 掌心，第2、3掌骨之间，握拳时中指尖下"
        ],
        "Answer": "B"
    },
    {
        "ID": "5",
        "Type": "Image Understanding",
        "Class": "手太阳腧穴",
        "Acupoint name": "支正",
        "Images": [
            "图8-2-3.jpeg"
        ],
        "Question": "支正的正确定位是？",
        "Options": [
            "A. 腕背侧远端横纹上3寸，尺骨尺侧与尺侧腕屈肌之间。",
            "B. 腕掌侧远端横纹上5寸，尺骨尺侧与尺侧腕屈肌之间。",
            "C. 腕背侧远端横纹上5寸，桡骨桡侧与桡侧腕屈肌之间。",
            "D. 腕背侧远端横纹上5寸，尺骨尺侧与尺侧腕屈肌之间。"
        ],
        "Answer": "D"
    }
]
const vqaType3Data = [
    {
        "ID": "1",
        "Type": "Image Reasoning",
        "Class": "手厥阴腧穴",
        "Acupoint name": "曲泽",
        "Images": [
            "图11-2-2.jpeg"
        ],
        "Question": "曲泽穴的针灸操作正确的是？",
        "Options": [
            "A. 直刺1～1.5寸，或用三棱针点刺出血。",
            "B. 直刺0.5～1寸，局部酸胀。",
            "C. 平刺0.3～0.5寸，不宜深刺。",
            "D. 直刺1.5～2寸，针感向手指放射。"
        ],
        "Answer": "A"
    },
    {
        "ID": "2",
        "Type": "Image Reasoning",
        "Class": "足太阴腧穴",
        "Acupoint name": "三阴交",
        "Images": [
            "图6-2-3.jpeg"
        ],
        "Question": "三阴交穴的针灸操作正确的是？",
        "Options": [
            "A. 斜刺0.5～1寸，孕妇禁用。",
            "B. 直刺0.5～1寸，孕妇慎用。",
            "C. 直刺2～2.5寸，孕妇禁用。",
            "D. 直刺1～1.5寸，孕妇慎用。"
        ],
        "Answer": "D"
    },
    {
        "ID": "3",
        "Type": "Image Reasoning",
        "Class": "足阳明胃经腧穴",
        "Acupoint name": "下巨虚",
        "Images": [
            "图5-2-8.jpeg"
        ],
        "Question": "下巨虚穴的针灸操作正确的是？",
        "Options": [
            "A. 直刺0.5～1寸",
            "B. 直刺1～1.5寸",
            "C. 直刺1.5～2寸",
            "D. 斜刺0.8～1.2寸"
        ],
        "Answer": "B"
    },
    {
        "ID": "4",
        "Type": "Image Reasoning",
        "Class": "手太阴腧穴",
        "Acupoint name": "中府",
        "Images": [
            "图3-2-2.jpeg"
        ],
        "Question": "中府穴的针灸操作正确的是？",
        "Options": [
            "A. 向内斜刺0.5～0.8寸，不可向外深刺，以免伤及脏器",
            "B. 直刺1～1.5寸，可向内深刺，注意避开血管",
            "C. 向外平刺1～1.2寸，不可向内深刺，以免伤及神经",
            "D. 向外斜刺或平刺0.5～0.8寸，不可向内深刺，以免伤及脏器"
        ],
        "Answer": "D"
    },
    {
        "ID": "5",
        "Type": "Image Reasoning",
        "Class": "手少阳腧穴",
        "Acupoint name": "外关",
        "Images": [
            "图12-2-2.jpeg"
        ],
        "Question": "外关穴的针灸操作正确的是？",
        "Options": [
            "A. 直刺0.3～0.5寸",
            "B. 斜刺1～1.5寸",
            "C. 平刺0.8～1.2寸",
            "D. 直刺0.5～1寸"
        ],
        "Answer": "D"
    }
]

const renderAnswer = (row) => {
    const ans = Array.isArray(row.Answer) ? row.Answer.join(', ') : row.Answer
    return h('div', { class: 'font-medium text-primary' }, ans)
}

const baseColumns = [
    { title: 'ID', key: 'id', width: 60, render: (row) => row.ID || row.id },
    { title: () => t('datasets.columns.image'), key: 'image', width: 120, render: renderImage },
    { title: () => t('datasets.columns.category'), key: 'Class', width: 120 },
    { title: () => t('datasets.columns.question'), key: 'Question', width: 200, ellipsis: { tooltip: true } },
    { title: () => t('datasets.columns.option_a'), key: 'option_a', width: 150, render: (row) => (row.Options && row.Options[0]) || '' },
    { title: () => t('datasets.columns.option_b'), key: 'option_b', width: 150, render: (row) => (row.Options && row.Options[1]) || '' },
    { title: () => t('datasets.columns.option_c'), key: 'option_c', width: 150, render: (row) => (row.Options && row.Options[2]) || '' },
    { title: () => t('datasets.columns.option_d'), key: 'option_d', width: 150, render: (row) => (row.Options && row.Options[3]) || '' },
    { title: () => t('datasets.columns.answer'), key: 'Answer', width: 100, render: renderAnswer }
]

const acupointColumns = [
    { title: 'ID', key: 'id', width: 60, render: (row) => row.ID || row.id },
    { title: () => t('datasets.columns.image'), key: 'image', width: 120, render: renderImage },
    { title: () => t('datasets.columns.category'), key: 'Class', width: 120 },
    { title: () => t('datasets.columns.acupoint_name'), key: 'Acupoint name', width: 100 },
    { title: () => t('datasets.columns.question'), key: 'Question', width: 200, ellipsis: { tooltip: true } },
    { title: () => t('datasets.columns.option_a'), key: 'option_a', width: 150, render: (row) => (row.Options && row.Options[0]) || '' },
    { title: () => t('datasets.columns.option_b'), key: 'option_b', width: 150, render: (row) => (row.Options && row.Options[1]) || '' },
    { title: () => t('datasets.columns.option_c'), key: 'option_c', width: 150, render: (row) => (row.Options && row.Options[2]) || '' },
    { title: () => t('datasets.columns.option_d'), key: 'option_d', width: 150, render: (row) => (row.Options && row.Options[3]) || '' },
    { title: () => t('datasets.columns.answer'), key: 'Answer', width: 100, render: renderAnswer }
]

const sections = ref([
    {
        title: () => t('datasets.vqa.single.title'),
        description: () => t('datasets.vqa.single.description'),
        githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A1.json',
        columns: baseColumns,
        data: vqaSingleData,
        scrollX: 1300,
        codeExample: `
{
    "ID": "1",
    "Type": "Image Understanding",
    "Class": "手太阴腧穴",
    "Images": [
        "图3-2-2.jpeg"
    ],
    "Question": "图片中可能包含选项中的哪些穴位？",
    "Options": [
        "A. 列缺",
        "B. 云门",
        "C. 孔最",
        "D. 经渠"
    ],
    "Answer": "B"
}`
    },
    {
        title: () => t('datasets.vqa.multi.title'),
        description: () => t('datasets.vqa.multi.description'),
        githubLink: '',
        columns: baseColumns,
        data: vqaMultiData,
        scrollX: 1300,
        codeExample: `
{
    "ID": "1",
    "Type": "Image Understanding",
    "Class": "手厥阴腧穴",
    "Images": [
        "图11-2-2.jpeg"
    ],
    "Question": "图片中可能包含选项中的哪些穴位？",
    "Options": [
        "A. 天泉",
        "B. 天池",
        "C. 郄门",
        "D. 间使"
    ],
    "Answer": [
        "A",
        "B"
    ]
}`
    },
    {
        title: () => t('datasets.vqa.type2.title'),
        description: () => t('datasets.vqa.type2.description'),
        githubLink: '',
        columns: acupointColumns,
        data: vqaType2Data,
        codeExample: `
{
    "ID": "1",
    "Type": "Image Understanding",
    "Class": "手太阴腧穴",
    "Acupoint name": "鱼际",
    "Images": [
        "图3-2-3.jpeg"
    ],
    "Question": "鱼际穴的正确定位是？",
    "Options": [
        "A. 第2掌骨桡侧中点赤白肉际处。",
        "B. 第1掌骨尺侧中点赤白肉际处。",
        "C. 第1掌骨桡侧中点赤白肉际处。",
        "D. 腕横纹上，尺侧腕屈肌腱的桡侧凹陷处。"
    ],
    "Answer": "C"
}`
    },
    {
        title: () => t('datasets.vqa.type3.title'),
        description: () => t('datasets.vqa.type3.description'),
        githubLink: '',
        columns: acupointColumns,
        data: vqaType3Data,
        scrollX: 1300,
        codeExample: `
{
    "ID": "1",
    "Type": "Image Reasoning",
    "Class": "手厥阴腧穴",
    "Acupoint name": "曲泽",
    "Images": [
        "图11-2-2.jpeg"
    ],
    "Question": "曲泽穴的针灸操作正确的是？",
    "Options": [
        "A. 直刺1～1.5寸，或用三棱针点刺出血。",
        "B. 直刺0.5～1寸，局部酸胀。",
        "C. 平刺0.3～0.5寸，不宜深刺。",
        "D. 直刺1.5～2寸，针感向手指放射。"
    ],
    "Answer": "A"
}`
    }
])
</script>
