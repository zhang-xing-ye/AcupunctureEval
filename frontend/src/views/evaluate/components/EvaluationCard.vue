<template>
    <n-card :title="title" size="large" class="shadow-sm hover:shadow-md transition-shadow">
        <template #header-extra>
            <div class="flex items-center gap-2">
                <n-button v-if="referenceCode" size="small" secondary type="primary" @click="showModal = true">
                    {{ t('evaluate.reference_button') }}
                </n-button>
                <n-tag type="info" size="small">JSON</n-tag>
            </div>
        </template>

        <!-- 顶部说明文案 -->
        <div class="mb-6 text-gray-500">
            {{ instruction }}
        </div>

        <!-- Metadata Inputs -->
        <div v-if="showMeta" class="mb-6 grid grid-cols-1 gap-4 md:grid-cols-2">
            <div class="flex flex-col gap-1">
                <label class="text-sm font-medium text-gray-700">{{ t('evaluate.llm_name_label') }} <span
                        class="text-red-500">*</span></label>
                <n-input v-model:value="llmName" :placeholder="t('evaluate.llm_name_placeholder')" />
            </div>
            <div class="flex flex-col gap-1">
                <label class="text-sm font-medium text-gray-700">{{ t('evaluate.llm_org_label') }}</label>
                <n-input v-model:value="llmOrg" :placeholder="t('evaluate.llm_org_placeholder')" />
            </div>
        </div>

        <!-- 文件上传列表区域 -->
        <div class="space-y-6">
            <div v-for="(label, type) in fileTypes" :key="type" class="border rounded-lg p-4 bg-gray-50">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-2">
                        <!-- 文件类型名称 -->
                        <span class="font-medium text-gray-700">{{ getFileLabel(type) }}</span>
                        <!-- 上传成功标记 -->
                        <n-tag v-if="files[type]" type="success" size="small" round>
                            ✓ {{ t('evaluate.upload_success', { name: '' }).replace('文件 上传成功', '已上传') }}
                        </n-tag>
                    </div>
                </div>

                <!-- 单个文件上传组件 -->
                <n-upload :max="1" accept=".json" :show-file-list="true"
                    :custom-request="(options) => customUploadRequest(options, type)" @before-upload="beforeUpload"
                    @remove="() => handleRemove(type)">
                    <n-button dashed block class="w-full">
                        {{ t('evaluate.upload_button') }}
                    </n-button>
                </n-upload>
            </div>
        </div>

        <!-- 底部提交区域 -->
        <div class="mt-8 flex flex-col items-end gap-2">
            <n-button type="primary" size="large" block :disabled="!canSubmit" :loading="loading" @click="submit">
                {{ t('evaluate.submit_button') }}
            </n-button>
            <!-- 缺失文件提示 -->
            <n-text v-if="!canSubmit && hasAnyFile" type="error" class="text-xs text-center w-full block">
                {{ t('evaluate.missing_files', { files: missingFiles }) }}
            </n-text>
        </div>
    </n-card>

    <!-- Reference Modal -->
    <n-modal v-model:show="showModal" preset="card" :title="t('evaluate.reference_title')" class="w-[95vw] max-w-3xl"
        :style="{ width: '800px' }">
        <div class="space-y-4">
            <p class="text-gray-600">{{ referenceText || t('evaluate.reference_description') }}</p>
            <div class="bg-gray-50 p-4 rounded-md border overflow-auto max-h-[60vh]">
                <n-code :code="referenceCode" language="json" :hljs="hljs" />
            </div>
        </div>
    </n-modal>
</template>

<script setup>
import { ref, computed, reactive } from 'vue'
import { useI18n } from 'vue-i18n'
import { useMessage, NCard, NUpload, NButton, NTag, NText, NInput, NModal, NCode } from 'naive-ui'
import hljs from 'highlight.js/lib/core'
import json from 'highlight.js/lib/languages/json'

hljs.registerLanguage('json', json)

const props = defineProps({
    title: {
        type: String,
        required: true
    },
    instruction: {
        type: String,
        required: true
    },
    // 文件类型定义对象 { key: labelKey }
    fileTypes: {
        type: Object,
        required: true
    },
    // 用于构建国际化 key 的前缀，如 'evaluate.file_types.qa'
    i18nPrefix: {
        type: String,
        required: true
    },
    loading: {
        type: Boolean,
        default: false
    },
    showMeta: {
        type: Boolean,
        default: true
    },
    referenceCode: {
        type: String,
        default: ''
    },
    referenceText: {
        type: String,
        default: ''
    }
})

const emit = defineEmits(['submit'])

const { t } = useI18n()
const message = useMessage()

// Modal state
const showModal = ref(false)

// 存储已上传的文件对象: { a1: fileObj, a2: null, ... }
const files = reactive(
    Object.keys(props.fileTypes).reduce((acc, type) => ({ ...acc, [type]: null }), {})
)

const llmName = ref('')
const llmOrg = ref('')

// 获取文件类型的显示名称
const getFileLabel = (type) => {
    return t(`${props.i18nPrefix}.${type}`)
}

// --- 上传逻辑 ---

/**
 * 上传前校验
 * 仅允许上传 JSON 格式文件
 */
const beforeUpload = (data) => {
    if (data.file.file?.type !== 'application/json' && !data.file.name.endsWith('.json')) {
        message.error(t('evaluate.error_file_type'))
        return false
    }
    return true
}

/**
 * 自定义上传请求
 * 这里只负责将文件保存到状态中，不进行实际网络请求
 */
const customUploadRequest = ({ file, onFinish }, type) => {
    files[type] = file
    onFinish()
    message.success(t('evaluate.upload_success', { name: file.name }))
}

/**
 * 处理文件移除
 * 清空对应类型的状态
 */
const handleRemove = (type) => {
    files[type] = null
}

// --- 校验与计算属性 ---

/**
 * 是否可以提交
 * 只有当所有类型的文件都已上传且必填元数据已填写时才为 true
 */
const canSubmit = computed(() => {
    const filesOk = Object.values(files).every(file => file !== null)
    if (props.showMeta) {
        return filesOk && llmName.value.trim() !== ''
    }
    return filesOk
})

/**
 * 是否有任意文件已上传
 * 用于控制错误提示的显示时机（完全未上传时不显示错误）
 */
const hasAnyFile = computed(() => {
    return Object.values(files).some(file => file !== null)
})

/**
 * 获取缺失的文件类型列表
 * 用于在提交按钮下方显示提示
 */
const missingFiles = computed(() => {
    return Object.entries(files)
        .filter(([_, file]) => file === null)
        .map(([type, _]) => getFileLabel(type))
        .join(', ')
})

// --- 提交操作 ---

const submit = () => {
    if (!canSubmit.value) return

    emit('submit', {
        llm_name: llmName.value,
        llm_org: llmOrg.value,
        files: { ...files }
    })
}

// 暴露重置方法供父组件调用
const reset = () => {
    Object.keys(files).forEach(key => files[key] = null)
    llmName.value = ''
    llmOrg.value = ''
}

defineExpose({ reset })
</script>