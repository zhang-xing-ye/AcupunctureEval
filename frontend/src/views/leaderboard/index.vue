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
            <n-tab-pane name="qa_objective" :tab="t('leaderboard.tabs.qa_objective')">
                <div class="mt-6">
                    <LeaderboardTable :columns="qaObjectiveColumns" :data="qaObjectiveData"
                        :pagination="qaPagination" />
                </div>
            </n-tab-pane>
            <n-tab-pane name="vqa" :tab="t('leaderboard.tabs.vqa')">
                <div class="mt-6">
                    <LeaderboardTable :columns="vqaColumns" :data="vqaData" :pagination="pagination" />
                </div>
            </n-tab-pane>
        </n-tabs>
    </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { NTabs, NTabPane, useMessage } from 'naive-ui'
import LeaderboardTable from './components/LeaderboardTable.vue'
import { getVqaLeaderboard } from '@/api/vqaLeaderboard'
import { getQALeaderboard } from '@/api/qaLeaderboard'

const { t } = useI18n()
const message = useMessage()

// Data for each tab
const qaObjectiveData = ref([])
const qaPagination = ref({
    page: 1,
    pageSize: 10,
    itemCount: 0,
    onChange: (page) => {
        qaPagination.value.page = page
        fetchQaData()
    },
    onUpdatePageSize: (pageSize) => {
        qaPagination.value.pageSize = pageSize
        qaPagination.value.page = 1
        fetchQaData()
    }
})

const vqaData = ref([])
const pagination = ref({
    page: 1,
    pageSize: 10,
    itemCount: 0,
    onChange: (page) => {
        pagination.value.page = page
        fetchVqaData()
    },
    onUpdatePageSize: (pageSize) => {
        pagination.value.pageSize = pageSize
        pagination.value.page = 1
        fetchVqaData()
    }
})

// Fetch VQA Data from API
const fetchVqaData = async () => {
    const params = {
        skip: (pagination.value.page - 1) * pagination.value.pageSize,
        limit: pagination.value.pageSize
    }
    const response = await getVqaLeaderboard(params)
    // 数据映射
    vqaData.value = response.items.map((item, index) => ({
        rank: (pagination.value.page - 1) * pagination.value.pageSize + index + 1,
        model: item.llm_name,
        single_choice: (item.type_one_single_score * 100).toFixed(2),
        multiple_choice: (item.type_one_multi_score * 100).toFixed(2),
        localization: (item.type_two_score * 100).toFixed(2),
        operation: (item.type_three_score * 100).toFixed(2),
        average: (item.avg_score * 100).toFixed(2)
    }))
    pagination.value.itemCount = response.total
}

// Fetch QA Data from API
const fetchQaData = async () => {
    const params = {
        skip: (qaPagination.value.page - 1) * qaPagination.value.pageSize,
        limit: qaPagination.value.pageSize
    }
    const response = await getQALeaderboard(params)
    // 数据映射
    qaObjectiveData.value = response.items.map((item, index) => ({
        rank: (qaPagination.value.page - 1) * qaPagination.value.pageSize + index + 1,
        model: item.llm_name,
        a1: (item.a1_score * 100).toFixed(2),
        a2: (item.a2_score * 100).toFixed(2),
        a3: (item.a3_score * 100).toFixed(2),
        a4: (item.a4_score * 100).toFixed(2),
        b: (item.b_score * 100).toFixed(2),
        x: (item.x_score * 100).toFixed(2),
        average: (item.avg_score * 100).toFixed(2)
    }))
    qaPagination.value.itemCount = response.total
}

onMounted(() => {
    fetchVqaData()
    fetchQaData()
})


// --- Column Definitions (Computed for i18n) ---

// Base columns
const baseColumns = computed(() => [
    { title: t('leaderboard.columns.rank'), key: 'rank', width: 80, align: 'center', sorter: 'default' },
    { title: t('leaderboard.columns.model'), key: 'model', width: 200, ellipsis: { tooltip: true } },
])

// Specific columns per tab
const qaObjectiveColumns = computed(() => [
    ...baseColumns.value,
    { title: t('leaderboard.columns.a1'), key: 'a1', width: 100, align: 'center', sorter: (row1, row2) => row1.a1 - row2.a1 },
    { title: t('leaderboard.columns.a2'), key: 'a2', width: 100, align: 'center', sorter: (row1, row2) => row1.a2 - row2.a2 },
    { title: t('leaderboard.columns.a3'), key: 'a3', width: 100, align: 'center', sorter: (row1, row2) => row1.a3 - row2.a3 },
    { title: t('leaderboard.columns.a4'), key: 'a4', width: 100, align: 'center', sorter: (row1, row2) => row1.a4 - row2.a4 },
    { title: t('leaderboard.columns.b'), key: 'b', width: 100, align: 'center', sorter: (row1, row2) => row1.b - row2.b },
    { title: t('leaderboard.columns.x'), key: 'x', width: 100, align: 'center', sorter: (row1, row2) => row1.x - row2.x },
    { title: t('leaderboard.columns.average'), key: 'average', width: 100, align: 'center', sorter: (row1, row2) => row1.average - row2.average },
])

const vqaColumns = computed(() => [
    ...baseColumns.value,
    { title: t('leaderboard.columns.single_choice'), key: 'single_choice', width: 120, align: 'center', sorter: (row1, row2) => row1.single_choice - row2.single_choice },
    { title: t('leaderboard.columns.multiple_choice'), key: 'multiple_choice', width: 120, align: 'center', sorter: (row1, row2) => row1.multiple_choice - row2.multiple_choice },
    { title: t('leaderboard.columns.localization'), key: 'localization', width: 120, align: 'center', sorter: (row1, row2) => row1.localization - row2.localization },
    { title: t('leaderboard.columns.operation'), key: 'operation', width: 120, align: 'center', sorter: (row1, row2) => row1.operation - row2.operation },
    { title: t('leaderboard.columns.average'), key: 'average', width: 120, align: 'center', sorter: (row1, row2) => row1.average - row2.average },
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
