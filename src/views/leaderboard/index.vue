<template>
    <div class="leaderboard-container max-w-7xl mx-auto px-4 py-8">
        <!-- Header -->
        <div class="mb-8 text-center">
            <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ t('leaderboard.title') }}</h1>
            <p class="text-gray-500 max-w-2xl mx-auto">{{ t('leaderboard.description') }}</p>
        </div>

        <!-- Tabs & Content -->
        <n-tabs type="segment" animated size="large" class="custom-tabs" justify-content="center"
            @update:value="handleTabChange">
            <n-tab-pane name="overall" :tab="t('leaderboard.tabs.overall')">
                <div class="mt-6">
                    <LeaderboardTable :columns="overallColumns" :data="overallData" />
                </div>
            </n-tab-pane>
            <n-tab-pane name="choice" :tab="t('leaderboard.tabs.choice')">
                <div class="mt-6">
                    <LeaderboardTable :columns="choiceColumns" :data="choiceData" />
                </div>
            </n-tab-pane>
            <n-tab-pane name="qa" :tab="t('leaderboard.tabs.qa')">
                <div class="mt-6">
                    <LeaderboardTable :columns="qaColumns" :data="qaData" />
                </div>
            </n-tab-pane>
            <n-tab-pane name="vqa" :tab="t('leaderboard.tabs.vqa')">
                <div class="mt-6">
                    <LeaderboardTable :columns="vqaColumns" :data="vqaData" />
                </div>
            </n-tab-pane>
            <n-tab-pane name="video" :tab="t('leaderboard.tabs.video')">
                <div class="mt-6">
                    <LeaderboardTable :columns="videoColumns" :data="videoData" />
                </div>
            </n-tab-pane>
        </n-tabs>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { NTabs, NTabPane } from 'naive-ui'
import LeaderboardTable from './components/LeaderboardTable.vue'

const { t } = useI18n()

// --- Mock Data Generator ---
const generateData = (type) => {
    const models = [
        { name: 'TCM-LLM-Pro', org: 'TCM-AI Lab', params: '72B' },
        { name: 'HuatuoGPT-II', org: 'CUHK-SZ', params: '34B' },
        { name: 'ShenNong-TCM', org: 'TCM Research', params: '13B' },
        { name: 'Qwen-72B-Chat', org: 'Alibaba Cloud', params: '72B' },
        { name: 'GPT-4o', org: 'OpenAI', params: '-' },
        { name: 'Yi-34B-Chat', org: '01.AI', params: '34B' },
        { name: 'Baichuan2-13B', org: 'Baichuan', params: '13B' },
        { name: 'ChatGLM3-6B', org: 'Zhipu AI', params: '6B' },
        { name: 'InternLM2-20B', org: 'Shanghai AI Lab', params: '20B' },
        { name: 'Llama-3-70B', org: 'Meta', params: '70B' }
    ]

    return models.map((model, index) => {
        // Generate random scores based on rank slightly to simulate realistic data
        const baseScore = 90 - (index * 2.5) + (Math.random() * 2)

        return {
            rank: index + 1,
            model: model.name,
            org: model.org,
            params: model.params,
            score: baseScore.toFixed(1),
            choice_score: (baseScore + Math.random() * 5 - 2).toFixed(1),
            qa_score: (baseScore + Math.random() * 5 - 2).toFixed(1),
            vqa_score: (baseScore - 10 + Math.random() * 5).toFixed(1), // VQA usually harder
            video_score: (baseScore - 15 + Math.random() * 5).toFixed(1) // Video usually hardest
        }
    })
}

// Data for each tab
const overallData = generateData('overall')
const choiceData = generateData('choice').sort((a, b) => b.choice_score - a.choice_score).map((item, index) => ({ ...item, rank: index + 1 }))
const qaData = generateData('qa').sort((a, b) => b.qa_score - a.qa_score).map((item, index) => ({ ...item, rank: index + 1 }))
const vqaData = generateData('vqa').sort((a, b) => b.vqa_score - a.vqa_score).map((item, index) => ({ ...item, rank: index + 1 }))
const videoData = generateData('video').sort((a, b) => b.video_score - a.video_score).map((item, index) => ({ ...item, rank: index + 1 }))


// --- Column Definitions (Computed for i18n) ---

// Base columns
const baseColumns = computed(() => [
    { title: t('leaderboard.columns.rank'), key: 'rank', width: 80, align: 'center', sorter: 'default' },
    { title: t('leaderboard.columns.model'), key: 'model', width: 200, ellipsis: { tooltip: true } },
    { title: t('leaderboard.columns.org'), key: 'org', width: 150, ellipsis: { tooltip: true } },
    { title: t('leaderboard.columns.params'), key: 'params', width: 120, align: 'center' },
])

// Specific columns per tab
const overallColumns = computed(() => [
    ...baseColumns.value,
    { title: t('leaderboard.columns.score'), key: 'score', width: 100, align: 'center', sorter: (row1, row2) => row1.score - row2.score },
    { title: t('leaderboard.columns.choice_score'), key: 'choice_score', width: 100, align: 'center', sorter: (row1, row2) => row1.choice_score - row2.choice_score },
    { title: t('leaderboard.columns.qa_score'), key: 'qa_score', width: 100, align: 'center', sorter: (row1, row2) => row1.qa_score - row2.qa_score },
    { title: t('leaderboard.columns.vqa_score'), key: 'vqa_score', width: 100, align: 'center', sorter: (row1, row2) => row1.vqa_score - row2.vqa_score },
    { title: t('leaderboard.columns.video_score'), key: 'video_score', width: 100, align: 'center', sorter: (row1, row2) => row1.video_score - row2.video_score },
])

const choiceColumns = computed(() => [
    ...baseColumns.value,
    { title: t('leaderboard.columns.choice_score'), key: 'choice_score', width: 120, align: 'center', sorter: (row1, row2) => row1.choice_score - row2.choice_score }
])

const qaColumns = computed(() => [
    ...baseColumns.value,
    { title: t('leaderboard.columns.qa_score'), key: 'qa_score', width: 120, align: 'center', sorter: (row1, row2) => row1.qa_score - row2.qa_score }
])

const vqaColumns = computed(() => [
    ...baseColumns.value,
    { title: t('leaderboard.columns.vqa_score'), key: 'vqa_score', width: 120, align: 'center', sorter: (row1, row2) => row1.vqa_score - row2.vqa_score }
])

const videoColumns = computed(() => [
    ...baseColumns.value,
    { title: t('leaderboard.columns.video_score'), key: 'video_score', width: 120, align: 'center', sorter: (row1, row2) => row1.video_score - row2.video_score }
])

const handleTabChange = (value) => {
    // console.log(value)
}
</script>

<style scoped>
.custom-tabs :deep(.n-tabs-rail) {
    background-color: #f1f5f9;
    padding: 4px;
    border-radius: 9999px;
}

.custom-tabs :deep(.n-tabs-tab) {
    border-radius: 9999px;
    font-weight: 500;
}

.custom-tabs :deep(.n-tabs-tab--active) {
    background-color: white;
    box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
    color: #0d9488;
    /* teal-600 */
}
</style>
