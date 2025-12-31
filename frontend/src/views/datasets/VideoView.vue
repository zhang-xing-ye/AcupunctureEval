<template>
    <div class="space-y-6">
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
            <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <div class="w-1 h-6 bg-teal-600 rounded-full"></div>
                {{ t('datasets.video.section1_title') }}
            </h3>

            <!-- Temporary Header Structure -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="space-y-3">
                    <div class="font-medium text-gray-700 border-b pb-2">{{ t('datasets.video.section1_title') }}</div>
                    <div
                        class="aspect-video bg-gray-100 rounded-lg overflow-hidden border border-gray-200 relative group">
                        <n-image src="/video1.png" alt="Video 1 Placeholder" class="w-full h-full object-cover"
                            object-fit="cover" />
                        <div
                            class="absolute inset-0 flex items-center justify-center bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity">
                            <div class="w-12 h-12 rounded-full bg-white/90 flex items-center justify-center pl-1">
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-teal-600"
                                    viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M8 5v14l11-7z" />
                                </svg>
                            </div>
                        </div>
                    </div>
                    <p class="text-sm text-gray-500">{{ t('datasets.video.section1_desc') }}</p>
                </div>

                <div class="space-y-3">
                    <div class="font-medium text-gray-700 border-b pb-2">{{ t('datasets.video.section2_title') }}</div>
                    <div
                        class="aspect-video bg-gray-100 rounded-lg overflow-hidden border border-gray-200 relative group">
                        <n-image src="/video2.png" alt="Video 2 Placeholder" class="w-full h-full object-cover"
                            object-fit="cover" />
                        <div
                            class="absolute inset-0 flex items-center justify-center bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity">
                            <div class="w-12 h-12 rounded-full bg-white/90 flex items-center justify-center pl-1">
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-teal-600"
                                    viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M8 5v14l11-7z" />
                                </svg>
                            </div>
                        </div>
                    </div>
                    <p class="text-sm text-gray-500">{{ t('datasets.video.section2_desc') }}</p>
                </div>
            </div>

            <!-- Data Table Placeholder -->
            <div class="mt-8">
                <h4 class="font-bold text-gray-800 mb-3">{{ t('datasets.video.metadata_title') }}</h4>
                <n-data-table :columns="columns" :data="videoData" :bordered="false" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const columns = [
    { title: () => t('datasets.columns.id'), key: 'id', width: 80 },
    { title: () => t('datasets.columns.video_title'), key: 'title' },
    { title: () => t('datasets.columns.duration'), key: 'duration', width: 100 },
    { title: () => t('datasets.columns.category'), key: 'category', width: 120 },
    { title: () => t('datasets.columns.description'), key: 'description', ellipsis: { tooltip: true } }
]

const videoData = [
    { id: 1, title: '针灸手法演示-提插法', duration: '05:30', category: '针灸', description: '详细演示了提插补泻的操作要领与注意事项。' },
    { id: 2, title: '名老中医脉诊教学', duration: '12:45', category: '诊断', description: '主要讲解常见病脉的指下感觉与临床意义。' },
    { id: 3, title: '推拿基本手法-滚法', duration: '08:20', category: '推拿', description: '滚法的动作要领与在颈肩腰腿痛中的应用。' },
    { id: 4, title: '舌诊典型案例分析', duration: '15:10', category: '诊断', description: '结合高清舌象图片，分析不同证型的舌象特征。' },
    { id: 5, title: '拔罐疗法操作规范', duration: '06:50', category: '外治', description: '闪罐、走罐、留罐等不同拔罐法的操作演示。' }
]
</script>
