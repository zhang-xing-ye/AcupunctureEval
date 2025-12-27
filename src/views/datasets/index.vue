<template>
    <div class="datasets-container max-w-7xl mx-auto">
        <!-- Header -->
        <div class="mb-8">
            <h1 class="text-3xl font-bold text-gray-900">{{ datasetTitle }}</h1>
            <p class="text-gray-500 mt-2">
                {{ t('datasets.index.browse_desc', { type: datasetTypeLabel }) }}
            </p>
        </div>

        <!-- Dynamic Component Loading -->
        <transition name="fade" mode="out-in">
            <component :is="currentComponent" />
        </transition>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'

// Import Sub-views
import ChoiceView from './ChoiceView.vue'
import QAView from './QAView.vue'
import VQAView from './VQAView.vue'
import VideoView from './VideoView.vue'

const route = useRoute()
const { t } = useI18n()

const datasetType = computed(() => route.meta.type)

const datasetTypeLabel = computed(() => {
    switch (datasetType.value) {
        case 'choice': return t('datasets.index.label_choice')
        case 'qa': return t('datasets.index.label_qa')
        case 'vqa': return t('datasets.index.label_vqa')
        case 'video': return t('datasets.index.label_video')
        default: return ''
    }
})

const datasetTitle = computed(() => {
    switch (datasetType.value) {
        case 'choice': return t('nav.data_choice')
        case 'qa': return t('nav.data_qa')
        case 'vqa': return t('nav.data_vqa')
        case 'video': return t('nav.data_video')
        default: return '未知数据集'
    }
})

const currentComponent = computed(() => {
    switch (datasetType.value) {
        case 'choice': return ChoiceView
        case 'qa': return QAView
        case 'vqa': return VQAView
        case 'video': return VideoView
        default: return null
    }
})
</script>

<style scoped>
.datasets-container {
    padding: 1rem;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
