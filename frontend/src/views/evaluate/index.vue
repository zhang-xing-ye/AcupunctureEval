<template>
    <div class="evaluate-container max-w-7xl mx-auto px-4 py-8">
        <!-- 页面顶部标题区域 -->
        <div class="mb-8 text-center">
            <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ t('evaluate.title') }}</h1>
            <p class="text-gray-500 max-w-2xl mx-auto">{{ t('evaluate.description') }}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- QA 客观题评估卡片 -->
            <EvaluationCard ref="qaCardRef" :title="t('evaluate.qa_title')" :instruction="t('evaluate.qa_instruction')"
                :file-types="qaFileTypes" i18n-prefix="evaluate.file_types.qa" :loading="isQaSubmitting"
                :reference-code="qaReferenceJson" @submit="handleQaSubmit" />

            <!-- VQA 评估卡片 -->
            <EvaluationCard ref="vqaCardRef" :title="t('evaluate.vqa_title')"
                :instruction="t('evaluate.vqa_instruction')" :file-types="vqaFileTypes"
                i18n-prefix="evaluate.file_types.vqa" :loading="isVqaSubmitting" :reference-code="vqaReferenceJson"
                @submit="handleVqaSubmit" />
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useMessage } from 'naive-ui'
import EvaluationCard from './components/EvaluationCard.vue'
import { vqaEvaluate } from '@/api/vqaLeaderboard'

const { t } = useI18n()
const message = useMessage()

// 组件引用
const qaCardRef = ref(null)
const vqaCardRef = ref(null)

// 提交加载状态
const isQaSubmitting = ref(false)
const isVqaSubmitting = ref(false)

// 参考案例数据
const qaReferenceJson = JSON.stringify([
    {
        "ID": "1",
        "question": "最早且体系比较完整的针灸专书是（ ）",
        "options": [
            "A.《针灸甲乙经》",
            "B.《灵枢》",
            "C.《明堂孔穴针灸治要》",
            "D.《针灸资生经》",
            "E.《十四经发挥》"
        ],
        "output": "A"
    },
], null, 4)

const vqaReferenceJson = JSON.stringify([
    {
        "ID": "1",
        "Type": "Image Understanding",
        "Class": "手太阴腧穴",
        "Images": [
            "图3-2-2.jpeg"
        ],
        "Question": "图片中可能包含选项中的哪些穴位？",
        "Options": [
            "A. 列缺",
            "B. 云门",
            "C. 孔最",
            "D. 经渠"
        ],
        "output": "B"
    },
], null, 4)

// --- 配置定义 ---

/**
 * QA 客观题文件类型配置
 */
const qaFileTypes = {
    a1: 'a1',
    a2: 'a2',
    a3: 'a3',
    a4: 'a4',
    b: 'b',
    x: 'x'
}

/**
 * VQA 视觉问答文件类型配置
 */
const vqaFileTypes = {
    single: 'single',
    multi: 'multi',
    localization: 'localization',
    operation: 'operation'
}

// --- 提交处理 ---

/**
 * 处理 QA 评估提交
 * 目前后端未实现 QA 评估接口，此处保留模拟逻辑或待后续实现
 */
const handleQaSubmit = async (data) => {
    isQaSubmitting.value = true
    try {
        // 模拟 API 调用
        await new Promise(resolve => setTimeout(resolve, 2000))
        message.success(t('evaluate.success_message'))
        // 重置表单
        qaCardRef.value?.reset()
    } catch (error) {
        message.error('QA Evaluation failed')
    } finally {
        isQaSubmitting.value = false
    }
}

/**
 * 处理 VQA 评估提交
 * 调用后端真实接口
 */
const handleVqaSubmit = async ({ llm_name, llm_org, files }) => {
    isVqaSubmitting.value = true
    try {
        const formData = new FormData()
        formData.append('llm_name', llm_name)
        if (llm_org) {
            formData.append('llm_org', llm_org)
        }

        // 映射文件字段到后端接口要求的字段名
        // backend/router/vqaRouter.py:
        // file_type_one_single, file_type_one_multi, file_type_two, file_type_three

        // files[key] 是 Naive UI 的 UploadFileInfo 对象，其中的 file 属性是真实的 JS File 对象
        if (files.single?.file) formData.append('file_type_one_single', files.single.file)
        if (files.multi?.file) formData.append('file_type_one_multi', files.multi.file)
        if (files.localization?.file) formData.append('file_type_two', files.localization.file)
        if (files.operation?.file) formData.append('file_type_three', files.operation.file)

        await vqaEvaluate(formData)

        message.success(t('evaluate.success_message'))
        // 重置表单
        vqaCardRef.value?.reset()
    } catch (error) {
        console.error('VQA Evaluation Error:', error)
        const errorMsg = error.response?.data?.detail || error.message || 'Evaluation failed'
        message.error(errorMsg)
    } finally {
        isVqaSubmitting.value = false
    }
}
</script>

<style scoped>
/* 页面容器样式，主要依赖 Tailwind CSS，此处无需额外样式 */
</style>