<template>
    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <n-data-table :columns="columns" :data="data" :pagination="pagination" :bordered="false" :single-line="false"
            :row-class-name="rowClassName" size="large" :remote="true" />
    </div>
</template>

<script setup>
import { defineProps, computed } from 'vue'

const props = defineProps({
    columns: {
        type: Array,
        required: true
    },
    data: {
        type: Array,
        required: true
    },
    pagination: {
        type: [Object, Boolean],
        default: () => ({ pageSize: 10 })
    }
})

// 行样式：前三名高亮
const rowClassName = (row, index) => {
    if (index === 0) return 'rank-1'
    if (index === 1) return 'rank-2'
    if (index === 2) return 'rank-3'
    return ''
}
</script>

<style scoped>
:deep(.n-data-table-th) {
    background-color: #f8fafc;
    font-weight: 600;
    color: #334155;
}

:deep(.rank-1 td) {
    background-color: #fefce8;
    /* Yellow-50 */
}

:deep(.rank-2 td) {
    background-color: #f9fafb;
    /* Gray-50 */
}

:deep(.rank-3 td) {
    background-color: #fff7ed;
    /* Orange-50 */
}
</style>
