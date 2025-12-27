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

// Render function for image column
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

const commonColumns = [
    { title: 'ID', key: 'id', width: 60 },
    { title: () => t('datasets.columns.image'), key: 'image', width: 120, render: renderImage },
    { title: () => t('datasets.columns.question'), key: 'question' },
    { title: () => t('datasets.columns.options_answer'), key: 'options_answer', ellipsis: { tooltip: true } }
]

const vqaType1Data = [
    { id: 1, question: "图中所示舌象特征是什么？", options_answer: "A. 舌红苔黄 B. 舌淡苔白 ... 答案: A" },
    { id: 2, question: "该面部气色反映了什么病理状态？", options_answer: "答案: 脾虚湿盛" },
    { id: 3, question: "图中草药的名称是？", options_answer: "A. 人参 B. 黄芪 ... 答案: A" },
    { id: 4, question: "舌下络脉迂曲提示什么？", options_answer: "答案: 气滞血瘀" },
    { id: 5, question: "图中穴位定位是否正确？", options_answer: "答案: 正确" }
]

const sections = ref([
    {
        title: () => t('datasets.vqa.type1.title'),
        description: () => t('datasets.vqa.type1.description'),
        githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A1.json',
        columns: commonColumns,
        data: vqaType1Data,
        codeExample: `
{
  "image_id": "img_001.jpg",
  "question": "图中所示舌象特征是什么？",
  "options": ["A. 舌红苔黄", "B. 舌淡苔白"],
  "answer": "A"
}`
    },
    {
        title: () => t('datasets.vqa.type2.title'),
        description: () => t('datasets.vqa.type2.description'),
        githubLink: '',
        columns: commonColumns,
        data: [], // Placeholder
        codeExample: `
{
  "image_id": "acu_001.jpg",
  "question": "请指出合谷穴的位置",
  "bbox": [100, 200, 150, 250]
}`
    },
    {
        title: () => t('datasets.vqa.type3.title'),
        description: () => t('datasets.vqa.type3.description'),
        githubLink: '',
        columns: commonColumns,
        data: [], // Placeholder
        codeExample: `
{
  "video_id": "video_001.mp4",
  "question": "该视频演示的是哪种补泻手法？",
  "answer": "提插补法"
}`
    }
])
</script>
