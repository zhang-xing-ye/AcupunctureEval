<template>
    <div class="space-y-6">
        <div v-for="(section, index) in sections" :key="index"
            class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
            <!-- 标题与描述 -->
            <div class="mb-4">
                <h3 class="text-lg font-bold text-gray-900 flex items-center gap-2">
                    <div class="w-1 h-6 bg-teal-600 rounded-full"></div>
                    <!-- 支持动态标题（函数或字符串） -->
                    {{ typeof section.title === 'function' ? section.title() : section.title }}
                </h3>
                <!-- 支持动态描述（函数或字符串） -->
                <p v-if="section.description" class="text-gray-500 mt-2 text-sm">
                    {{ typeof section.description === 'function' ? section.description() : section.description }}
                </p>
                <div v-if="section.githubLink" class="mt-2">
                    <a :href="section.githubLink" target="_blank"
                        class="text-teal-600 hover:text-teal-700 text-sm flex items-center gap-1 inline-flex">
                        <span>View on GitHub</span>
                        <span class="text-xs">↗</span>
                    </a>
                </div>
            </div>

            <!-- 数据表格 -->
            <n-data-table :columns="section.columns" :data="section.data" :bordered="false" :single-line="false"
                class="mb-6" />

            <!-- 代码示例 -->
            <div v-if="section.codeExample" class="bg-gray-50 rounded-lg border border-gray-200 overflow-hidden">
                <div class="px-4 py-2 bg-gray-100 border-b border-gray-200 text-xs font-mono text-gray-500">
                    JSON Example
                </div>
                <n-config-provider :hljs="hljs">
                    <n-code :code="section.codeExample" language="json" class="p-4 text-sm" />
                </n-config-provider>
            </div>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue'
import hljs from 'highlight.js/lib/core'
import json from 'highlight.js/lib/languages/json'

hljs.registerLanguage('json', json)

defineProps({
    sections: {
        type: Array,
        required: true
    }
})
</script>
