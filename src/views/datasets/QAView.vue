<template>
    <DatasetSection :sections="sections" />
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import DatasetSection from './components/DatasetSection.vue'

const { t } = useI18n()

const commonColumns = [
    { title: () => t('datasets.columns.id'), key: 'id', width: 80 },
    { title: () => t('datasets.columns.question'), key: 'question', ellipsis: { tooltip: true } },
    { title: () => t('datasets.columns.answer'), key: 'answer', ellipsis: { tooltip: true } }
]

const tcmData = [
    { id: 1, question: "中医如何治疗感冒？", answer: "中医治疗感冒主要依据辨证论治，分为风寒感冒、风热感冒、暑湿感冒等。风寒感冒常用荆防达表汤或通宣理肺丸；风热感冒常用银翘散或桑菊饮；暑湿感冒常用新加香薷饮。" },
    { id: 2, question: "什么是“气虚”？", answer: "气虚是指元气不足，脏腑功能减退，抗病能力下降的病理状态。主要表现为神疲乏力、少气懒言、自汗、舌淡苔白、脉虚无力等。" },
    { id: 3, question: "针灸的作用是什么？", answer: "针灸具有疏通经络、调和阴阳、扶正祛邪的作用。通过刺激穴位，调节人体气血运行，从而达到治疗疾病的目的。" },
    { id: 4, question: "六味地黄丸的主治是什么？", answer: "六味地黄丸主要滋补肾阴。主治肾阴亏损，头晕耳鸣，腰膝酸软，骨蒸潮热，盗汗遗精，消渴等证。" },
    { id: 5, question: "中医的“四诊”是指什么？", answer: "四诊是指望、闻、问、切四种诊察疾病的方法。望诊观气色神态；闻诊听声息气味；问诊询病情症状；切诊摸脉象体征。" }
]

const sections = ref([
    {
        title: () => t('datasets.qa.tcm.title'),
        description: () => t('datasets.qa.tcm.desc'),
        githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Clin/CMB-Clin.json',
        columns: commonColumns,
        data: tcmData,
        codeExample: `
{
  "question": "中医如何治疗感冒？",
  "answer": "中医治疗感冒主要依据辨证论治..."
}`
    },
    {
        title: () => t('datasets.qa.acu.title'),
        description: () => t('datasets.qa.acu.desc'),
        githubLink: '',
        columns: commonColumns,
        data: [], // Placeholder
        codeExample: `
{
  "question": "足三里穴位的作用？",
  "answer": "调理脾胃，补中益气..."
}`
    },
    {
        title: () => t('datasets.qa.mra.title'),
        description: () => t('datasets.qa.mra.desc'),
        githubLink: '',
        columns: commonColumns,
        data: [], // Placeholder
        codeExample: `
{
  "case": "患者男，45岁...",
  "question": "请给出诊断和治法",
  "answer": "诊断为..."
}`
    }
])
</script>
