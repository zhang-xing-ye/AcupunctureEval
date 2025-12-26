<template>
    <div class="datasets-container">
        <h1 class="text-2xl font-bold mb-4">数据集: {{ datasetTitle }}</h1>
        <p class="text-gray-600">
            这里将展示 {{ datasetType }} 相关的数据集内容。
        </p>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'

const route = useRoute()
const { t } = useI18n()

const datasetType = computed(() => route.meta.type)

const datasetTitle = computed(() => {
    const type = route.meta.type
    switch (type) {
        case 'choice': return t('nav.data_choice')
        case 'qa': return t('nav.data_qa')
        case 'vqa': return t('nav.data_vqa')
        case 'video': return t('nav.data_video')
        default: return '未知数据集'
    }
})
</script>

<style scoped>
.datasets-container {
    padding: 2rem;
}
</style>
