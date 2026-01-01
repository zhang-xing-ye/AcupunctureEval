<template>
    <div class="h-16 px-4 flex items-center justify-between border-b border-gray-200 bg-white shadow-sm">
        <!-- Logo / Title -->
        <div class="flex items-center gap-3 cursor-pointer select-none" @click="router.push('/')">
            <!-- Logo Icon Placeholder -->
            <div class="w-9 h-9 bg-teal-600 rounded-lg flex items-center justify-center text-white shadow-sm">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path
                        d="M4.8 2.3A.3.3 0 1 0 5 2H4a2 2 0 0 0-2 2v5a6 6 0 0 0 6 6v0a6 6 0 0 0 6-6V4a2 2 0 0 0-2-2h-1a.3.3 0 1 0 .2.3V4a1 1 0 0 1 1 1v5a5 5 0 0 1-10 0V5a1 1 0 0 1 1-1h1.8" />
                </svg>
            </div>
            <span class="text-xl font-bold text-gray-800 tracking-tight">AcupunctureEval</span>
        </div>

        <!-- 导航栏 -->
        <div class="flex-1 flex justify-center">
            <n-menu mode="horizontal" :options="menuOptions" v-model:value="activeKey" responsive />
        </div>

        <!-- 右侧操作 -->
        <div class="flex items-center gap-4">
            <n-button quaternary circle @click="toggleLanguage" class="text-gray-600 hover:text-teal-600">
                <template #icon>
                    <span class="font-bold text-sm">{{ appStore.locale === 'zh-CN' ? 'EN' : '中' }}</span>
                </template>
            </n-button>
        </div>
    </div>
</template>

<script setup>
import { h, ref, computed, watch } from 'vue'
import { RouterLink, useRoute, useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useAppStore } from '@/stores/app'

const { t } = useI18n()

const appStore = useAppStore()
const route = useRoute()
const router = useRouter()

const activeKey = ref(null)

// 同步导航栏选中项与路由
watch(() => route.path, (path) => {
    if (path === '/' || path === '/home') {
        activeKey.value = 'home'
    } else if (path.includes('/datasets')) {
        // 找到子路由哪个被激活
        if (path.includes('qa')) activeKey.value = 'qa'
        else if (path.includes('vqa')) activeKey.value = 'vqa'
        else if (path.includes('video')) activeKey.value = 'video'
        else activeKey.value = 'data'
    } else if (path.includes('/leaderboard')) {
        activeKey.value = 'leaderboard'
    } else if (path.includes('/evaluate')) {
        activeKey.value = 'evaluate'
    } else {
        activeKey.value = null
    }
}, { immediate: true })

// 导航栏选项
const menuOptions = computed(() => [
    {
        label: () => h(RouterLink, { to: '/' }, { default: () => t('nav.home') }),
        key: 'home',
    },
    {
        label: t('nav.data'),
        key: 'data',
        children: [
            {
                label: () => h(RouterLink, { to: '/datasets/qa' }, { default: () => t('nav.data_qa') }),
                key: 'qa'
            },
            {
                label: () => h(RouterLink, { to: '/datasets/vqa' }, { default: () => t('nav.data_vqa') }),
                key: 'vqa'
            },
            {
                label: () => h(RouterLink, { to: '/datasets/video' }, { default: () => t('nav.data_video') }),
                key: 'video'
            }
        ]
    },
    {
        label: () => h(RouterLink, { to: '/leaderboard' }, { default: () => t('nav.leaderboard') }),
        key: 'leaderboard',
    },
    {
        label: () => h(RouterLink, { to: '/evaluate' }, { default: () => t('nav.evaluate') }),
        key: 'evaluate',
    },
    {
        label: () => h('a', { href: 'https://github.com/your-repo', target: '_blank', rel: 'noopener noreferrer', class: 'flex items-center gap-1' }, {
            default: () => [
                t('nav.github'),
                h('span', { class: 'text-xs opacity-50' }, '↗')
            ]
        }),
        key: 'github',
    }
])

const toggleLanguage = () => {
    const newLang = appStore.locale === 'zh-CN' ? 'en-US' : 'zh-CN'
    appStore.setLocale(newLang)
}
</script>

<style scoped>
:deep(.n-menu-item-content-header) {
    font-weight: 500;
}
</style>
